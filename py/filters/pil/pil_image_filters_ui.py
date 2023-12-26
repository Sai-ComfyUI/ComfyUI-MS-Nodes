import os
from ....modules import comm_funcs
from . import pil_image_filters_op as op

class Pil_Color3DLUT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
                },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("SEED",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, seed=0):
        """Returns the passed seed on execution."""
        return (seed,)
    
class Pil_BoxBlur:
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
        out = op.pil_box_blur(image, radius)
        return (out,)

class Pil_GaussianBlur:
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
        out = op.pil_gaussian_blur(image, radius)
        return (out,)

class Pil_UnsharpMask:
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
        out = op.pil_unsharp_mask(image, radius, percent, threshold)
        return (out,)

class Pil_Effects:
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
        out = op.pil_effects(image, effect)
        return (out,)

NODE_CLASS_MAPPINGS = {
    # "Pil_Color3DLUT": Pil_Color3DLUT,
    "Pil_BoxBlur": Pil_BoxBlur,
    "Pil_GaussianBlur": Pil_GaussianBlur,
    "Pil_UnsharpMask": Pil_UnsharpMask,
    "Pil_Effects": Pil_Effects,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # "Pil_Color3DLUT": "Pil Color3DLUT (MS) undeveloped",
    "Pil_BoxBlur": "Pil BoxBlur (MS)",
    "Pil_GaussianBlur": "Pil GaussianBlur (MS)",
    "Pil_UnsharpMask": "Pil UnsharpMask (MS)",
    "Pil_Effects": "Pil Effects (MS)",
}

