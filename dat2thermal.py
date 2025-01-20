import numpy as np
from PIL import Image
import os
import glob

MIN_TEMP = 90
MAX_TEMP = 115

root_path = "/home/srv-admin/images/kishino/20250119_1639/"
pattern = "*_T.dat"

file_list = []
for dirpath, _ , _ in os.walk(root_path):
    file_list.extend(glob.glob(os.path.join(dirpath, pattern)))


for file in file_list:
    with open(file, 'rb') as f:
        img_binary = f.read()

    data = np.frombuffer(img_binary, dtype=np.uint16).reshape([512, 640])
    data = data >> 8
    print(data.max(), data.min())
    data = 255*(data - MIN_TEMP)/(MAX_TEMP - MIN_TEMP)

    image = Image.fromarray(data.astype(np.uint8))
    image.save(file[:-4] + '.jpg', 'JPEG')
