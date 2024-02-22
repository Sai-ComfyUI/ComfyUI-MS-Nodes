import colortrans
import numpy as np
import cv2
from PIL import Image
from color_matcher import ColorMatcher
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

def color_matcher(image, ref, method):
    pil_image = image_funcs.tensor_to_pil(image)
    pil_image = np.array(pil_image.convert('RGB'))
    pil_ref = image_funcs.tensor_to_pil(ref)
    pil_ref = np.array(pil_ref.convert('RGB'))
    
    colormatcher = ColorMatcher()
    image_result = colormatcher.transfer(src=pil_image, ref=pil_ref, method=method)
    tensor_image = image_funcs.pil_to_tensor(image_result)
    
    return tensor_image

# Color-Transfer-between-Images
def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2))
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

def color_transfer_between_images(image, ref):
    cv2_image = image_funcs.tensor_to_cv2(image)
    cv2_image = cv2.cvtColor(cv2_image,cv2.COLOR_BGR2LAB)
    cv2_ref = image_funcs.tensor_to_cv2(ref)
    cv2_ref = cv2.cvtColor(cv2_ref,cv2.COLOR_BGR2LAB)
    
    s_mean, s_std = get_mean_and_std(cv2_image)
    t_mean, t_std = get_mean_and_std(cv2_ref)
    
    height, width, channel = cv2_image.shape
    for i in range(0,height):
        for j in range(0,width):
            for k in range(0,channel):
                x = cv2_image[i,j,k]
                x = ((x-s_mean[k])*(t_std[k]/s_std[k]))+t_mean[k]
                # round or +0.5
                x = round(x)
                # boundary check
                x = 0 if x<0 else x
                x = 255 if x>255 else x
                cv2_image[i,j,k] = x

    cv2_image = cv2.cvtColor(cv2_image,cv2.COLOR_LAB2BGR)

    tensor_image = image_funcs.cv2_to_tensor(cv2_image)
    
    return tensor_image