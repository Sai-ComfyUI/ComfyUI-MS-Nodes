from ....modules import image_funcs
from ....modules import folder_paths
from ms_ai_pack import DWposeDetector

import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

models_folder = r"%s\ControlNet_Aux" % folder_paths.folder_names_and_paths['models']

det_config = r"%s\yolox_config\yolox_l_8xb8-300e_coco.py" % models_folder
det_ckpt = r"%s\yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth" % models_folder
pose_config = r"%s\dwpose_config\dwpose-l_384x288.py" % models_folder
pose_ckpt = r"%s\dw-ll_ucoco_384.pth" % models_folder



dwpose = DWposeDetector(det_config=det_config, det_ckpt=det_ckpt, pose_config=pose_config, pose_ckpt=pose_ckpt, device=device)
# dwpose = DWposeDetector(device=device,)

def controlnet_dwpose(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = dwpose(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

