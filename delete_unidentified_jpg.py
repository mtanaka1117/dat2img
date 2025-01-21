import os
from PIL import Image, UnidentifiedImageError
import glob

root_path = '/home/srv-admin/images/kishino/20250116_1704/'
pattern = "*_V.jpg"

file_list = []
for dirpath, _ , _ in os.walk(root_path):
    file_list.extend(glob.glob(os.path.join(dirpath, pattern)))

for file in file_list:
    try:
        with Image.open(file) as img:
            img.verify()
    except:
        print(f"removed file: {file}")
        os.remove(file)
