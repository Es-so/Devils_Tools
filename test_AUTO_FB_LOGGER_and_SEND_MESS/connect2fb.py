#!/usr/bin/env python

import re
from mechanize import Browser
import os
import sys

import requests
from lxml import html

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');

LOGIN_URL = "https://www.facebook.com/login.php?login_attempt=1&lwv=110"
TARGET_MP = raw_input('FRIENDS: ');
TARGET_MP.replace(' ', '.');
URL = "https://www.facebook.com/messages/" + TARGET_MP;
# URL = "https://www.facebook.com/messages/victor.danain"

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
	main()







# payload = {
# 	"username": "khatir.sofiane@gmail.com", 
# 	"password": "marina94f", 
# 	"csrfmiddlewaretoken": "<CSRF_TOKEN>"
# }

# br = Browser()
# # Ignore robots.txt
# br.set_handle_robots( False )
# # Google demands a useragent that isn't a robot
# br.addheaders = [('User-agent', 'Firefox')]

# br.open("https://www.facebook.com")

# br.select_form(nr=0)
# tophp = br.response().read()

# # print tophp

# os.system("rmf find.txt ;\
#     php get_img_captcha.php \'" + tophp + "\' ;\
#     tesseract captcha/captcha.png find");

# captcha_file = open('find.txt')

# tt =  captcha_file.read()

# print (tt)

# xx = ''

# for c in tt:
#     if c.isalnum():
#         xx += c

# print "send [" + xx + "]"

# br['cametu'] = xx

# response = br.submit()

# reponse_page = response.read()

# result = re.search( r"<p>(.*)<br><\/p>", reponse_page, re.M|re.I)

# br.close()

# if "retente ta chance." in result.group():
#     print "Result [" + result.group(1) + "]"
# else:
#     print result