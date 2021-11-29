from matplotlib import pyplot as plt
from scipy import ndimage
import cv2

img = cv2.imread('C:/Users/Frank/Desktop/Pics/Test/0001.png')
print(cv2.imshow('Image',img))
plt.imshow(img)
plt.show()





if __name__ == '__main__':



     rotated = ndimage.rotate(img, 45)
     plt.imshow(rotated)
     plt.show()

     rotated = ndimage.rotate(img, 90)
     plt.imshow(rotated)
     plt.show()

     rotated = ndimage.rotate(img, 180)
     plt.imshow(rotated)
     plt.show()