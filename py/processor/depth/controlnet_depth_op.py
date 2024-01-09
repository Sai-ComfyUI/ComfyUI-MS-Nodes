from ....modules import image_funcs
from ....modules import folder_paths
from controlnet_aux import MidasDetector, ZoeDetector, LeresDetector

# import torch
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# dwpose = DWposeDetector(det_config=det_config, det_ckpt=det_ckpt, pose_config=pose_config, pose_ckpt=pose_ckpt, device=device)

models_folder = r"%s\ControlNet_Aux" % folder_paths.folder_names_and_paths['models']

midas = MidasDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
zoe = ZoeDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
leres = LeresDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)

def controlnet_aux_midas(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = midas(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_zoe(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = zoe(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_leres(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = leres(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image
