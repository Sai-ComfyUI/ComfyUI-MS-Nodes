from PIL import Image
import io
from pillow_lut import load_cube_file, load_hald_image, rgb_color_enhance
from .....modules import image_funcs, folder_paths

luts_folder = r"%s\luts" % folder_paths.folder_names_and_paths['assets']

def pillow_apply_cube_luts(image, luts_file):
    image = image_funcs.tensor_to_pil(image)
    luts_file = r"%s\%s" % (luts_folder, luts_file)
    color_lut = load_cube_file(luts_file)
    image = image.filter(color_lut)
    image = image_funcs.pil_to_tensor(image)

    return image

def pillow_hald_image(image, hald_image):
    image = image_funcs.tensor_to_pil(image)
    hald_image = image_funcs.tensor_to_pil(hald_image)
    #force to 512*512 png
    hald_image = hald_image.resize((512, 512))
    png_data = io.BytesIO()
    hald_image.save(png_data, format='PNG')
    png_data.seek(0)

    luts_from_image = load_hald_image(png_data)
    image = image.filter(luts_from_image)
    image = image_funcs.pil_to_tensor(image)

    return image


def pillow_rgb_color_enhance(image, table_size, brightness, exposure, contrast, warmth, saturation, vibrance, hue, gamma, linear):
    image = image_funcs.tensor_to_pil(image)
    color_lut = rgb_color_enhance(table_size, brightness, exposure, contrast, warmth, saturation, vibrance, hue, gamma, linear)
    image = image.filter(color_lut)
    image = image_funcs.pil_to_tensor(image)

    return image