import os
from ...modules import comm_funcs
from . import openpose_op as op

class ControlNetAux_Openpose:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "hand_and_face": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, hand_and_face):
        tensor_image = op.controlnet_openpose(image, hand_and_face)
        
        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "ControlNetAux_Openpose": ControlNetAux_Openpose,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "ControlNetAux_Openpose": "ControlNet OpenPose (MS)",
    }