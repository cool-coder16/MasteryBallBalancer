import os

DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces", "anaaya")

for file in os.listdir(DIR_PATH):
    if not file.lower().endswith(".png"): continue
    stem = file[:-4]
    new_name = f"{int(stem) - 30:03d}.png"
    os.rename(os.path.join(DIR_PATH, file), os.path.join(DIR_PATH, new_name))