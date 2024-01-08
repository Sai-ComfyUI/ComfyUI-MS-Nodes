from PIL import Image, ImageDraw
import math
from ....modules import image_funcs

def draw_centered_polygon(resolution, radius, num_sides, rotation_angle, fill_color, bg_color):
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

    # 將多邊形頂點旋轉
    rotated_polygon = rotate_polygon(polygon_points, center[0], center[1], math.radians(rotation_angle))
    
    # 繪製多邊形
    draw.polygon(rotated_polygon, fill=fill_color)
    
    tensor_image = image_funcs.pil_to_tensor(pil_image)
    
    return tensor_image


def draw_centered_star(resolution, outer_radius, inner_radius, num_points, rotation_angle, fill_color, bg_color):
    # 創建一個有背景色的 PIL 圖片對象
    pil_image = Image.new("RGB", (resolution, resolution), bg_color)
    draw = ImageDraw.Draw(pil_image)

    # 中心點
    center = (resolution // 2, resolution // 2)

    # 計算星星的頂點
    theta = 2 * math.pi / (2 * num_points)  # 注意這裡是 2*num_points
    star_points = [
        (center[0] + int(outer_radius * math.cos(theta * i)),
         center[1] + int(outer_radius * math.sin(theta * i)))
        if i % 2 == 0
        else (center[0] + int(inner_radius * math.cos(theta * i)),
              center[1] + int(inner_radius * math.sin(theta * i)))
        for i in range(2 * num_points)
    ]

    # 將星星頂點旋轉
    rotated_star = rotate_polygon(star_points, center[0], center[1], math.radians(rotation_angle))

    # 繪製星星
    draw.polygon(rotated_star, fill=fill_color)

    tensor_image = image_funcs.pil_to_tensor(pil_image)
    
    return tensor_image


def rotate_polygon(polygon, cx, cy, angle):
    # 將多邊形頂點旋轉指定角度
    rotated_polygon = []
    for x, y in polygon:
        x -= cx
        y -= cy
        new_x = int(x * math.cos(angle) - y * math.sin(angle) + cx)
        new_y = int(x * math.sin(angle) + y * math.cos(angle) + cy)
        rotated_polygon.append((new_x, new_y))
    return rotated_polygon