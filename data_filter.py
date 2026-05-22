import cv2
import os
import numpy as np
import shutil

# How likely picture has court
def court_visible(img_path,min_court = 0.15):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_bound = (35, 40, 40)
    upper_bound = (85, 255, 255)

    mask = cv2.inRange(hsv,lower_bound,upper_bound)

    total_pixel = img.shape[0]*img.shape[1]
    count_pixel = np.count_nonzero(mask)
    ratio = count_pixel/total_pixel
    return ratio>= min_court

frames_dir = "frames/"
filter_frame = "filterFrames/"
add =0
remove = 0
os.makedirs(filter_frame,exist_ok= True)

for fname in os.listdir(frames_dir):
    if fname.startswith("."):
        continue
    path = os.path.join(frames_dir,fname)

    if court_visible(path,min_court = 0.15):
        dst = os.path.join(filter_frame,fname)
        shutil.copy(path,dst)
        add+=1
    else:
        remove +=1

print(f"Kept {add} images and removed {remove} images")