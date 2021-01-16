import scripts.dwt as dwt
import scripts.change_image as change_image
import os

root_path = os.path.abspath(os.getcwd())

images_dir = root_path + '/images/'

# cover image
cover_img = images_dir + 'a_grayscale.bmp'

# logo image
logo_img = images_dir + 'logo1_grayscale.png'

k = 0.05

# output watermarked_img
output_watermarked_img = images_dir + 'w-gray_' + str(k) + '.bmp'

# embed
# dwt.embed(cover_img, logo_img, output_watermarked_img, k)

# extract watermark
# watermarked_img = images_dir + 'w-gray_' + str(k) + '.bmp'
# extract_watermarked_img = images_dir + 'e-gray' + str(k) + '.bmp'
# dwt.extract_watermark(cover_img, watermarked_img, logo_img, extract_watermarked_img, k)

#
# extract watermark compress jpg
# input_img_grayscale = images_dir + 'w-gray_' + str(k) + '.bmp'
# output_img_grayscale = images_dir + 'w-gray_' + str(k) + '.jpg'
# # đổi từ bmp sang jpg
# change_image.rgb_to_grayscale(input_img_grayscale, output_img_grayscale)
# # trích suất
# watermarked_img = output_img_grayscale
# extract_watermarked_img = images_dir + 'e-gray-jpg_' + str(k) + '.bmp'
# dwt.extract_watermark(cover_img, watermarked_img, logo_img, extract_watermarked_img, k)

#
# extract watermark resize 80%
# input_img_resize = images_dir + 'w-gray_' + str(k) + '.bmp'
# output_img_resize = images_dir + 'w-gray_80p_' + str(k) + '.bmp'
# # resize
# change_image.resize_percent_img(input_img_resize, output_img_resize, width_percent=80, height_percent=80)
# # trích suất
# watermarked_img = output_img_resize
# extract_watermarked_img = images_dir + 'e-gray-80p_' + str(k) + '.bmp'
# dwt.extract_watermark(cover_img, watermarked_img, logo_img, extract_watermarked_img, k)
