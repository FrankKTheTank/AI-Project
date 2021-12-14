from PIL import Image
import os

"""Rotation of a simple picture and saving it in different versions 
   Args: dir_name:string, image:image, counter:integer 
   Returns: different perspectives of the rotated image (5 degree steps)   
"""
def rotate_Picture(dir_name, image, counter):

    for r in range(0, 360, 5):

        rotate_img = image.rotate(r)
        rotate_img.save(f"C:/Users/Frank/Desktop/Lego/{dir_name}/rotate_defekt" + str(counter) + "." + str(r) + ".jpg")

"""Tansposition of a simple picture and saving it in different versions 
   Args: dir_name:string, image:image, counter:integer 
   Returns: different perspectives of the transposed Image (90 degree steps, flipped-images)  
"""
def transpose_Picture(dir_name, image, counter):

    transposeList = [Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270, Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM]

    for t in transposeList:

        transpose_img = image.transpose(t)
        transpose_img.save(f"C:/Users/Frank/Desktop/Lego/{dir_name}/transpose_defekt" + str(counter) + "." + str(t) +".jpg")
        t += 1


if __name__ == '__main__':

    dir_errorList = ['Bemalt','Verformt','Vermackt','Zerkratzt']
    size = [400, 400]

    for err_dict in dir_errorList:

            dir_path = f'C:/Users/Frank/Desktop/Pics/Fotos2/{err_dict}'

            img_number = 0

            for element in os.listdir(dir_path):


                         img = Image.open(dir_path + '//' + element)

                         img = img.resize(size)

                         transpose_Picture(err_dict, img, img_number)

                         rotate_Picture(err_dict, img, img_number)

                         img_number += 1

