from PIL import Image, ImageDraw
import math
from ....modules import image_funcs

def draw_centered_polygon(resolution, radius, num_sides, fill_color, bg_color):
    # 創建一個有背景色的 PIL 圖片對象
    pil_image = Image.new("RGB", (resolution, resolution), bg_color)
    draw = ImageDraw.Draw(pil_image)

    # 中心點
    center = (resolution // 2, resolution // 2)

    # 計算多邊形的頂點
    theta = 2 * math.pi / num_sides
    polygon_points = [
        (center[0] + int(radius * math.cos(theta * i)),
         center[1] + int(radius * math.sin(theta * i)))
        for i in range(num_sides)
    ]

    # 繪製多邊形
    draw.polygon(polygon_points, fill=fill_color)
    
    tensor_image = image_funcs.pil_to_tensor(pil_image)
    
    return tensor_image