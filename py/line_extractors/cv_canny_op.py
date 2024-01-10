import cv2
from ...modules import image_funcs

def cv2_canny(tensor_image, threshold1, threshold2, apertureSize, L2gradient):
    cv2_image = image_funcs.tensor_to_cv2(tensor_image)
    cv2_gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(cv2_gray, threshold1, threshold2, apertureSize=apertureSize, L2gradient=L2gradient)
    tensor_image = image_funcs.cv2_to_tensor(canny_image)
    
    return tensor_image
