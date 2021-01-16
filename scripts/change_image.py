import numpy as np
import pywt
from PIL import Image
import cv2

images_dir = '../images/'


def rgb_to_grayscale(input_img, output_img):
    Image.open(input_img).convert('L').save(output_img)
    print(input_img + ' -> to grayscale ->' + output_img)


def resize_percent_img(input_img, output_img, width_percent=80, height_percent=80):
    im = Image.open(input_img)
    width_r = int((im.width * width_percent) / 100)
    height_r = int((im.height * height_percent) / 100)
    resized = im.resize((width_r, height_r))
    pixels = np.array(resized).astype(np.uint8)
    Image.fromarray(pixels).save(output_img)
    im.close()


# def crop_img(input_img, output_img, left, right, upper, lower):
#     im = Image.open(input_img)
#     left_r = int(im.width / left)
#     right_r = int(im.width / right)
#     upper_r = int(im.height / upper)
#     lower_r = int(im.height / lower)
#     crop_img = np.array(im.crop((left_r, upper_r, right_r, lower_r))).astype(np.uint8)
#     Image.fromarray(crop_img).save(output_img)
#     im.close()


input_img_grayscale = images_dir + 'w-gray_0.05.bmp'
output_img_grayscale = images_dir + 'w-gray_0.05.jpg'
# rgb_to_grayscale(input_img_grayscale, output_img_grayscale)

# resize image
input_img_resize = images_dir + 'w-gray_0.05.bmp'
output_img_resize = images_dir + 'w-gray_0.05_80p.bmp'
# resize_percent_img(input_img_resize, output_img_resize, width_percent=80, height_percent=80)

# crop image
input_img_crop = images_dir + 'w-gray_0.05.bmp'
output_img_crop = images_dir + 'w-gray_0.05_crop.bmp'
crop_img(input_img_resize, output_img_resize, left=80, right=80, upper=80, lower=80)

# # Thu nhỏ ảnh & phóng to lên lại
# img = Image.open('10-marked_lena.bmp')
# down_img = img.resize((int(img.width / 2), int(img.height / 2)))
# down_up_img = down_img.resize((img.width, img.height))
# down_up_img.save('10-down_up_marked_lena.bmp')
# img.close()

# # Crop ảnh, rồi tạo ảnh hoàn chỉnh (để có thể check watermark)
# # bằng cách thêm vào các phần của ảnh ban đầu (ko có watermark)
# img = Image.open('10-marked_lena.bmp')
# left = int(img.width / 4); upper = int(img.height / 4)
# right = int(img.width / 4 * 3); lower = int(img.height / 4 * 3)
# crop_img = np.array(img.crop((left, upper, right, lower)))
# uncrop_crop_img = np.array(Image.open('10-lena.bmp'))
# uncrop_crop_img[upper:lower, left:right] = crop_img
# Image.fromarray(uncrop_crop_img).save('10-uncrop_crop_marked_lena.bmp')
