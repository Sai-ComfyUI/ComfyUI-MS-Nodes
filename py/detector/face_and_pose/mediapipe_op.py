from ....modules import image_funcs
from ....modules import folder_paths
from ms_ai_pack import MediapipeFaceDetector

models_folder = r"%s\ControlNet_Aux" % folder_paths.folder_names_and_paths['models']

face_detector = MediapipeFaceDetector()

def controlnet_mediapipe_face(tensor_image):
    pil_image = image_funcs.tensor_to_pil(tensor_image)
    processed_image = face_detector(pil_image)
    tensor_image = image_funcs.pil_to_tensor(processed_image)
    return tensor_image

