import cv2
import numpy as np
from ....modules import image_funcs

def cv2_hough_circles(tensor_image, method, dp, minDist, param1, param2, minRadius, maxRadius):
    cv2_image = image_funcs.tensor_to_cv2(tensor_image)
    cv2_gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(cv2_gray,
                                  method=cv2.HOUGH_GRADIENT,
                                  dp=dp,
                                  minDist=minDist,
                                  param1=param1,
                                  param2=param2,
                                  minRadius=minRadius,
                                  maxRadius=maxRadius,
                                  )
    if circles is not None:
        circles = np.uint16(np.around(circles))

        # 繪製檢測到的圓
        for i in circles[0, :]:
            # 繪製外圈
            cv2.circle(cv2_image, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # 繪製圓心
            cv2.circle(cv2_image, (i[0], i[1]), 2, (0, 0, 255), 3)
            
    tensor_image = image_funcs.cv2_to_tensor(cv2_image)
    
    return tensor_image

def cv2_hough_lines_p(tensor_image, threshold, minLineLength, maxLineGap):
    cv2_image = image_funcs.tensor_to_cv2(tensor_image)
    cv2_gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
    lines = cv2.HoughLinesP(cv2_gray,
                            rho=1, 
                            theta=np.pi/180,
                            threshold=threshold,
                            minLineLength=minLineLength,
                            maxLineGap=maxLineGap,
                            )
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(cv2_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
    tensor_image = image_funcs.cv2_to_tensor(cv2_image)
    
    return tensor_image