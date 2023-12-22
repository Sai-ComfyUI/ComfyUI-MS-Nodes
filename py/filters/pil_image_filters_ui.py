import os
from ...modules import comm_funcs
# from .pil_image_filters_op

class Pli_Color3DLUT:
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
    
class Pli_BoxBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "lock_ratio": ("BOOLEAN", {"default": False}),
                "radius_x": ("FLOAT", {"default": 1, "min": 0, "max": 100}),
                "radius_y": ("FLOAT", {"default": 1, "min": 0, "max": 100}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output_image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, lock_ratio, radius_x, radius_y):
        print (type(image))
        out = image
        """Returns the passed seed on execution."""
        return (out,)


NODE_CLASS_MAPPINGS = {
    # "Pli_Color3DLUT": Pli_Color3DLUT,
    "Pli_BoxBlur": Pli_BoxBlur,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    # "Pli_Color3DLUT": "Pli Color3DLUT (MS) undeveloped",
    "Pli_BoxBlur": "Pli BoxBlur",
}

