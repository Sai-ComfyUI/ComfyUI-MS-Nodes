import os
from ....modules import comm_funcs
from . import controlnet_normal_map_op as op

class ControlNetAux_NormalBae:
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
        tensor_image = op.controlnet_aux_normal_bae(image)
        
        return (tensor_image,)


NODE_CLASS_MAPPINGS = {
    "ControlNetAux_NormalBae": ControlNetAux_NormalBae,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ControlNetAux_NormalBae": "ControlNet Normal Bae (MS)",
    }