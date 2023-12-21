import os
import torch
from PIL import Image
from ....modules import folder_paths
from ....modules import image_funcs
from ....packages.ms_ZoeDepth.zoedepth.utils.misc import save_raw_16bit, colorize
from ....packages.ms_MiDaS.run_ms import midas_color_to_depth

depth_models_folder = r"%s\Depth" % folder_paths.folder_names_and_paths['models']
packages_folder = folder_paths.folder_names_and_paths['packages']
ms_ZoeDepth_path = r"%s\ms_ZoeDepth" % packages_folder
ms_MiDaS = r"%s\ms_MiDaS" % packages_folder

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

depth_models = dict()
depth_models['ZoeD_M12_N'] = None
depth_models['dpt_hybrid-midas'] = None
depth_models['dpt_large-midas'] = None
depth_models['midas_v21'] = None

def image_to_depth(depth_model, image, greyscale):
    out = image
    if 'ZoeD_M12_N' in depth_model:
        return run_zoedepth(depth_model, image, greyscale)

    else :
        input_path = (r"%s\input.png" % ms_MiDaS)
        image = image_funcs.tensor_to_pil(image)
        w, h = image.size
        image.save(input_path)
        output_path = midas_color_to_depth(input_path = input_path, 
                                           output_path =(r"%s\output.png" % ms_MiDaS), 
                                           model_path = (r"%s\%s" % (depth_models_folder, depth_model)), 
                                           model_type = os.path.splitext(depth_model)[0],
                                           optimize=False, 
                                           side=False,
                                           height=h,
                                           square=False, 
                                           grayscale=False)
        image = Image.open(output_path)
        image = image_funcs.pil_to_tensor(image)
        out = image

    return out


def run_zoedepth(depth_model, image, greyscale):
    out = None
    if depth_models['ZoeD_M12_N'] == None:
        model_path = r"%s\%s" % (depth_models_folder, depth_model)
        depth_models['ZoeD_M12_N'] = torch.hub.load(ms_ZoeDepth_path, "ZoeD_N", source="local", path = model_path, pretrained=True).to(DEVICE)
        # depth_models['ZoeD_M12_N'] = torch.hub.load(ms_ZoeDepth_path, "ZoeD_N", source="local", pretrained=True).to(DEVICE)
    image = image_funcs.tensor_to_pil(image)
    depth_zoe_n = depth_models['ZoeD_M12_N'].infer_pil(image)
    colored = colorize(depth_zoe_n)
    image = image_funcs.pil_to_tensor(colored)
    
    out = image
    return out

def ms_midas_depth_run(image, device, model_path, model_type="dpt_large_384", optimize=True, height=None, square=False):
    from ....packages.ms_MiDaS.midas.model_loader import load_model
    load_model(device, model_path, model_type, optimize, height, square)