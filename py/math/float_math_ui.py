import os
from ...modules import comm_funcs
from . import float_math_op as OP


class FloatMath:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "A": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "B": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Operation": (["Add", "Subtract", "Multiply", "Dvivie"],),
                    }
                }
    RETURN_TYPES = ("FLOAT", )
    RETURN_NAMES = ("Float",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, A, B, Operation):
        out = OP.evaluate(A, B, Operation)
        return (out,)
    

NODE_CLASS_MAPPINGS = {
    "FloatMath": FloatMath,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "FloatMath": "Float Math",
}

