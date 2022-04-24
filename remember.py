import cv2
import numpy as np
from PIL import Image
import matplotlib.image as image

def find_message(path):
    """
       function that return the min length of the argument
    """
    message=""
    images = Image.open(path)
    images = images.convert("L")

    pixcel = list(images.getdata())
    matrix_pixcel = np.empty((images.size[1] , images.size[0]))

    for line in range(images.size[1]):
        for column in range(images.size[0]):
            matrix_pixcel[line][column] = pixcel[0]
            pixcel.pop(0)

    for column in range(images.size[0]):
        for line in range(images.size[1]):
            if not matrix_pixcel[line][column] == 255:
                message += chr(line)
                break
    return  message




if __name__=="__main__":
   print(find_message(r"C:\Users\efrat\Downloads\code.png"))

