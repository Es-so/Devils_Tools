#!/usr/bin/env python





import re
from mechanize import Browser

br = Browser()
# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a useragent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

br.open("http://challenge01.root-me.org/programmation/ch8/")

br.select_form(nr=0)


br.forn = "whatever"

response = br.submit()

print response.read()













# import sys
# from PIL import Image


# def ocr(im, threshold=200, mask="letters.bmp", alphabet="0123456789abcdef"):
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
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             if (pixdata[x, y][0] > threshold) \
#                     and (pixdata[x, y][1] > threshold) \
#                     and (pixdata[x, y][2] > threshold):

#                 pixdata[x, y] = (255, 255, 255, 255)
#             else:
#                 pixdata[x, y] = (0, 0, 0, 255)

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
#     t = t[0:5]  # 5-letter captcha

#     final = sorted(t, key=lambda e: e[2])

#     answer = ''.join(map(lambda l: l[1], final))
#     # answer = ""
#     # for l in final:
#     #     answer = answer + l[1]
#     return answer


# if __name__ == '__main__':
# 	print(ocr(sys.argv[1]))






#______________________________________________________________________________
# from BeautifulSoup import BeautifulSoup
# import urllib

# post_params = {
#     param1 : val1,
#     param2 : val2,
#     param3 : val3
#         }
# post_args = urllib.urlencode(post_params)

# url = 'http://challenge01.root-me.org/programmation/ch8/'
# fp = urllib.urlopen(url, post_args)
# soup = BeautifulSoup(fp)


# from selenium import webdriver

# webpage = r"http://challenge01.root-me.org/programmation/ch8/" # edit me
# searchterm = "test" # edit me

# driver = webdriver.Chrome()
# driver.get(webpage)

# sbox = driver.find_element_by_name("cametu")
# sbox.send_keys(searchterm)

# submit = driver.find_element_by_class_name("sbtSearch")
# submit.click()