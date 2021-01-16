import numpy as np
import pywt
from PIL import Image


#                             -------------------
#                             |        |        |
#                             | cA(LL) | cH(LH) |
#                             |        |        |
# (cA, (cH, cV, cD))  <--->   -------------------
#                             |        |        |
#                             | cV(HL) | cD(HH) |
#                             |        |        |
#                             -------------------


def embed(cover_img, logo_img, output_watermarked_img, k=0.05):
    # read cover
    cover_img = Image.open(cover_img).convert('L')
    data = np.array(cover_img)

    # read watermark
    logo_img = Image.open(logo_img).convert('L')
    watermark_data = np.array(logo_img)

    # DWT
    coeffs = pywt.dwt2(data, 'haar')
    # cA, (cH, cV, cD) = coeffs
    LL1, (LH1, HL1, HH1) = coeffs
    LL2, (HL2, LH2, HH2) = pywt.dwt2(LL1, 'haar')
    LL3, (HL3, LH3, HH3) = pywt.dwt2(LL2, 'haar')
    # print('LV3:', type(LL3), LL3.shape, HL3.shape, LH3.shape, HH3.size)
    # check can embed?
    if watermark_data.size < HL3.size:
        # col, row
        height_w, width_w = watermark_data.shape
        sliced_wLH3 = LH3[:height_w, :width_w] + (watermark_data * k)
        for i in range(sliced_wLH3.shape[0]):
            for j in range(sliced_wLH3.shape[1]):
                LH3[i, j] = sliced_wLH3[i, j]
        # print('embed_watermark:', sliced_wLH3.shape)
        wLH3 = LH3

    if watermark_data.size > HL3.size:
        # print('resize smaller')
        # size – The requested size in pixels, as a 2-tuple: (width, height).
        watermark_resized = logo_img.resize((HL3.shape[1], HL3.shape[0]))
        # tạo file resize mới
        idx_rdot = logo_img.rfind('.')
        extension = logo_img[idx_rdot:]
        name = logo_img[:idx_rdot]
        new_name = name + '_resized' + extension
        watermark_resized.save(new_name)
        # convert msg
        # embed_watermark = np.where(np.array(watermark_resized) > 128, 1, 0)
        embed_watermark = np.array(watermark_resized)
        # print('embed_watermark:', embed_watermark.shape)
        # embed at LV3
        wLH3 = LH3 + (embed_watermark * k)
    # IDWT
    LL2 = pywt.idwt2((LL3, (HL3, wLH3, HH3)), 'haar')
    LL1 = pywt.idwt2((LL2, (HL2, LH2, HH2)), 'haar')
    data_idwt = pywt.idwt2((LL1, (LH1, HL1, HH1)), 'haar')
    # save watermarked img
    marked_pixels = np.rint(data_idwt).astype(np.uint8)
    marked_img = Image.fromarray(marked_pixels)
    marked_img.save(output_watermarked_img)
    print(output_watermarked_img + ' watermarked')


def extract_watermark(origin_image, watermarked_image, logo_image, extract_watermarked_img, k=0.05):
    # read watermarked image
    watermarked_img = Image.open(watermarked_image).convert('L')
    watermarked_data = np.array(watermarked_img)
    height_w, width_w = watermarked_data.shape

    # read origin image
    origin_img = Image.open(origin_image).convert('L')
    origin_img = origin_img.resize((width_w, height_w))
    origin_data = np.array(origin_img)
    height_o, width_o = origin_data.shape

    # read watermark img
    logo_image = Image.open(logo_image)
    logo_data = np.array(logo_image)
    height_logo, width_logo = logo_data.shape

    # DWT
    # LV1
    ocoeffs = pywt.dwt2(origin_data, 'haar')
    wcoeffs = pywt.dwt2(watermarked_data, 'haar')
    # cA, (cH, cV, cD) = coeffs
    oLL1, (oLH1, oHL1, oHH1) = ocoeffs
    wLL1, (wLH1, wHL1, wHH1) = wcoeffs
    # print('LV1:', type(wLL1), wLL1.shape, wLH1.shape, wHL1.shape, wHH1.size)

    # LV2
    oLL2, (oHL2, oLH2, oHH2) = pywt.dwt2(oLL1, 'haar')
    wLL2, (wHL2, wLH2, wHH2) = pywt.dwt2(wLL1, 'haar')
    # print('LV2:', type(wLL2), wLL2.shape, wHL2.shape, wLH2.shape, wHH2.size)

    # LV3
    oLL3, (oHL3, oLH3, oHH3) = pywt.dwt2(oLL2, 'haar')
    wLL3, (wHL3, wLH3, wHH3) = pywt.dwt2(wLL2, 'haar')
    # print('LV3:', type(oLH3), oLH3.shape, type(wLH3), wLH3.shape)

    # get watermark
    eLH3 = (oLH3 - wLH3)
    eLH3 = eLH3[:height_logo, : width_logo] / k
    # print('eLH3:', type(eLH3), eLH3.shape)

    # save watermarked img
    extracted_pixels = np.rint(eLH3).astype(np.uint8)
    extracted_img = Image.fromarray(extracted_pixels)
    extracted_img.save(extract_watermarked_img)
    no_zeros = np.count_nonzero(extracted_pixels)
    print('extract:', no_zeros)
