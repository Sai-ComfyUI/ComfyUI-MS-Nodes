import os
from .....modules import comm_funcs, folder_paths
from . import pillow_color_op as op

luts_folder = folder_paths.folder_names_and_paths['assets']
luts_files = comm_funcs.list_files_with_extensions(luts_folder, extensions=[".cube"])

class Pillow_LUTs:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required":
                {
                "image": ("IMAGE",),
                "luts_file" : (luts_files,),
                },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "run"
    CATEGORY = comm_funcs.category_from_file(os.path.abspath(__file__))

    def run(self, image, luts_file):
        image_tensor = op.pillow_apply_luts(image, luts_file)
        return (image_tensor,)


NODE_CLASS_MAPPINGS = {
    "Pillow_LUTs": Pillow_LUTs,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Pillow_LUTs": "Pillow LUTs (MS)",
}

