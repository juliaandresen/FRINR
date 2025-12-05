import torch
import torch.nn.functional as F


def interpolate(image, mode='bilinear', size=(224, 224)):
    
    image = F.interpolate(image, size)
    
    return image

