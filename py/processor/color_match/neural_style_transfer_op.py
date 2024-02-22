import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
from torchvision.models import vgg19, VGG19_Weights

import copy


def neural_style_transfer(content_img, 
                          style_img, 
                          model, 
                          optimizer, 
                          num_steps, 
                          style_weight, 
                          content_weight, 
                          resolution, 
                          device):
    
    output_image = torch.randn(1, 512, 512, 3)
    
    return output_image
