from ...modules import image_funcs
from ...modules import folder_paths
from controlnet_aux import HEDdetector, MLSDdetector, PidiNetDetector, LineartDetector, LineartAnimeDetector

# import torch
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# dwpose = DWposeDetector(det_config=det_config, det_ckpt=det_ckpt, pose_config=pose_config, pose_ckpt=pose_ckpt, device=device)

models_folder = r"%s\ControlNet_Aux" % folder_paths.folder_names_and_paths['models']

hed = HEDdetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
mlsd = MLSDdetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
pidi = PidiNetDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
# normal_bae = NormalBaeDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
lineart = LineartDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
lineart_anime = LineartAnimeDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)
# sam = SamDetector.from_pretrained("ybelkada/segment-anything", subfolder="checkpoints", cache_dir=models_folder)
# mobile_sam = SamDetector.from_pretrained("dhkim2810/MobileSAM", model_type="vit_t", filename="mobile_sam.pt", cache_dir=models_folder)

def controlnet_aux_hed(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = hed(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_mlsd(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = mlsd(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_pidi(tensor_image, safe):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = pidi(pil_image, safe=safe)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_lineart(tensor_image, coarse):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = lineart(pil_image, coarse=coarse)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

def controlnet_aux_lineart_anime(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = lineart(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image
