from PIL import Image
from ...modules import image_funcs

def Pli_box_blur(image, lock_ratio, radius_x, radius_y):
    # print (type(image))
    pli_image = image_funcs.tensor_to_pil(image)
    
    
    return image