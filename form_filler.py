import re
from mechanize import Browser

br = Browser()
# Ignore robots.txt
br.set_handle_robots( False )
# Google demands a user-agent that isn't a robot
br.addheaders = [('User-agent', 'Firefox')]

br.open("http://www.http://challenge01.root-me.org/programmation/ch8/")

br.select_form(nr=0)

browser.input_elements[1] = "whatever"

response = br.submit()

print response.read