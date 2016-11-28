#!/usr/bin/env python

import re
from mechanize import Browser
import os
import sys

br = Browser()
# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a useragent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

br.open("http://challenge01.root-me.org/programmation/ch8/")

br.select_form(nr=0)
tophp = br.response().read()

# print tophp

os.system("rmf find.txt ;\
    php get_img_captcha.php \'" + tophp + "\' ;\
    tesseract captcha/captcha.png find");

captcha_file = open('find.txt')

tt =  captcha_file.read()

print (tt)

xx = ''

for c in tt:
    if c.isalnum():
        xx += c

print "send [" + xx + "]"

br['cametu'] = xx

response = br.submit()

reponse_page = response.read()

result = re.search( r"<p>(.*)<br><\/p>", reponse_page, re.M|re.I)

br.close()

if "retente ta chance." in result.group():
    print "Result [" + result.group(1) + "]"
else:
    print result
