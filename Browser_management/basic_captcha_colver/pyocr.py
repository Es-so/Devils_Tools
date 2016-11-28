#!/usr/bin/env python


import sys
from PIL import Image

img = Image.open(sys.argv[1]) # Your image here!
img = img.convert("RGBA")

pixdata = img.load()

# Make the letters bolder for easier recognition

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][0] < 90:
            pixdata[x, y] = (0, 0, 0, 255)

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][1] < 136:
            pixdata[x, y] = (0, 0, 0, 255)

for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pixdata[x, y][2] > 0:
            pixdata[x, y] = (255, 255, 255, 255)

img.save("input-black.gif", "GIF")

#   Make the image bigger (needed for OCR)
im_orig = Image.open('input-black.gif')
big = im_orig.resize((1000, 500), Image.NEAREST)

ext = ".tif"
big.save("input-NEAREST" + ext)

#   Perform OCR using tesseract-ocr library
from tesseract import image_to_string
from pytesser import *

image = Image.open('input-NEAREST.tif')

print (image_to_string(image))









# from PIL import Image
# import sys


# def ocr(im, threshold=200, mask="letters.bmp", alphabet="0123456789abcdefhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
#     img = Image.open(im)
#     img = img.convert("RGB")
#     box = (8, 8, 58, 18)
#     img = img.crop(box)
#     pixdata = img.load()

#     # open the mask
#     letters = Image.open(mask)
#     ledata = letters.load()

#     def test_letter(img, letter):
#         A = img.load()
#         B = letter.load()
#         mx = 1000000
#         max_x = 0
#         x = 0
#         for x in range(img.size[0] - letter.size[0]):
#             _sum = 0
#             for i in range(letter.size[0]):
#                 for j in range(letter.size[1]):
#                     _sum = _sum + abs(A[x + i, j][0] - B[i, j][0])
#             if _sum < mx:
#                 mx = _sum
#                 max_x = x
#         return mx, max_x

#     # Clean the background noise, if color != white, then set to black.
#     # for y in range(img.size[1]):
#     #     for x in range(img.size[0]):
#     #         if (pixdata[x, y][0] > threshold) \
#     #                 and (pixdata[x, y][1] > threshold) \
#     #                 and (pixdata[x, y][2] > threshold):
#     #             pixdata[x, y] = (255, 255, 255, 255)
#     #         else:
#     #             pixdata[x, y] = (0, 0, 0, 255)

#     counter = 0
#     old_x = -1

#     letterlist = []

#     for x in range(letters.size[0]):
#         black = True
#         for y in range(letters.size[1]):
#             if ledata[x, y][0] != 0:
#                 black = False
#                 break
#         if black:
#             if True:
#                 box = (old_x + 1, 0, x, 10)
#                 letter = letters.crop(box)
#                 t = test_letter(img, letter)
#                 letterlist.append((t[0], alphabet[counter], t[1]))
#             old_x = x
#             counter += 1

#     box = (old_x + 1, 0, 140, 10)
#     letter = letters.crop(box)
#     t = test_letter(img, letter)
#     letterlist.append((t[0], alphabet[counter], t[1]))

#     t = sorted(letterlist)
#     t = t[0:12]  # 5-letter captcha

#     final = sorted(t, key=lambda e: e[2])

#     answer = ''.join(map(lambda l: l[1], final))
#     # answer = ""
#     # for l in final:
#     #     answer = answer + l[1]
#     return answer


# if __name__ == '__main__':
#     print(ocr(sys.argv[1]))












# from PIL import Image

# im = Image.open("pyte.png")
# im = im.convert("P")
# im2 = Image.new("P",im.size,255)

# im = im.convert("P")

# temp = {}

# for x in range(im.size[1]):
#   for y in range(im.size[0]):
#     pix = im.getpixel((y,x))
#     temp[pix] = pix
#     if pix == 220 or pix == 227:
#         im2.putpixel((y,x),0)
#         print "x"

# im2.save("output.png")
