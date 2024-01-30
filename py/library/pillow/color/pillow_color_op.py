from pillow_lut import load_cube_file 
from .....modules import image_funcs

def pillow_apply_luts(image, luts_file):
    image = image_funcs.tensor_to_pil(image)
    color_lut = load_cube_file(luts_file)
    image = image.filter(color_lut)
    image = image_funcs.pil_to_tensor(image)

    return image
