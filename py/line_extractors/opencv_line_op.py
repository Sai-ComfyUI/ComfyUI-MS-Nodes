import cv2
from ...modules import image_funcs

def opencv2_canny(tensor_image, threshold1, threshold2, apertureSize, L2gradient):
    cv2_image = image_funcs.tensor_to_cv2(tensor_image)
    cv2_gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(cv2_gray, threshold1, threshold2, apertureSize=apertureSize, L2gradient=L2gradient)
    tensor_image = image_funcs.cv2_to_tensor(canny_image)
    
    return tensor_image

def opencv2_binary_line(tensor_image, threshold1, color1, threshold2, color2, mid_color):
    cv2_image = image_funcs.tensor_to_cv2(tensor_image)
    cv2_gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(cv2_gray, threshold1, color1, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(cv2_gray, threshold2, color2, cv2.THRESH_BINARY_INV)
    thresh = cv2.bitwise_and(thresh1, thresh2) * 255 + (255 - cv2.bitwise_or(thresh1, thresh2)) * mid_color
    tensor_image = image_funcs.cv2_to_tensor(thresh)
    
    return tensor_image