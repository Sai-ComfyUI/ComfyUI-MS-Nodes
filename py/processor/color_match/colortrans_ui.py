import os
from ....modules import comm_funcs
from . import colortrans_op as op

class ColorTrans:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "ref": ("IMAGE",),
                "method": (["lhm", "pccm", "reinhard"], {"default": "lhm"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, ref, method):
        tensor_image = op.color_trans(image, ref, method)
        
        return (tensor_image,)

class ColorMatcher:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "ref": ("IMAGE",),
                "method": (['mkl','hm', 'reinhard', 'mvgd', 'hm-mvgd-hm', 'hm-mkl-hm',], {"default": "mkl"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, ref, method):
        tensor_image = op.color_matcher(image, ref, method)
        
        return (tensor_image,)


NODE_CLASS_MAPPINGS = {
    "ColorTrans": ColorTrans,
    "ColorMatcher": ColorMatcher,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ColorTrans": "Color Trans (MS)",
    "ColorMatcher": "Color Matcher (MS)",
    }