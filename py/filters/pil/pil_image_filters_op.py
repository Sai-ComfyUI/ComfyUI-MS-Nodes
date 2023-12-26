from PIL import Image, ImageFilter
from ....modules import image_funcs


def pil_box_blur(image, radius: float):
    image = image_funcs.tensor_to_pil(image)
    pil_filter = ImageFilter.BoxBlur(radius=radius)
    image = image.filter(pil_filter)
    image = image_funcs.pil_to_tensor(image)

    return image


def pil_gaussian_blur(image, radius: float):
    image = image_funcs.tensor_to_pil(image)
    pil_filter = ImageFilter.GaussianBlur(radius=radius)
    image = image.filter(pil_filter)
    image = image_funcs.pil_to_tensor(image)

    return image


def pil_unsharp_mask(image, radius: int, percent: int, threshold: int):
    image = image_funcs.tensor_to_pil(image)
    pil_filter = ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold)
    image = image.filter(pil_filter)
    image = image_funcs.pil_to_tensor(image)

    return image


def pil_effects(image, effect:str):
    image = image_funcs.tensor_to_pil(image)
    
    pil_filter = getattr(ImageFilter, effect)
    image = image.filter(pil_filter)
    image = image_funcs.pil_to_tensor(image)

    return image