#!/usr/bin/env python

import re
from mechanize import Browser
import os
import sys
import fbchat
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
# br.set_all_readonly(False) 

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

for form in br.forms():
    print "[" + str(form) + "]"


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


# br.forms().set_all_readonly(False)

# form.set_value("rhubarb rhubarb", kind="text", nr=0)
# form.find_control("foo").readonly = False
# form.set_all_readonly(False)

form.new_control('text','message_body',{'value':''})
form.fixup()
form['message_body'] = 'input'

for form in br.forms():
    print "[" + str(form) + "]"

client = fbchat.Client(USERNAME, PASSWORD)
friend = client.getUsers("victor danain")

# for friend in friends: 
print friend[0]
sent = client.send(friend[0].uid, "Your Message")
if sent:
    print("Message sent successfully!")


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


