import os
from .. import comm_funcs

class MS_GenerateSeed:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "seed": ("INT", {"default": 0, "min": -1125899906842624, "max": 1125899906842624}),
                },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("SEED",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, seed=0):
        """Returns the passed seed on execution."""
        return (seed,)
    

NODE_CLASS_MAPPINGS = {
    "MS_GenerateSeed": MS_GenerateSeed,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "MS_GenerateSeed": "Seed (MS)",
}

