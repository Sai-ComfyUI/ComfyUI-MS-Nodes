import os
from ....modules import comm_funcs
from . import neural_style_transfer_op as op

class NeuralStyleTransfer:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "content_img": ("IMAGE",),
                "style_img": ("IMAGE",),
                "model": (["vgg16", "vgg19"], {"default": "vgg19"}),
                "optimizer": (["adam", "lbfgs"], {"default": "lbfgs"}),
                "num_steps":("INT", {"default": 1000, "min": 1, "max": 9999999999, "step": 1,}),
                "style_weight":("INT", {"default": 100000, "min": 1, "max": 9999999999, "step": 1,}),
                "content_weight":("INT", {"default": 30000, "min": 1, "max": 9999999999, "step": 1,}),
                "resolution":("INT", {"default": 512, "min": 64, "max": 2048, "step": 64,}),
                "device": (["cpu", "cuda"], {"default": "cpu"}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, content_img, style_img, model, optimizer, num_steps, style_weight, content_weight, resolution, device):
        tensor_image = op.neural_style_transfer(content_img, style_img, model, optimizer, num_steps, style_weight, content_weight, resolution, device)
        
        return (tensor_image,)
    

NODE_CLASS_MAPPINGS = {
    "NeuralStyleTransfer": NeuralStyleTransfer,
    }

NODE_DISPLAY_NAME_MAPPINGS = {
    "NeuralStyleTransfer": "NeuralStyleTransfer (MS)",
    }