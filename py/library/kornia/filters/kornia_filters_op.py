import torch
from kornia import filters
from einops import rearrange


def make_odd(number):
    if number % 2 == 0:
        number += 1
    return number


def bilateral_blur(input: torch.tensor, kernel_size, sigma_color, sigma_space, border_type):
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(sigma_space, float):
        sigma_space = (sigma_space, sigma_space)

    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.bilateral_blur(input, kernel_size, sigma_color, sigma_space, border_type, color_distance_type='l1')
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor


def blur_pool2d(input: torch.tensor, kernel_size, stride):
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.blur_pool2d(input, kernel_size, stride)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor


def box_blur(input: torch.tensor, kernel_size, border_type, separable):
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.box_blur(input, kernel_size, border_type, separable)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor


def gaussian_blur2d(input: torch.tensor, kernel_size, sigma, border_type, separable):
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(sigma, float):
        sigma = (sigma, sigma)
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.gaussian_blur2d(input, kernel_size, sigma, border_type, separable)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor


def guided_blur(input: torch.tensor, guidance: torch.tensor, kernel_size=(3, 3), eps=0.1, border_type='reflect', subsample=1):
    image_tensor = filters.guided_blur(
        guidance, input, kernel_size, eps, border_type, subsample)

    return image_tensor


def joint_bilateral_blur(input: torch.tensor, guidance: torch.tensor, kernel_size=(3, 3), sigma_color=0.1, sigma_space=(1.5, 1.5), border_type='reflect'):
    image_tensor = filters.joint_bilateral_blur(
        input, guidance, kernel_size, sigma_color, sigma_space, border_type, color_distance_type='l1')

    return image_tensor


def max_blur_pool2d(input: torch.tensor, kernel_size=(3, 3), stride=2, max_pool_size=2, ceil_mode=False):
    image_tensor = filters.max_blur_pool2d(
        input, kernel_size, stride, max_pool_size, ceil_mode=False)

    return image_tensor


def median_blur(input: torch.tensor, kernel_size=(3, 3)):
    image_tensor = filters.median_blur(input, kernel_size)

    return image_tensor


def motion_blur(input: torch.tensor, kernel_size=(3, 3), angle=90., direction=1, border_type='constant', mode='nearest'):
    image_tensor = filters.motion_blur(
        input, kernel_size, angle, direction, border_type, mode)

    return image_tensor


def unsharp_mask(input: torch.tensor, kernel_size=(3, 3), sigma=(1.5, 1.5), border_type='reflect'):
    image_tensor = filters.unsharp_mask(input, kernel_size, sigma, border_type)

    return image_tensor


# Edge detection
def canny(input: torch.tensor, low_threshold=0.1, high_threshold=0.2, kernel_size=(5, 5), sigma=(1, 1), hysteresis=True):
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(sigma, float):
        sigma = (sigma, sigma)
    input = rearrange(input, 'b h w c-> b c h w')
    edge_magnitudes, edge_detection = filters.canny(
        input, low_threshold, high_threshold, kernel_size, sigma, hysteresis, eps=1e-6)

    edge_magnitudes = rearrange(
        edge_magnitudes, 'b c h w-> b h w c').expand(-1, -1, -1, 3)
    edge_detection = rearrange(
        edge_detection, 'b c h w-> b h w c').expand(-1, -1, -1, 3)

    return (edge_magnitudes, edge_detection)


def laplacian(input: torch.tensor, kernel_size, border_type='reflect', normalized=True):
    kernel_size = make_odd(kernel_size)
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.laplacian(
        input, kernel_size, border_type, normalized)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor


def sobel(input: torch.tensor, normalized=True):
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor = filters.sobel(input, normalized, eps=1e-6)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor
