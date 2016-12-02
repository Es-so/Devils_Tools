#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from mechanize import Browser
import os
import sys
import fbchat
import requests
from lxml import html
from subprocess import call
from bs4 import BeautifulSoup

os.system("clear")

#__________DATA_REQUIEREMENT_____________________________________________________#

USERNAME = raw_input('LOGIN/MAIL: '); 
PASSWORD = raw_input('MDP: ');
LOGIN_URL = "https://www.facebook.com/login.php"
MESSAGE_URL = "https://www.facebook.com/messages"

#__________END___________________________________________________________________#


def callBrowser(url):
	br = Browser()
	br.set_handle_robots( False )
	br.addheaders = [('User-agent', 'Firefox')]
	br.open(url)
	return br


def startConnect(browser):
	browser.select_form(nr=0)
	browser['email'] = USERNAME
	browser['pass'] = PASSWORD
	return browser.submit()


def getPage(url):
	brPage = callBrowser(url)
	r = startConnect(brPage)
	rc = startConnect(brPage)
	return brPage


def span_nbMess(page_html):
	nb_newMess = BeautifulSoup(page_html, "lxml")
	for span in nb_newMess.find_all('span'):
		if span.get('id') == "mercurymessagesCountValue":
			return span


def getAuthorsOfMess(url):
	messPage = callBrowser(url)
	for form in messPage.forms():
		print str(form)
	response = startConnect(messPage)
	response = startConnect(messPage)
	print "__"*45 + "\n"*20
	print response.read()



br = getPage(LOGIN_URL)


print  br.response().read()
print "__"*45 +"\n"*20


find = span_nbMess(br.response())
nbMess = re.findall(r".*>(.*)<.*", str(find));

print nbMess[0]
print "__"*45 + "\n"*20


if int(nbMess[0]) != 0:
	getAuthorsOfMess(MESSAGE_URL)





# <span class="_51lp _3z_5 _5ugh" id="mercurymessagesCountValue">1</span>


# client = fbchat.Client(USERNAME, PASSWORD);

# friend = client.getUsers('victor brk')

# friend_info = client.getUserInfo(friend[0].uid)

# have to scrap homepage 
# nb_mess = "<span class="_51lp _3z_5 _5ugh" id="mercurymessagesCountValue"> value = [x] </span>" 
# box = <div class="__tw toggleTargetClosed _1y2l uiToggleFlyout" role="dialog" aria-labelledby="fbMercuryJewelHeader"><div class="beeperNub"></div><div class="uiHeader uiHeaderBottomBorder jewelHeader"><div class="clearfix uiHeaderTop"><div class="rfloat _ohf"><h3 class="accessible_elem" id="fbMercuryJewelHeader">Messages</h3><div class="uiHeaderActions fsm fwn fcg"><a class="_1c1m" href="#" role="button" tabindex="0">Tout marquer comme lu</a><span role="presentation" aria-hidden="true"> · </span><a ajaxify="/ajax/messaging/composer.php" href="/messages/new/" accesskey="m" rel="dialog" role="button" id="u_0_e">Nouveau message</a></div></div><div><h3 class="uiHeaderTitle" aria-hidden="true"><div><a class="mrm _1sdi _1sde _1sdd" href="#" role="button">Récent<span class="_1sdj _1sdg">(2)</span></a><a class="_1sdi _1v8t _1sdf" href="#" role="button">Invitations<span class="_1sdj _1sdh"></span></a></div></h3></div></div></div><div class="_3v_l"><div data-reactroot="" class="_2q3u uiScrollableArea fade uiScrollableAreaWithShadow contentAfter" height="135" style="height: 135px;"><div class="uiScrollableAreaWrap scrollable"><div class="uiScrollableAreaBody" style="margin-right: -15px;"><div class="uiScrollableAreaContent"><ul class="jewelContent"><li><div class="_1xfk"></div></li><li class="jewelItemNew"><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1232897259"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/c0.0.50.50/p50x50/13880368_10207055631769207_5793305162472586463_n.jpg?oh=d3e28c663e590655aaf7587d5d16900e&amp;oe=58B4A9AF" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme lu(s)" class="_5c9q" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme lu(s)" role="button" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><em class="_4qba" data-intl-translation="{conversation-title} ({unread-count})" data-intl-trid=""><!-- react-text: 245 -->Victor Brk (3)<!-- /react-text --></em></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span><span><!-- react-text: 38 -->e\<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="Aujourd’hui" data-utime="1480565232.861">05:07</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1634995587"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/l/t1.0-1/p50x50/14232596_10208971657562057_1811180678890892618_n.jpg?oh=795176aea0d1cffa46bd83bd7c03348f&amp;oe=58B9CF39" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 59 -->Victor Danain<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5 repliedLast"></span><span><span><!-- react-text: 66 -->Wesh Victor Danain bot: il parle trop le mec c est un truc de ouf...<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="Aujourd’hui" data-utime="1480565127.939">05:05</abbr></div></div></div></div></div></div></a></li><li class="jewelItemNew"><a class="messagesContent" role="button" href="https://www.facebook.com/messages/conversation-1177709515576750"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div style="height: 50px; background-image: url(&quot;https://scontent-cdg2-1.xx.fbcdn.net/v/t34.0-12/14798786_10209007854087140_316294066_n.jpg?oh=40ad19cfc0e34e9f0bf445a3bc33c8bc&amp;oe=58419F9A&quot;); background-position: 50% 50%; background-repeat: no-repeat; background-size: cover; width: 50px;"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme lu(s)" class="_5c9q" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme lu(s)" role="button" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><em class="_4qba" data-intl-translation="{conversation-title} ({unread-count})" data-intl-trid=""><!-- react-text: 88 --><!-- /react-text --><span><!-- react-text: 90 -->Aéroport<!-- /react-text --></span><!-- react-text: 91 --> (18)<!-- /react-text --></em></span></strong><span class="presenceIndicator groupThread"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span><em class="_4qba" data-intl-translation="{name}&nbsp;: {conversation_snippet}" data-intl-trid=""><!-- react-text: 98 -->Hamza&nbsp;: <!-- /react-text --><span><!-- react-text: 100 -->Ahahahahahahahahaha<!-- /react-text --></span><!-- react-text: 101 --><!-- /react-text --></em></span></div><div class="time"><abbr class="timestamp" title="Mercredi" data-utime="1480536602.788">mer</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1207456300"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/p50x50/13012762_10209071906493967_188737036982795781_n.jpg?oh=a7757a0e6db134a41994dcb3837f6bda&amp;oe=58C51B74" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 122 -->Matthias Lct<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5 repliedLast seenByAll"></span><span><span><!-- react-text: 129 -->https://geoguessr.com/challenge/EvGZ38hvwGcsum8o<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="Vendredi" data-utime="1480094225.898">ven</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/100013953674496"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/c0.6.50.50/p50x50/14993449_138270846648037_3570741965865909806_n.jpg?oh=e9a8adfe3baa183084c790835d38ddc0&amp;oe=58F7F83D" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 150 -->Adrien Dacher<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span><span><!-- react-text: 157 -->ouais mais bon les gens me gave de ouf aussi ou qjaille<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="18 novembre" data-utime="1479497366.332">18 novembre</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1317376418"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/p50x50/10421438_10203528732561747_1690861697709891400_n.jpg?oh=6dbd469c98571ce405f1bd1dd17ce6bc&amp;oe=58BF40CD" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 178 -->Julien Ripouteau<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5 repliedLast"></span><span><span><!-- react-text: 185 -->bon c kan ktu pase<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="9 novembre" data-utime="1478717990.449">9 novembre</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1444606659"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/p50x50/14183859_10210987168342221_8931088304663776747_n.jpg?oh=643379cfdeac56325aeb8e308dc9d1d0&amp;oe=58C419EC" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 206 -->David Mathe<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span></span></div><div class="time"><abbr class="timestamp" title="9 novembre" data-utime="1478717965.041">9 novembre</abbr></div></div></div></div></div></div></a></li><li class=""><a class="messagesContent" role="button" href="https://www.facebook.com/messages/100008320896636"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/p50x50/14469586_1784203745200305_679852985479145587_n.jpg?oh=c9fe988b6fe554707a359a4ddf48c94c&amp;oe=58B27583" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme non lu" class=" _5c9_" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme non lu" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><!-- react-text: 232 -->Pariston Hill<!-- /react-text --></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span><span><!-- react-text: 239 -->ça a durè combien de temps le hangout avec nicolas?<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="9 novembre" data-utime="1478706261.217">9 novembre</abbr></div></div></div></div></div></div></a></li></ul><div class="_v8y"><a href="#"><em class="_4qba" data-intl-translation="Afficher les plus anciens" data-intl-trid=""><!-- react-text: 12 -->Afficher les plus anciens<!-- /react-text --></em></a></div></div></div></div><div class="uiScrollableAreaTrack invisible_elem" style="opacity: 0;"><div class="uiScrollableAreaGripper" style="height: 35.0198px; top: 0px;"></div></div></div></div><div id="MercuryJewelFooter"><span></span><div class="jewelFooter"><a class="seeMore" href="https://www.facebook.com/messages/" target="" accesskey="4"><span>Voir tout</span></a></div></div></div>
# unread = <li class="jewelItemNew"><a class="messagesContent" role="button" href="https://www.facebook.com/messages/1232897259"><div direction="left" class="clearfix"><div class="_ohe lfloat"><div class="MercuryThreadImage _4qeb img _8o _8s"><div class="_55lt" size="50" style="width: 50px; height: 50px;"><img src="https://scontent-cdg2-1.xx.fbcdn.net/v/t1.0-1/c0.0.50.50/p50x50/13880368_10207055631769207_5793305162472586463_n.jpg?oh=d3e28c663e590655aaf7587d5d16900e&amp;oe=58B4A9AF" alt="" class="img" width="50" height="50"></div></div></div><div class=""><div class="_42ef clearfix" direction="right"><div class="_ohf rfloat"><div><span></span><div class="x_div"><div aria-label="Marquer comme lu(s)" class="_5c9q" data-hover="tooltip" data-tooltip-alignh="center" data-tooltip-content="Marquer comme lu(s)" role="button" tabindex="0"></div></div></div></div><div class=""><div class="content"><div class="author"><strong><span><em class="_4qba" data-intl-translation="{conversation-title} ({unread-count})" data-intl-trid=""><!-- react-text: 245 -->Victor Brk (3)<!-- /react-text --></em></span></strong><span class="presenceIndicator"><span class="accessible_elem"></span></span></div><div class="snippet preview"><span class="_3jy5"></span><span><span><!-- react-text: 38 -->e\<!-- /react-text --></span></span></div><div class="time"><abbr class="timestamp" title="Aujourd’hui" data-utime="1480565232.861">05:07</abbr></div></div></div></div></div></div></a></li>
# author = <div id=authors />

# {message_counts":[{"unread_count":2,"unseen_count":1,"seen_timestamp":1480640440891,"folder":"inbox"}




# last_messages = client.getThreadInfo(friend[0].uid,0)
# last_messages.reverse()  # messages come in reversed order


# for message in last_messages:
#     print(message.body)

# print (last_messages)
