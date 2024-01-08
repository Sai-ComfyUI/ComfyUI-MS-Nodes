import os
from ....modules import comm_funcs
from . import color_channel_op as op

    
class SeparateRGB:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "image": ("IMAGE",),
                    }
                }
    RETURN_TYPES = ("IMAGE", "IMAGE", "IMAGE")
    RETURN_NAMES = ("R", "G", "B",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image):
        r_channel, g_channel, b_channel = op.separate_rgb(image)
        return (r_channel, g_channel, b_channel,)

class CombineRGB:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "r": ("IMAGE",),
                    "g": ("IMAGE",),
                    "b": ("IMAGE",),
                    }
                }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, r, g, b):
        image = op.combine_rgb(r, g, b)
        return (image,)    
    
NODE_CLASS_MAPPINGS = {
    "SeparateRGB": SeparateRGB,
    "CombineRGB": CombineRGB,
    
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "SeparateRGB": "Separate RGB (MS)",
    "CombineRGB": "Combine RGB (MS)",
}

