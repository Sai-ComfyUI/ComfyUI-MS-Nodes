import os
from ....modules import comm_funcs
from ....modules import folder_paths
from . import depth_processor_op as op

    
class DepthModelLoader:
    @classmethod
    def INPUT_TYPES(s):
        model_path = r"%s\Depth" % folder_paths.folder_names_and_paths['models']
        model_path_list = comm_funcs.list_files_with_extensions(model_path, ".pt")
        model_name_list = [model.split('\\')[-1] for model in model_path_list]        
        return {"required": 
                    { 
                    "depth_model": (model_name_list,),
                    }
                }
    RETURN_TYPES = ("Model_Depth", )
    RETURN_NAMES = ("Depth Model",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, depth_model):
        out = depth_model
        return (out,)
    
class ImageToDepthProcesser:
    @classmethod
    def INPUT_TYPES(s):

        return {"required": 
                    { 
                    "depth_model": ("Model_Depth",),
                    "image": ("IMAGE",),
                    "greyscale": ("BOOLEAN", {"default": False}),
                    }
                }
    RETURN_TYPES = ("IMAGE", )
    RETURN_NAMES = ("Depth Image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, depth_model, image, greyscale):
        out = op.image_to_depth(depth_model, image, greyscale)
        return (out,)


NODE_CLASS_MAPPINGS = {
    "DepthModelLoader": DepthModelLoader,
    "ImageToDepthProcesser": ImageToDepthProcesser,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "DepthModelLoader": "Load Depth Model (MS)",
    "ImageToDepthProcesser": "Image To Depth with Model (MS)",
}

