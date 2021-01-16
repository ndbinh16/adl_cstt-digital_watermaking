import numpy as np
import pywt
from PIL import Image
import cv2


def rgb_to_grascale(input_name_img, output_name_img):
    Image.open(input_name_img).convert('L').save(output_name_img)


# rgb_to_grascale('./images/logo1_2.png', './images/logo1_2_grayscale.png')
# rgb_to_grascale('./images/logo1.png', './images/logo1_grayscale.png')
# rgb_to_grascale('./images/IMG20170516144945_25p.bmp', './images/IMG20170516144945_25p_grayscale.bmp')
# rgb_to_grascale('./images/05-cover.bmp', './images/05-cover_grayscale.bmp')
