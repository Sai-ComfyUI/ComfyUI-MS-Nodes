from ....modules import image_funcs
from ....modules import folder_paths
from controlnet_aux import OpenposeDetector

models_folder = r"%s\ControlNet_Aux" % folder_paths.folder_names_and_paths['models']

open_pose = OpenposeDetector.from_pretrained("lllyasviel/Annotators", cache_dir=models_folder)

def controlnet_openpose(tensor_image, hand_and_face):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = open_pose(pil_image, hand_and_face=hand_and_face)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

