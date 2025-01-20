import numpy as np
import os
import glob
import cv2
from pathlib import Path


root_path = "images/kishino/"
pattern = "*_V.dat"

file_list = []
for dirpath, _ , _ in os.walk(root_path):
    file_list.extend(glob.glob(os.path.join(dirpath, pattern)))

for file in file_list:
    yuv_array = np.fromfile(file, np.uint8).reshape([1200, 1920, 2])
    bgr = cv2.cvtColor(yuv_array, cv2.COLOR_YUV2BGR_UYVY)
    cv2.imwrite(str(Path(file).with_suffix('.jpg')), bgr)
