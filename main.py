import scripts.dwt as dwt

images_dir = './images/'
# cover_img_name = images_dir + 'IMG20170516144945_25p.bmp'
cover_img_name = images_dir + 'IMG20170516144945_25p_grayscale.bmp'
# cover_img_name = '05-cover.bmp'
# watermark_img_name = 'logo1_2_grayscale.png'
watermark_img_name = images_dir + 'logo1_grayscale.png'
# cover_img_name = '05-cover.bmp'

watermarked_img_name = images_dir + 'w.bmp'
k = 0.035

dwt.embed(cover_img_name, watermark_img_name, watermarked_img_name, k)

extract_watermarked_img = images_dir + 'w2.bmp'
dwt.extract(cover_img_name, watermarked_img_name, watermark_img_name, extract_watermarked_img, k)
extract_watermarked_img = images_dir + 'w2jpg.jpg'
dwt.extract(cover_img_name, watermarked_img_name, watermark_img_name, extract_watermarked_img, k)
