import os
from .....modules import comm_funcs
from . import pillow_filters_op as op

class Pillow_BoxBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "radius": ("FLOAT", {"default": 1, "min": 0, "max": 100}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, radius):
        out = image
        out = op.pillow_box_blur(image, radius)
        return (out,)

class Pillow_GaussianBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "radius": ("FLOAT", {"default": 1, "min": 0, "max": 100}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, radius):
        out = image
        out = op.pillow_gaussian_blur(image, radius)
        return (out,)

class Pillow_UnsharpMask:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "radius": ("INT", {"default": 2, "min": 0, "max": 100}),
                "percent": ("INT", {"default": 150, "min": 0, "max": 99999}),
                "threshold": ("INT", {"default": 2, "min": 0, "max": 100}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, radius:float, percent:float, threshold:float):
        out = image
        out = op.pillow_unsharp_mask(image, radius, percent, threshold)
        return (out,)

class Pillow_Effects:
    @classmethod
    def INPUT_TYPES(cls):
        effect_list = ["BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EDGE_ENHANCE_MORE",
                "EMBOSS", "FIND_EDGES", "SHARPEN", "SMOOTH", "SMOOTH_MORE"]
        return {
            "required":
                {
                "image": ("IMAGE",),
                "effect": (effect_list,),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, effect):
        out = image
        out = op.pillow_effects(image, effect)
        return (out,)

NODE_CLASS_MAPPINGS = {
    "Pillow_BoxBlur": Pillow_BoxBlur,
    "Pillow_GaussianBlur": Pillow_GaussianBlur,
    "Pillow_UnsharpMask": Pillow_UnsharpMask,
    "Pillow_Effects": Pillow_Effects,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Pillow_BoxBlur": "Pillow BoxBlur (MS)",
    "Pillow_GaussianBlur": "Pillow GaussianBlur (MS)",
    "Pillow_UnsharpMask": "Pillow UnsharpMask (MS)",
    "Pillow_Effects": "Pillow Effects (MS)",
}

