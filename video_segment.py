import cv2
import os
# collecting data following the method of a differnet Repo
# https://github.com/yastrebksv/TennisCourtDetector

def extract_frame(input_v,output_p,step = 50):
    os.makedirs(output_p,exist_ok= True)

    cap = cv2.VideoCapture(input_v)
    frame_idx = 0
    saved = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % step == 0: # multiple of 50
            filename = os.path.join(output_p,f"frame_{frame_idx:06d}.jpg")
            cv2.imwrite(filename,frame)
            saved+=1 
        frame_idx+=1
    cap.release()
    print(f"Saved {saved} at {output_p}")


import glob

for video in glob.glob("data/*.mp4"):

    name = os.path.splitext(os.path.basename(video))[0]
    extract_frame(video, f"frames/{name}",step = 50)


