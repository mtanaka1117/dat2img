import numpy as np
import os
import glob
from PIL import Image, UnidentifiedImageError

# root_path = "images/kishino/"
root_path = '/home/srv-admin/images/kishino/20250120_1954/'
pattern = "*_V.jpg"


file_list = []
for dirpath, _ , _ in os.walk(root_path):
    file_list.extend(glob.glob(os.path.join(dirpath, pattern)))


feature_points1 = np.array([[ 393,  221],
                            [1458, 1071]])

for file in file_list:
    try:
        with Image.open(file) as img:
            left_x, left_y = feature_points1[0]
            right_x, right_y = feature_points1[1]
            cropped_img = img.crop((left_x, left_y, right_x, right_y))
            cropped_img.save(str(file))
    except UnidentifiedImageError as e:
        print(f"failed to open {file}: {e}")
        os.remove(file)
    except OSError as e:
        print(f"failed to open {file}: {e}")
        os.remove(file)