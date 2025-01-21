import os
import glob

root_path = "/home/srv-admin/images/kishino/20250120_1958/"
pattern = "*_V.dat"

file_list = []
for dirpath, _ , _ in os.walk(root_path):
    file_list.extend(glob.glob(os.path.join(dirpath, pattern)))


for file in file_list:
    new_filename = file.replace("_V.dat", "_V.jpg")
    os.rename(os.path.join(root_path, file), os.path.join(root_path, new_filename))

    print(f"renamed: {file} -> {new_filename}")

