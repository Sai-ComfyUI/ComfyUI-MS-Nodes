import torch

def separate_rgb(tensor_image):
    # hwc_image = tensor_image.squeeze(0)
    # chw_tensor = hwc_image.permute(2, 0, 1)
    r = tensor_image[:, :, :, 0].repeat(3, 1, 1).permute(1, 2, 0).unsqueeze(0)
    g = tensor_image[:, :, :, 1].repeat(3, 1, 1).permute(1, 2, 0).unsqueeze(0)
    b = tensor_image[:, :, :, 2].repeat(3, 1, 1).permute(1, 2, 0).unsqueeze(0)
    
    return (r, g, b)

def combine_rgb(r, g, b):
    # hwc_image = tensor_image.squeeze(0)
    # chw_tensor = hwc_image.permute(2, 0, 1)
    extract_r = r[:, :, :, 0]
    extract_g = g[:, :, :, 1]
    extract_b = b[:, :, :, 2]
    chw_tensor = torch.stack([extract_r, extract_g, extract_b], dim=-1)
    # bhwc_tensor = chw_tensor.permute(1, 2, 0).unsqueeze(0)
    
    return (chw_tensor)