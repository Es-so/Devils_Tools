#!/usr/bin/env python

import re
from mechanize import Browser
import os
import sys

import requests
from lxml import html

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');

LOGIN_URL = "https://www.facebook.com"
TARGET_MP = raw_input('FRIENDS: ');
TARGET_MP.replace(' ', '.');
# URL_MESS = "https://www.facebook.com/messages/" + TARGET_MP;
URL_MESS = "https://www.facebook.com/messages/victor.danain"

br = Browser()
# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a useragent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

br.open(LOGIN_URL)

br.select_form(nr=0)
tophp = br.response().read()
print tophp

br['email'] = USERNAME
br['pass'] = PASSWORD

response = br.submit()

reponse_page = response.read()

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
________________________________________________________________________________\
\	\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

print reponse_page

page_mess = br.open(URL_MESS)

for form in br.forms():
    print "[" + str(form) + "]"

br.select_form(nr=0)
br['email'] = USERNAME
br['pass'] = PASSWORD

response = br.submit()


print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
________________________________________________________________________________\
\	\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

dd = response.read()
ff = br.response()

print ">>>>" + dd + "<<"

print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
________________________________________________________________________________\
\	\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
form.set_value("rhubarb rhubarb", kind="text", nr=0)
for form in br.forms():
    print "[" + str(form) + "]"


# import re
# from mechanize import Browser
# import os
# import sys

# import requests
# from lxml import html

# USERNAME = raw_input('LOGIN/MAIL: '); 
# PASSWORD = raw_input('MDP: ');

# LOGIN_URL = "https://www.facebook.com/login.php?login_attempt=1&lwv=110"
# TARGET_MP = raw_input('FRIENDS: ');
# TARGET_MP.replace(' ', '.');
# # URL = "https://www.facebook.com/messages/" + TARGET_MP;
# URL = "https://www.facebook.com/messages/victor.danain"

# def main():
#     session_requests = requests.session()

#     # Get login csrf token
#     result = session_requests.get(LOGIN_URL)
#     tree = html.fromstring(result.text)
#     authenticity_token = ''

#     # Create payload
#     payload = {
#         "username": USERNAME, 
#         "password": PASSWORD, 
#         "csrfmiddlewaretoken": authenticity_token
#     }

#     # Perform login
#     result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

#     # Scrape url
#     result = session_requests.get(URL, headers = dict(referer = URL))
#     print result.text
#     tree = html.fromstring(result.content)
#     bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

#     print(bucket_names)

# if __name__ == '__main__':
# 	main()


# emojiChoices:["✌","😂","😝","😁","😱","👉","🙌","🍻","🔥","🌈","☀","🎈","🌹","💄","🎀","⚽","🎾","🏁","😡","👿","🐻","🐶","🐬","🐟","🍀","👀","🚗","🍎","💝","💙","👌","❤","😍","😉","😓","😳","💪","💩","🍸","🔑","💖","🌟","🎉","🌺","🎶","👠","🏈","⚾","🏆","👽","💀","🐵","🐮","🐩","🐎","💣","👃","👂","🍓","💘","💜","👊","💋","😘","😜","😵","🙏","👋","🚽","💃","💎","🚀","🌙","🎁","⛄","🌊","⛵","🏀","🎱","💰","👶","👸","🐰","🐷","🐍","🐫","🔫","👄","🚲","🍉","💛","💚"]