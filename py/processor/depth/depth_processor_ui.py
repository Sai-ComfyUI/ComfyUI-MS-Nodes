import os
from ....modules import comm_funcs
from . import depth_processor_op as op

depth_model_list = [
    "dpt_beit_base_384",
    "dpt_beit_large_384",
    "dpt_beit_large_512",
    "dpt_hybrid_384",
    "dpt_large_384",
    "dpt_levit_224",
    "midas_v21_384",
    "midas_v21_small_256",
    "ZoeD_M12_N",
]

unsupported_depth_model_list = [
    "dpt_next_vit_large_384",
    "dpt_swin_large_384", # force 384*384 only
    "dpt_swin2_base_384", # force 384*384 only
    "dpt_swin2_large_384", # force 384*384 only
    "dpt_swin2_tiny_256", # force 256*256 only
]

colorize_method_list = ['Spectral',
                        'terrain',
                        'viridis',
                        'plasma',
                        'inferno',
                        'magma',
                        'cividis',
                        'twilight',
                        'rainbow',
                        'gist_rainbow',
                        'gist_ncar',
                        'gist_earth',
                        'turbo',
                        'jet',
                        'afmhot',
                        'copper',
                        'seismic',
                        'hsv',
                        'brg',
]

class DepthModelLoader:
    @classmethod
    def INPUT_TYPES(s):
        # model_path = r"%s\Depth" % folder_paths.folder_names_and_paths['models']
        # model_path_list = comm_funcs.list_files_with_extensions(model_path, ".pt")
        # model_name_list = [model.split('\\')[-1] for model in model_path_list]    

        return {"required": 
                    { 
                    "depth_model": (depth_model_list, {"default": "ZoeD_M12_N"}),
                    }
                }
    RETURN_TYPES = ("Model_Depth", )
    RETURN_NAMES = ("Depth Model",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, depth_model):
        out = depth_model
        return (out,)
    

class ImageToDepthWithModel:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "depth_model": ("Model_Depth",),
                    "image": ("IMAGE",),
                }
                }
    RETURN_TYPES = ("IMAGE","IMAGE")
    RETURN_NAMES = ("colored_depth", "grayscale_depth")
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, depth_model, image):
        
        colored_depth, grayscale_depth = op.image_to_depth_with_model(depth_model, image)
        return (colored_depth, grayscale_depth,)


class ColorizeDepthmap:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "image": ("IMAGE", ),
                    "colorize_method": (colorize_method_list, {"default": 'Spectral'}),
                    "depth_min": ("FLOAT", {"default": 0, "min": 0, "max": 2, "step": 0.01}),
                    "depth_max": ("FLOAT", {"default": 1, "min": 0, "max": 2, "step": 0.01}),
                    "depth_mid_point": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.01}),
                },

                }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("colored depth",)
    FUNCTION = "run"

    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, colorize_method, depth_min, depth_max, depth_mid_point):
        
        out = op.colorize_depth(image, colorize_method, depth_min, depth_max, depth_mid_point)
        return (out,)


class MarigoldDepthEstimation:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {
                    "image": ("IMAGE", ),
                    "ensemble_size": ("INT", {"default": 10, "min": 1, "max": 4096, "step": 1}),
                    "denoising_steps": ("INT", {"default": 10, "min": 1, "max": 4096, "step": 1}),
                    "half_precision": ("BOOLEAN", {"default": False}),
                    "processing_res": ("INT", {"default": 768, "min": 0, "max": 4096, "step": 1}),
                    "output_processing_res": ("BOOLEAN", {"default": False}),
                    "seed": ("INT", {"default": 123, "min": 0, "max": 0xffffffffffffffff, "step": 1}),
                    "batch_size": ("INT", {"default": 0, "min": 0, "max": 4096, "step": 1}),
                    "color_map": (colorize_method_list, {"default": 'Spectral'}),
                    "apple_silicon": ("BOOLEAN", {"default": False}),
                },

                }

    RETURN_TYPES = ("IMAGE","IMAGE")
    RETURN_NAMES = ("colored_depth", "grayscale_depth")
    FUNCTION = "run"

    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, ensemble_size, denoising_steps, half_precision, processing_res, output_processing_res, seed, batch_size, color_map, apple_silicon):
        
        colored_depth, grayscale_depth = op.resolve_marigold_depth(image, ensemble_size, denoising_steps, half_precision,processing_res, output_processing_res, seed, batch_size, color_map, apple_silicon)
        
        return (colored_depth, grayscale_depth,)

NODE_CLASS_MAPPINGS = {
    "DepthModelLoader": DepthModelLoader,
    "ImageToDepthWithModel": ImageToDepthWithModel,
    "ColorizeDepthmap": ColorizeDepthmap,
    "MarigoldDepthEstimation": MarigoldDepthEstimation,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DepthModelLoader": "Load Depth Model (MS)",
    "ImageToDepthWithModel": "Image To Depth with Model (MS)",
    "ColorizeDepthmap": "Colorize Depth map (MS)",
    "MarigoldDepthEstimation": "Marigold Depth Estimation (MS)",
}

