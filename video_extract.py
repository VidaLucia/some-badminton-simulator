import numpy as np
import cv2 as cv
import os
cap = cv.VideoCapture('videos/ParisFinal.webm')
# Run this to download the videos
# yt-dlp -f "bestvideo[height<=1080]+bestaudio" -a video.txt -o "videos/%(title)s.%(ext)s"
 # You can run this or... 
 # ffmpeg -i videos/set1.webm -c:v libx264 -preset ultrafast -an data/set1.mp4
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('data/output.mp4', fourcc, 20.0, (640,  480))
if not cap.isOpened():
    print("No work")
    print(os.path.exists("videos/ParisFinal.webm"))
while cap.isOpened():
    ret, frame = cap.read()
    

    if not ret:
        print("Video Over")
        break
    frame = cv.resize(frame,(640,480))

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1)== ord('q'):
        break
cap.release()
out.release()
cv.destroyAllWindows()