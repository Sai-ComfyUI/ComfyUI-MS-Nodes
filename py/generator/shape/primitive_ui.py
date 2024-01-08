import os
from ....modules import comm_funcs
from . import primitive_op as op

    
class PrimitivePolygon:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "resolution": ("INT", {"default": 256, "min": 64, "max": 8192, "step": 1,}),
                    "radius": ("INT", {"default": 64, "min": 12, "max": 8192, "step": 1,}),
                    "num_sides": ("INT", {"default": 3, "min": 3, "max": 120, "step": 1,}),
                    "rotation_angle": ("INT", {"default": 0, "min": 0, "max": 360, "step": 1,}),
                    "fill_r": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "fill_g": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "fill_b": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "bg_r": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    "bg_g": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    "bg_b": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    }
                }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("shape",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, resolution, radius, num_sides, rotation_angle, fill_r, fill_g, fill_b, bg_r, bg_g, bg_b):
        fill_color = (fill_r, fill_g, fill_b)
        bg_color = (bg_r, bg_g, bg_b)
        tensor_image = op.draw_centered_polygon(resolution, radius, num_sides, rotation_angle, fill_color, bg_color)
        return (tensor_image,)


class PrimitiveStar:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "resolution": ("INT", {"default": 256, "min": 64, "max": 8192, "step": 1,}),
                    "outer_radius": ("INT", {"default": 64, "min": 12, "max": 8192, "step": 1,}),
                    "inner_radius": ("INT", {"default": 6, "min": 1, "max": 8192, "step": 1,}),
                    "num_points": ("INT", {"default": 5, "min": 5, "max": 120, "step": 1,}),
                    "rotation_angle": ("INT", {"default": 0, "min": 0, "max": 360, "step": 1,}),
                    "fill_r": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "fill_g": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "fill_b": ("INT", {"default": 255, "min": 1, "max": 255, "step": 1,}),
                    "bg_r": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    "bg_g": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    "bg_b": ("INT", {"default": 1, "min": 1, "max": 255, "step": 1,}),
                    }
                }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("shape",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, resolution, outer_radius, inner_radius, num_points, rotation_angle, fill_r, fill_g, fill_b, bg_r, bg_g, bg_b):
        fill_color = (fill_r, fill_g, fill_b)
        bg_color = (bg_r, bg_g, bg_b)
        tensor_image = op.draw_centered_star(resolution, outer_radius, inner_radius, num_points, rotation_angle, fill_color, bg_color)
        return (tensor_image,)

NODE_CLASS_MAPPINGS = {
    "PrimitivePolygon": PrimitivePolygon,
    "PrimitiveStar": PrimitiveStar,
    
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PrimitivePolygon": "Polygon (MS)",
    "PrimitiveStar": "Star (MS)",
}

