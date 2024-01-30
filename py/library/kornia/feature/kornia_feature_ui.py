import os
from .....modules import comm_funcs
from . import kornia_feature_op as op

# static variables
border_type = (["constant", "reflect", "replicate", "circular"], {"default": "reflect"})


class KorniaFeature_DogResponseSingle:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                    "image": ("IMAGE",),
                    "sigma1": ("FLOAT", {"default": 1, "min": 0.001, "max": 999}),
                    "sigma2": ("FLOAT", {"default": 2, "min": 0.001, "max": 999}),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, sigma1, sigma2):
        image_tensor = op.dog_response_single(image, sigma1, sigma2)
        return (image_tensor,)
    

# node class mapping
NODE_CLASS_MAPPINGS = {
    "KorniaFeature_DogResponseSingle": KorniaFeature_DogResponseSingle,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "KorniaFeature_DogResponseSingle": "Kornia DogResponseSingle (MS)",
}
