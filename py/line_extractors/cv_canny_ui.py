import os
from ...modules import comm_funcs
from . import cv_canny_op as op


class CV_CannyEdge:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "threshold1": ("INT", {"default": 1, "min": 0, "max": 99999, "step": 1}),
                "threshold2": ("INT", {"default": 100, "min": 0, "max": 99999, "step": 1}),
                "apertureSize": ([3, 5, 7],),
                "L2gradient": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, threshold1, threshold2, apertureSize, L2gradient):
        out = image
        out = op.cv2_canny(image, threshold1, threshold2, apertureSize, L2gradient)
        
        return (out,)



NODE_CLASS_MAPPINGS = {"CV_CannyEdge": CV_CannyEdge}
NODE_DISPLAY_NAME_MAPPINGS = {"CV_CannyEdge": "CV Canny Edge (MS)"}