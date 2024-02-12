import os
from .....modules import comm_funcs, folder_paths
from . import pillow_color_op as op

luts_folder = r"%s\luts" % folder_paths.folder_names_and_paths['assets']
luts_files = comm_funcs.list_files_with_extensions(luts_folder, extensions=[".cube"], rel_path=True)

class Pillow_LUTs_FromCube:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "luts_file" : (luts_files,),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, luts_file):
        image_tensor = op.pillow_apply_cube_luts(image, luts_file)
        return (image_tensor,)


class Pillow_LUTs_FromHaldImage:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "hald_image": ("IMAGE",),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, hald_image):
        image_tensor = op.pillow_hald_image(image, hald_image)
        return (image_tensor,)


class Pillow_RGBColorEnhance:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "table_size": ("INT", {"default": 11, "min": 2, "max": 65, "step": 1}),
                "brightness": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01}),
                "exposure": ("FLOAT", {"default": 0, "min": -5, "max": 5, "step": 0.01}),
                "contrast": ("FLOAT", {"default": 0, "min": -1, "max": 5, "step": 0.01}),
                "warmth": ("FLOAT", {"default": 0, "min": -1, "max": 1, "step": 0.01}),
                "saturation": ("FLOAT", {"default": 0, "min": -1, "max": 5, "step": 0.01}),
                "vibrance": ("FLOAT", {"default": 0, "min": -1, "max": 5, "step": 0.01}),
                "hue": ("FLOAT", {"default": 0, "min": 0, "max": 1, "step": 0.01}),
                "gamma": ("FLOAT", {"default": 1, "min": 0, "max": 10, "step": 0.01}),
                "linear": ("BOOLEAN", {"default": False}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, table_size, brightness, exposure, contrast, warmth, saturation, vibrance, hue, gamma, linear):
        out = image
        out = op.pillow_rgb_color_enhance(image, table_size, brightness, exposure, contrast, warmth, saturation, vibrance, hue, gamma, linear)
        return (out,)


NODE_CLASS_MAPPINGS = {
    "Pillow_LUTs_FromCube": Pillow_LUTs_FromCube,
    "Pillow_LUTs_FromHaldImage": Pillow_LUTs_FromHaldImage,
    "Pillow_RGBColorEnhance": Pillow_RGBColorEnhance,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Pillow_LUTs_FromCube": "Pillow Apply Cube LUTs (MS)",
    "Pillow_LUTs_FromHaldImage": "Pillow Apply LUTs From Hald (MS)",
    "Pillow_RGBColorEnhance": "Pillow RGB Color Enhance (MS)",
}

