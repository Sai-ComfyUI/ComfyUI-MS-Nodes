import os
import numpy as np
from ...modules import comm_funcs

    
class MS_Boolean:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "Value": ("BOOLEAN", {"default": False}),
                    }
                }
    RETURN_TYPES = ("BOOLEAN", )
    RETURN_NAMES = ("Boolean",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, Value):
        out = Value
        return (out,)
    
class MS_Float:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "Value": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    }
                }
    RETURN_TYPES = ("FLOAT", )
    RETURN_NAMES = ("Float",)
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, Value):
        out = Value
        return (out,)

class MS_NP_Vector3:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    { 
                    "X": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Y": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    "Z": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999999999.0, "step": 0.01, "round": 0.001,}),
                    }
                }
    RETURN_TYPES = ("VECTOR3", "STRING")
    RETURN_NAMES = ("Vect3","Vect3 as string")
    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, X, Y, Z):
        out = np.array([ X, Y, Z])
        return (out, str(out))

NODE_CLASS_MAPPINGS = {
    "MS_Boolean": MS_Boolean,
    "MS_Float": MS_Float,
    "MS_NP_Vector3": MS_NP_Vector3,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "MS_Boolean": "Boolean",
    "MS_Float": "Float",
    "MS_NP_Vector3": "Vector3",
}

