import cv2
import numpy as np
import matplotlib.pyplot as plt
import easyocr
from utils_me import rectangle, resize, putText, extract_npm, extract_prodi

def detect(image):
    scale = round(500 / image.shape[0], 1)
    image = resize(image, scale)
    reader = easyocr.Reader(['id', 'en'])
    result = reader.readtext(image)
    result

    img = rectangle(image, result)

    detail = extract_prodi(result)
    npm = extract_npm(result, detail[2], detail[3])
    img = putText(image, detail, npm)

    cv2.imshow("Your ID",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


