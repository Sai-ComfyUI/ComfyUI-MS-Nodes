import os
from ...modules import comm_funcs
from . import vector_math_op as OP

class VectorMath:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "X_A": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Y_A": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Z_A": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "X_B": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Y_B": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Z_B": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Operation": (["Add", "Subtract", "Multiply", "Dvivie"],),
                    }
                }
    RETURN_TYPES = ("VECTOR3", "STRING")
    RETURN_NAMES = ("Vect3","Vect3 as string")
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, X_A, Y_A, Z_A, X_B, Y_B, Z_B,Operation):
        out = OP.evaluate(X_A, Y_A, Z_A, X_B, Y_B, Z_B,Operation)
        return (out, str(out))
    

NODE_CLASS_MAPPINGS = {
    "VectorMath": VectorMath,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "VectorMath": "Vector Math",
    
}

