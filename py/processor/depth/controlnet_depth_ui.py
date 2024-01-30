import os
from ....modules import comm_funcs
from . import controlnet_depth_op as op

class ControlNetAux_Midas:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image):
        tensor_image = op.controlnet_aux_midas(image)
        
        return (tensor_image,)
    
class ControlNetAux_Zoe:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image):
        tensor_image = op.controlnet_aux_zoe(image)
        
        return (tensor_image,)

class ControlNetAux_Zoe_DepthAnything:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "environment" : (["indoor", "outdoor"], {"default": "indoor"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, environment):
        tensor_image = op.controlnet_aux_zoe_depth_anything(image, environment)
        
        return (tensor_image,)


class ControlNetAux_Leres:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image):
        tensor_image = op.controlnet_aux_leres(image)
        
        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "ControlNetAux_Midas": ControlNetAux_Midas,
    "ControlNetAux_Zoe": ControlNetAux_Zoe,
    "ControlNetAux_Leres": ControlNetAux_Leres,
    "ControlNetAux_Zoe_DepthAnything": ControlNetAux_Zoe_DepthAnything,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ControlNetAux_Midas": "ControlNet Midas Depth (MS)",
    "ControlNetAux_Zoe": "ControlNet Zoe Depth (MS)",
    "ControlNetAux_Leres": "ControlNet Leres Depth (MS)",
    "ControlNetAux_Zoe_DepthAnything": "ControlNet Zoe DepthAnything (MS)",
    }