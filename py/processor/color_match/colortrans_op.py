import colortrans
import numpy as np
from PIL import Image
from ....modules import image_funcs

def color_trans(image, ref, method):    
    pil_image = image_funcs.tensor_to_pil(image)
    pil_image = np.array(pil_image.convert('RGB'))
    pil_ref = image_funcs.tensor_to_pil(ref)
    pil_ref = np.array(pil_ref.convert('RGB'))
    
    if method == "lhm":
        output = colortrans.transfer_lhm(pil_image, pil_ref)
    elif method == "pccm":
        output = colortrans.transfer_pccm(pil_image, pil_ref)
    elif method == "reinhard":
        output = colortrans.transfer_reinhard(pil_image, pil_ref)
        
    pil_output = Image.fromarray(output)
    tensor_image = image_funcs.pil_to_tensor(pil_output)
    
    return tensor_image
    