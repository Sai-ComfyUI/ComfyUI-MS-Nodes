import torch
import numpy as np
from PIL import Image
import cv2



def tensor_to_pil(tensor_image, batch_index=0):
    # Convert tensor of shape [batch_size, channels, height, width] at the batch_index to PIL Image
    tensor_image = tensor_image[batch_index].unsqueeze(0)
    i = 255. * tensor_image.cpu().numpy()
    pil_image = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8).squeeze())
    return pil_image

def batch_tensor_to_pil(tensor_image):
    # Convert tensor of shape [batch_size, channels, height, width] to a list of PIL Images
    return [tensor_to_pil(tensor_image, i) for i in range(tensor_image.shape[0])]


def pil_to_tensor(image):
    # Takes a PIL image and returns a tensor of shape [1, height, width, channels]
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image).unsqueeze(0)
    if len(image.shape) == 3:  # If the image is grayscale, add a channel dimension
        image = image.unsqueeze(-1)
        
    return image


def batched_pil_to_tensor(images):
    # Takes a list of PIL images and returns a tensor of shape [batch_size, height, width, channels]
    return torch.cat([pil_to_tensor(image) for image in images], dim=0)


def tensor_to_cv2(tensor_image):
    numpy_image = tensor_image.numpy()
    numpy_image = numpy_image.squeeze()
    numpy_image = (numpy_image * 255).astype(np.uint8)
    
    # to pil
    # pil_image = Image.fromarray(numpy_image)
    
    # to cv2
    if len(numpy_image.shape) == 2: # 灰階的狀況
        numpy_image = cv2.cvtColor(numpy_image, cv2.COLOR_GRAY2BGR)
    cv2_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    return cv2_image

def cv2_to_tensor(cv2_image, batch_index=0):
    # 將BGR轉換為RGB
    cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
    # 將數據類型轉換為float32，並歸一化到[0, 1]範圍
    tensor_image = torch.from_numpy(cv2_image.astype(np.float32) / 255.0)
    # 將通道維度移到最前面（C,H,W）
    # tensor_image = tensor_image.permute(2, 0, 1)
    tensor_image = tensor_image.unsqueeze(0)
    return tensor_image

def cv2_to_pil(cv2_image):
    pil_image = Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
    return pil_image