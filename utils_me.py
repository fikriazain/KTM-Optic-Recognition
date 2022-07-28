import cv2
import numpy as np
from sympy import re
from prodi_and_angkatan import get_angkatan, get_faculty_detail

def rectangle(img, result):
    #Make a rectangle for Name, NPM, and Email
    index = [5,6,7,8]
    for i in index:
        x1,y1 = result[i][0][0]
        x2,y2 = result[i][0][2]
        cv2.rectangle(img, pt1=(x1, y1), pt2=(x2, y2), color=(250,0,0), thickness=3)
    return img

def extract_npm(result, faculty, jenjang):
    #Extract NPM from result
    npm = result[6][1][0:3]
    return get_angkatan(faculty, npm, jenjang)

def extract_prodi(result):
    prodi = result[7][1]
    return get_faculty_detail(prodi)

def resize(img, scale):
    widht = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimension = (widht, height)
    img = cv2.resize(img, dimension)
    return img

def putText(img, detail, angkatan):
    program = detail[0]
    jurusan = detail[1]
    faculty = detail[2]
    jenjang = detail[3]

    cv2.putText(img, "Jenjang: "+str(jenjang), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,2), thickness=2)
    cv2.putText(img, "Fakultas: "+str(faculty), (20, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,2), thickness=2)
    cv2.putText(img, "Jurusan: "+str(jurusan), (20, 90), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,2), thickness=2)
    cv2.putText(img, "Program: "+str(program), (20, 110), cv2.FONT_HERSHEY_PLAIN, 1.5, (255,255,2), thickness=2)
    cv2.putText(img, "Angkatan: "+str(angkatan), (20, 150), cv2.FONT_HERSHEY_PLAIN, 1.5, (43, 56, 240), thickness=2)
    return img
