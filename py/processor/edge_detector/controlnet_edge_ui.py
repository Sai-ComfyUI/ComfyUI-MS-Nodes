import os
from ....modules import comm_funcs
from . import controlnet_edge_op as op

class ControlNetAux_Hed:
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
        tensor_image = op.controlnet_aux_hed(image)
        
        return (tensor_image,)


class ControlNetAux_Mlsd:
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
        tensor_image = op.controlnet_aux_mlsd(image)
        
        return (tensor_image,)
    
class ControlNetAux_Pidi:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "safe": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, safe):
        tensor_image = op.controlnet_aux_pidi(image, safe)
        
        return (tensor_image,)

class ControlNetAux_Lineart:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "coarse": ("BOOLEAN", {"default": True}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, coarse):
        tensor_image = op.controlnet_aux_lineart(image, coarse)
        
        return (tensor_image,)

class ControlNetAux_Lineart_Anime:
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
        tensor_image = op.controlnet_aux_lineart_anime(image)
        
        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "ControlNetAux_Hed": ControlNetAux_Hed,
    "ControlNetAux_Mlsd": ControlNetAux_Mlsd,
    "ControlNetAux_Pidi": ControlNetAux_Pidi,
    "ControlNetAux_Lineart": ControlNetAux_Lineart,
    "ControlNetAux_Lineart_Anime": ControlNetAux_Lineart_Anime,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ControlNetAux_Hed": "ControlNet Hed Edge (MS)",
    "ControlNetAux_Mlsd": "ControlNet Mlsd Edge (MS)",
    "ControlNetAux_Pidi": "ControlNet Pidi Edge (MS)",
    "ControlNetAux_Lineart": "ControlNet Lineart (MS)",
    "ControlNetAux_Lineart_Anime": "ControlNet Lineart Anime(MS)",
    }