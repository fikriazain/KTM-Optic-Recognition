import cv2
import numpy as np
from angkatan_dict import get_angkatan

def rectangle(img, result):
    #Make a rectangle for Name, NPM, and Email
    index = [5,6,8]
    for i in index:
        x1,y1 = result[i][0][0]
        x2,y2 = result[i][0][2]
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(250,0,0), thickness=5)
    return img

def extract_npm(result):
    #Extract NPM from result
    npm = result[6][1][0:3]
    return get_angkatan("Fasilkom",npm)
