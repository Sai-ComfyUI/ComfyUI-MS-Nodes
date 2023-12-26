import os
from ....modules import comm_funcs
from . import cv_hough_op as op


class CV_HoughLinesP:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "threshold": ("INT", {"default": 100, "min": 1, "max": 99999, "step": 1}),
                "minLineLength": ("INT", {"default": 15, "min": 0, "max": 99999, "step": 1}),
                "maxLineGap": ("INT", {"default": 30, "min": 0, "max": 99999, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, threshold, minLineLength, maxLineGap):
        out = image
        out = op.cv2_hough_lines_p(image, threshold, minLineLength, maxLineGap)
        
        return (out,)



class CV_HoughCircles:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "method": (['cv2.HOUGH_GRADIENT'],),
                "dp": ("INT", {"default": 1, "min": 1, "max": 10, "step": 1}),
                "minDist": ("INT", {"default": 100, "min": 1, "max": 99999, "step": 1}),
                "param1": ("INT", {"default": 15, "min": 0, "max": 99999, "step": 1}),
                "param2": ("INT", {"default": 30, "min": 0, "max": 99999, "step": 1}),
                "minRadius": ("INT", {"default": 10, "min": 0, "max": 99999, "step": 1}),
                "maxRadius": ("INT", {"default": 50, "min": 0, "max": 99999, "step": 1}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, method, dp, minDist, param1, param2, minRadius, maxRadius):
        out = image
        out = op.cv2_hough_circles(image, method, dp, minDist, param1, param2, minRadius, maxRadius)
        
        return (out,)




NODE_CLASS_MAPPINGS = {
                        "CV_HoughCircles": CV_HoughCircles,
                        "CV_HoughLinesP": CV_HoughLinesP,
                       }
NODE_DISPLAY_NAME_MAPPINGS = {
                                "CV_HoughCircles": "CV Hough Circles (MS)",
                                "CV_HoughLinesP": "CV Hough Lines P (MS)",
                              }