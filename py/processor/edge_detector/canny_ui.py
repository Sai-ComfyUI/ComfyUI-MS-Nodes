import os
from ....modules import comm_funcs
from ....modules import folder_paths


class CannyPreprocessor:
    @classmethod
    def INPUT_TYPES(s):
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
    FUNCTION = "execute"

    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, depth_model):
        out = depth_model
        return (out,)

NODE_CLASS_MAPPINGS = {
    "CannyEdgePreprocessor": CannyPreprocessor
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "CannyEdgePreprocessor": "Canny Edge"
}
