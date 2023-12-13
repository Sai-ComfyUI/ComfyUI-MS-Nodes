import os
from ... import comm_funcs
from . import fractal_noise_op as OP

# PERLIN POWER FRACTAL NOISE LATENT

class PowerFractalNoiseNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "batch_size": ("INT", {"default": 1, "max": 64, "min": 1, "step": 1}),
                "width": ("INT", {"default": 512, "max": 8192, "min": 64, "step": 1}),
                "height": ("INT", {"default": 512, "max": 8192, "min": 64, "step": 1}),
                "resampling": (["nearest-exact", "bilinear", "area", "bicubic", "bislerp"],),
                "X": ("FLOAT", {"default": 0, "max": 99999999, "min": -99999999, "step": 0.01}),
                "Y": ("FLOAT", {"default": 0, "max": 99999999, "min": -99999999, "step": 0.01}),
                "Z": ("FLOAT", {"default": 0, "max": 99999999, "min": -99999999, "step": 0.01}),
                "evolution": ("FLOAT", {"default": 0.0, "max": 1.0, "min": 0.0, "step": 0.01}),
                "frame": ("INT", {"default": 0, "max": 99999999, "min": 0, "step": 1}),
                "scale": ("FLOAT", {"default": 5, "max": 2048, "min": 2, "step": 0.01}),
                "octaves": ("INT", {"default": 8, "max": 8, "min": 1, "step": 1}),
                "persistence": ("FLOAT", {"default": 1.5, "max": 23.0, "min": 0.01, "step": 0.01}),
                "lacunarity": ("FLOAT", {"default": 2.0, "max": 99.0, "min": 0.01, "step": 0.01}),
                "exponent": ("FLOAT", {"default": 4.0, "max": 38.0, "min": 0.01, "step": 0.01}),
                "brightness": ("FLOAT", {"default": 0.0, "max": 1.0, "min": -1.0, "step": 0.01}),
                "contrast": ("FLOAT", {"default": 0.0, "max": 1.0, "min": -1.0, "step": 0.01}),
                "clamp_min": ("FLOAT", {"default": 0.0, "max": 10.0, "min": -10.0, "step": 0.01}),
                "clamp_max": ("FLOAT", {"default": 1.0, "max": 10.0, "min": -10.0, "step": 0.01}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}), 
                "device": (["cpu", "cuda"],),
            },
            "optional": {
                "optional_vae": ("VAE",),
            }
        }

    RETURN_TYPES = ("LATENT","IMAGE")
    RETURN_NAMES = ("latents","previews")
    FUNCTION = "run"

    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))
    
    def run(self, batch_size, width, height, resampling, X, Y, Z, evolution, frame, scale, octaves, persistence, lacunarity, exponent, brightness, contrast, clamp_min, clamp_max, seed, device, optional_vae=None):
        LATENT ,IMAGE = OP.power_fractal_latent(batch_size, width, height, resampling, X, Y, Z, evolution, frame, scale, octaves, persistence, lacunarity, exponent, brightness, contrast, clamp_min, clamp_max, seed, device, optional_vae=None)
        return (LATENT, IMAGE)
    

class PowerFractalCrossHatchNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "batch_size": ("INT", {"default": 1, "max": 64, "min": 1, "step": 1}),
                "width": ("INT", {"default": 512, "max": 8192, "min": 64, "step": 1}),
                "height": ("INT", {"default": 512, "max": 8192, "min": 64, "step": 1}),
                "resampling": (["nearest-exact", "bilinear", "area", "bicubic", "bislerp"],),
                "frequency": ("FLOAT", {"default": 320.0, "max": 1024.0, "min": 0.001, "step": 0.001}),
                "octaves": ("INT", {"default": 12, "max": 32, "min": 1, "step": 1}),
                "persistence": ("FLOAT", {"default": 1.5, "max": 2.0, "min": 0.001, "step": 0.001}),
                "num_colors": ("INT", {"default": 16, "max": 256, "min": 2, "step": 1}),
                "color_tolerance": ("FLOAT", {"default": 0.05, "max": 1.0, "min": 0.001, "step": 0.001}),
                "angle_degrees": ("FLOAT", {"default": 45.0, "max": 360.0, "min": 0.0, "step": 0.01}),
                "brightness": ("FLOAT", {"default": 0.0, "max": 1.0, "min": -1.0, "step": 0.001}),
                "contrast": ("FLOAT", {"default": 0.0, "max": 1.0, "min": -1.0, "step": 0.001}),
                "blur": ("FLOAT", {"default": 2.5, "max": 1024, "min": 0, "step": 0.01}),
                "clamp_min": ("FLOAT", {"default": 0.0, "max": 10.0, "min": -10.0, "step": 0.01}),
                "clamp_max": ("FLOAT", {"default": 1.0, "max": 10.0, "min": -10.0, "step": 0.01}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}), 
                "device": (["cpu", "cuda"],),
            },
            "optional": {
                "optional_vae": ("VAE",),
            }
        }

    RETURN_TYPES = ("LATENT","IMAGE")
    RETURN_NAMES = ("latents","previews")
    FUNCTION = "run"
    
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))
    
    def run(self, batch_size, width, height, resampling, frequency, octaves, persistence, color_tolerance, num_colors, angle_degrees, brightness, contrast, blur, clamp_min, clamp_max, seed, device, optional_vae=None):
        
        LATENT ,IMAGE = OP.cross_hatch(batch_size, width, height, resampling, frequency, octaves, persistence, color_tolerance, num_colors, angle_degrees, brightness, contrast, blur, clamp_min, clamp_max, seed, device, optional_vae=None)
        
        return (LATENT, IMAGE)

NODE_CLASS_MAPPINGS = {
    "PowerFractalNoiseNode": PowerFractalNoiseNode,
    "PowerFractalCrossHatchNode": PowerFractalCrossHatchNode,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PowerFractalNoiseNode": "Power Fractal Noise",
    "PowerFractalCrossHatchNode": "Power Fractal Cross Hatch",
}

