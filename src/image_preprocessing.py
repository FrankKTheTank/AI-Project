from PIL import Image
import shutil
import os

"""Rotation of a simple picture and saving it in different versions 
   Args: dir_name:string, image:image, counter:integer 
   Returns: different perspectives of the rotated image (5 degree steps)   
"""
def rotate_Picture(dir_name, image, counter):

    for r in range(0, 360, 45):

        rotate_img = image.rotate(r)
        rotate_img.save(f"C:/Users/Frank/Desktop/Lego/{dir_name}/rotate_defekt" + str(counter) + "." + str(r) + ".jpg")

"""Tansposition of a simple picture and saving it in different versions 
   Args: dir_name:string, image:image, counter:integer 
   Returns: different perspectives of the transposed Image (90 degree steps, flipped-images)  
"""
def transpose_Picture(dir_name, image, counter):

    transposeList = [Image.FLIP_LEFT_RIGHT, Image.FLIP_TOP_BOTTOM]

    for t in transposeList:

        transpose_img = image.transpose(t)
        transpose_img.save(f"C:/Users/Frank/Desktop/Lego/{dir_name}/transpose_defekt" + str(counter) + "." + str(t) +".jpg")
        t += 1


if __name__ == '__main__':

    dir_errorList = ['Bemalt','Intakt', 'Verformt','Vermackt','Zerkratzt']

    for err_dict in dir_errorList:

            dir_path_lego = f'C:/Users/Frank/Desktop/Pics/Fotos/{err_dict}'

            img_number = 0

            for element in os.listdir(dir_path_lego):

                            """
                            Set the base width and 
                            calculate the aspect ratio for the width( with_percent) = base with / existing width of the image,
                            calculate the correct height for the base width (hsize) = existing width of the image * with_percent
                            and then the size of the image is adjusted based on the two values (base_width and hsize).
                            """
                            base_width = 400
                            image = Image.open(dir_path_lego + '/' + element)
                            width_percent = (base_width / float(image.size[0]))
                            hsize = int((float(image.size[1]) * float(width_percent)))
                            image = image.resize((base_width, hsize), Image.ANTIALIAS)

                            """Transpose and save pictures"""
                            transpose_Picture(err_dict, image, img_number)

                            """Rotate and save pictures"""
                            rotate_Picture(err_dict, image, img_number)

                            """Increase counter to save images by a numbering"""
                            img_number += 1

                            """Copy 20% of the lego images to a validation folder"""
                            dir_path_lego = f'C:/Users/Frank/Desktop/Lego/{err_dict}'

                            if((img_number%5) == 0):
                                shutil.copy(dir_path_lego + '/' + f'{element}', f'C:/Users/Frank/Desktop/LegoVal/{err_dict}')

