import os
from .....modules import comm_funcs
from . import kornia_filters_op as op

# static variables
border_type = (["constant", "reflect", "replicate", "circular"], {"default": "reflect"})

# blur
class KorniaFilter_BilateralBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "kernel_size": ("INT", {"default": 3, "min": 1, "max": 9}),
                    "sigma_color": ("FLOAT", {"default": 1, "min": 0.001, "max": 999}),
                    "sigma_space": ("FLOAT", {"default": 1, "min": 0.001, "max": 999}),
                    "border_type": border_type,
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, kernel_size, sigma_color, sigma_space, border_type):
        image_tensor = op.bilateral_blur(
            image, kernel_size, sigma_color, sigma_space, border_type)
        return (image_tensor,)


class KorniaFilter_BoxBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "kernel_size": ("INT", {"default": 3, "min": 1, "max": 999}),
                    "border_type": border_type,
                    "separable": ("BOOLEAN", {"default": False})
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, kernel_size, border_type, separable):
        image_tensor = op.box_blur(image, kernel_size, border_type, separable)
        return (image_tensor,)


class KorniaFilter_GaussianBlur:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "kernel_size": ("INT", {"default": 3, "min": 1, "max": 15}),
                    "sigma": ("FLOAT", {"default": 1, "min": 0.001, "max": 999}),
                    "border_type": border_type,
                    "separable": ("BOOLEAN", {"default": True})
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, kernel_size, sigma, border_type, separable):
        image_tensor = op.gaussian_blur2d(image, kernel_size, sigma, border_type, separable)
        return (image_tensor,)

# edge detect
class KorniaFilter_Canny:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "low_threshold": ("FLOAT", {"default": 0.1, "min": 0.001, "max": 0.999}),
                    "high_threshold": ("FLOAT", {"default": 0.2, "min": 0.001, "max": 0.999}),
                    "kernel_size": ("INT", {"default": 3, "min": 1, "max": 9}),
                    "sigma": ("FLOAT", {"default": 1, "min": 0.001, "max": 9.000}),
                    "hysteresis": ("BOOLEAN", {"default": True})
                },
        }

    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("edge_magnitudes", "edge_detection")
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, low_threshold, high_threshold, kernel_size, sigma, hysteresis):
        edge_magnitudes, edge_detection = op.canny(
            image, low_threshold, high_threshold, kernel_size, sigma, hysteresis)
        return (edge_magnitudes, edge_detection,)


class KorniaFilter_Laplacian:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "kernel_size": ("INT", {"default": 3, "min": 1, "max": 999}),
                    "border_type": border_type,
                    "normalized": ("BOOLEAN", {"default": True})
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, kernel_size, border_type, normalized):
        image_tensor = op.laplacian(
            image, kernel_size, border_type, normalized)
        return (image_tensor,)


class KorniaFilter_Sobel:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "normalized": ("BOOLEAN", {"default": True})
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, normalized):
        image_tensor = op.sobel(image, normalized)
        return (image_tensor,)


# node class mapping
NODE_CLASS_MAPPINGS = {
    "KorniaFilter_BilateralBlur": KorniaFilter_BilateralBlur,
    "KorniaFilter_BoxBlur": KorniaFilter_BoxBlur,
    "KorniaFilter_GaussianBlur": KorniaFilter_GaussianBlur,
    "KorniaFilter_Canny": KorniaFilter_Canny,
    "KorniaFilter_Laplacian": KorniaFilter_Laplacian,
    "KorniaFilter_Sobel": KorniaFilter_Sobel,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "KorniaFilter_BilateralBlur": "Kornia BilateralBlur (MS)",
    "KorniaFilter_BoxBlur": "Kornia BoxBlur (MS)",
    "KorniaFilter_GaussianBlur": "Kornia GaussianBlur (MS)",
    "KorniaFilter_Canny": "Kornia Canny (MS)",
    "KorniaFilter_Laplacian": "Kornia Laplacian (MS)",
    "KorniaFilter_Sobel": "Kornia Sobel (MS)",
}
