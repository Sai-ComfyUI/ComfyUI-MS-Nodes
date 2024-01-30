import torch
from kornia import feature
from einops import rearrange

# 
def make_odd(number):
    if number % 2 == 0:
        number += 1
    return number

# feature
def dog_response_single(input: torch.tensor, sigma1=1.0, sigma2=1.6):
    input = rearrange(input, 'b h w c-> b c h w')
    image_tensor  = feature.dog_response_single(input, sigma1, sigma2)
    image_tensor = rearrange(image_tensor, 'b c h w-> b h w c')

    return image_tensor
