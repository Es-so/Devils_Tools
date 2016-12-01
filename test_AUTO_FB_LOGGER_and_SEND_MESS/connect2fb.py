#!/usr/bin/env python

import re
from mechanize import Browser
import os
import sys
import fbchat
import requests
from lxml import html


#__________DATA_REQUIEREMENT_____________________________________________________#

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');
LOGIN_URL = "https://www.facebook.com"
TARGET_MP = raw_input('FRIENDS: ');
TARGET = TARGET_MP;
TARGET_MP.replace(' ', '.');
# URL_MESS = "https://www.facebook.com/messages/" + TARGET_MP;
URL_MESS = "https://www.facebook.com/messages/victor.danain"

# __MULTIPLE_MESSAGES_USER_______________________________

with open(raw_input("TARGETS USERS FILE: "), "r") as ins:
    TARGETS = []
    for line in ins:
        TARGETS.append(line)

#_______________________________________________________


#__________END_DATA_REQUIEREMENT_________________________________________________#



br = Browser()
br.set_handle_robots( False )
br.addheaders = [('User-agent', 'Firefox')]
br.open(LOGIN_URL)

print  br.response().read()

br.select_form(nr=0)

br['email'] = USERNAME
br['pass'] = PASSWORD

response = br.submit()


print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
________________________________________________________________________________\
\	\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

reponse_page = response.read()
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


form.new_control('text','message_body',{'value':''})
form.fixup()
form['message_body'] = 'input'

for form in br.forms():
    print "[" + str(form) + "]"

client = fbchat.Client(USERNAME, PASSWORD)
friend = client.getUsers(TARGET)


friends = []
for selected_target in TARGETS:
	print selected_target + "<-"*47
	friends.append(client.getUsers(selected_target))

	


friend_info = client.getUserInfo(friend[0].uid)

for f in friends:
	print ">"*50 + "\n" + str(f[0])
	client.send(f[0].uid, "message personnalise pour mon petit: " + str(f[0].name))


# print "|"*80 + str(friends[1]) + "|"*80

# for friend in friends: 

# sent = client.send(friend[0].uid, raw_input("MESSAGE: "))
# if sent:
#     print("Message sent successfully!")

print friend_info

last_messages = client.getThreadInfo(friend[0].uid,0)
last_messages.reverse()  # messages come in reversed order

for message in last_messages:
    print(message.body)

print (last_messages)


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


