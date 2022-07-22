import cv2
import numpy as np

def rectangle(img, result):
    #Make a rectangle for Name, NPM, and Email
    index = [5,6,8]
    for i in index:
        x1,y1 = result[i][0][0]
        x2,y2 = result[i][0][2]
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(250,0,0), thickness=5)
    return img


