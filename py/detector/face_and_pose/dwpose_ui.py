import os
from ....modules import comm_funcs
from . import dwpose_op as op

class ControlNetAux_DWPose:
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
        tensor_image = op.controlnet_dwpose(image)
        
        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "ControlNetAux_DWPose": ControlNetAux_DWPose,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ControlNetAux_DWPose": "ControlNet DWPose (MS)",
    }