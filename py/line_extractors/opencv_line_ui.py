import os
from ...modules import comm_funcs
from . import opencv_line_op as op


class OpenCV_CannyEdge:
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
        out = op.opencv2_canny(image, threshold1, threshold2, apertureSize, L2gradient)
        
        return (out,)


class OpenCV_Binary:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "threshold1": ("INT", {"default": 127, "min": 1, "max": 255, "step": 1}),
                "color1": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                "threshold2": ("INT", {"default": 127, "min": 1, "max": 255, "step": 1}),
                "color2": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                "mid_color": ("INT", {"default": 200, "min": 1, "max": 255, "step": 1,}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, threshold1, color1, threshold2, color2, mid_color):
        out = image
        out = op.opencv2_binary_line(image, threshold1, color1, threshold2, color2, mid_color)
        
        return (out,)

NODE_CLASS_MAPPINGS = {
    "OpenCV_CannyEdge": OpenCV_CannyEdge,
    "OpenCV_Binary": OpenCV_Binary,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenCV_CannyEdge": "OpenCV CannyEdge (MS)",
    "OpenCV_Binary": "OpenCV Binary (MS)",
    }