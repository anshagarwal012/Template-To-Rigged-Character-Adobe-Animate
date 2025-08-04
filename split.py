import re
from PIL import Image
import os

def safe_filename(name):
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)

# These coordinates were designed on a 2048x2048 reference image
reference_size = (2048, 2048)

part_positions = {
    "right_hand_palm_holding_prop__2": [5, 9, 590, 532],
    "Body": [616, 7, 611, 918],
    "mouth_shape_1": [5, 555, 227, 173],
    "mouth_shape_2": [5, 747, 234, 173],
    "mouth_shape_3": [10, 932, 225, 178],
    "mouth_shape_4": [7, 1122, 227, 176],
    "right_hand_palm_holding_prop__1": [239, 557, 365, 618],
    "head_eyes_closed": [5, 1324, 438, 354],
    "head_eyes_opened": [5, 1687, 433, 354],
    "arm_right": [464, 1197, 340, 419],
    "arm_left": [825, 1193, 335, 422],
    "hand_right": [455, 1628, 328, 407],
    "hand_left": [792, 1626, 333, 415],
    "right_palm_3": [1250, 10, 442, 376],
    "right_palm_2": [1245, 406, 444, 379],
    "right_palm_1": [1248, 803, 442, 376],
    "thigh_right": [1704, 10, 336, 366],
    "leg_lower_right": [1704, 390, 336, 417],
    "thigh_left": [1699, 809, 339, 374],
    "left_palm_3": [1180, 1196, 452, 422],
    "leg_lower_left": [1694, 1193, 351, 417],
    "left_palm_2": [1137, 1625, 447, 414],
    "left_palm_1": [1584, 1620, 454, 424],
    "eye_background": [619, 940, 294, 241],
    "eye_balls": [925, 938, 296, 241],
}

def slice_character(image_path, output_folder, target_size=(2048, 2048)):
    os.makedirs(output_folder, exist_ok=True)
    img = Image.open(image_path).convert("RGBA")

    # Resize if needed
    if img.size != target_size:
        img = img.resize(target_size, Image.Resampling.LANCZOS)

    # Scale based on known reference size, not the image's actual size
    scale_x = target_size[0] / reference_size[0]
    scale_y = target_size[1] / reference_size[1]

    exported_names = []

    for part_name, (x, y, w, h) in part_positions.items():
        clean_name = safe_filename(part_name)

        sx = int(x * scale_x)
        sy = int(y * scale_y)
        sw = int(w * scale_x)
        sh = int(h * scale_y)

        x1 = max(0, min(target_size[0], sx))
        y1 = max(0, min(target_size[1], sy))
        x2 = max(0, min(target_size[0], sx + sw))
        y2 = max(0, min(target_size[1], sy + sh))

        if x2 > x1 and y2 > y1:
            cropped = img.crop((x1, y1, x2, y2))
            save_path = os.path.join(output_folder, f"{clean_name}.png")
            cropped.save(save_path)
            exported_names.append(clean_name)
        else:
            print(f"⚠️ Skipping '{clean_name}' — invalid crop area")

    return exported_names