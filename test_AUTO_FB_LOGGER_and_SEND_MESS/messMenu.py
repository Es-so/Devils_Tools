#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import curses, os
import messageChecker

screen = curses.initscr()
curses.noecho() 
curses.cbreak() 
curses.start_color() 
screen.keypad(1)


curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_WHITE) 
h = curses.color_pair(1) 
n = curses.A_NORMAL 

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"
MID = "m"  #personal convers /!\ not only
_ID = "i"  #group
INFO = 'info' 
EXT = 'extend'


menu_data = {
  'title': "Message Checker", 'type': MENU, EXT : '', 'subtitle': "Please select an option...",
  'options':[
        { 'title': "Unread messages", 'type': MENU, EXT : '', 'subtitle': "Please select an option...", #
        'options': [
            { 'title': "author: ", 'type': INFO, EXT : '', 'ID': 'uid', 'nbUnread' : 'x' },
        ]
        },
        { 'title': "Sent messages", 'type': MENU, EXT : '', 'subtitle': "Please select an option...",  #
        'options': [
          { 'title': "author: ", 'type': INFO, EXT : '', 'ID': 'uid' },
        ]
        },
        { 'title': "Send new message", 'type': COMMAND, EXT : '', 'command': 'NewMessage' },               #
  ]
}

message_f = {
  'title' : "<Sender>: <body>", 'type' : INFO, EXT : '', 'timestamp' : 'timestamp', 'body' : 'body', 'subtitle': "Please select an option...", 
  'options' : [
            { 'title' : 'Mark as read', 'type' : COMMAND, EXT : '', 'command' : 'MarkAsRead'},
            { 'title' : 'Reply', 'type' : COMMAND, EXT : '', 'command' : 'Reply'},
            { 'title' : 'Decrypt', 'type' : COMMAND, EXT : '', 'command' : 'Decrypt', 'body' : 'body', 'timestamp' : 'timestamp'},
            { 'title' : 'Reply with encription', 'type' : COMMAND, EXT : '', 'command' : 'cryptReply'},
        ]
}

def fillMenu(menuFormat=menu_data):
  
  allMess = messageChecker.getUnread()
  for key in allMess:
    if int(key['nbUnread']) > 0:
      menuFormat['options'][0]['options'].append(key)

#Menu
#/!\ not dynamic yet
def runmenu(menu, parent):

  if parent is None:
    lastoption = "Exit"
  else:
    lastoption = "Return to %s menu" % parent['title']

  optioncount = len(menu['options']) 
  pos=0 
  oldpos=None 
  x = None 
  
  while x !=ord('\n'):
    if pos != oldpos:
      oldpos = pos
      screen.border(0)
      if menu[EXT] == 'body':
        screen.addstr(2,2, menu['body'], curses.A_STANDOUT)
      else:
        screen.addstr(2,2, menu['title'], curses.A_STANDOUT) 
      screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) 
      for index in range(optioncount):
        textstyle = n
        if pos==index:
          textstyle = h
        screen.addstr(5+index,4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
      textstyle = n
      if pos==optioncount:
        textstyle = h
      screen.addstr(5+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
      screen.refresh()
      
    x = screen.getch() 
    
    if x >= ord('1') and x <= ord(str(optioncount+1)[0]):
      pos = x - ord('0') - 1 
    elif x == 258: 
      if pos < optioncount:
        pos += 1
      else: pos = 0
    elif x == 259: 
      if pos > 0:
        pos += -1
      else: pos = optioncount

  return pos


#Selected checker
def processmenu(menu, parent=None):

  optioncount = len(menu['options'])
  exitmenu = False
  while not exitmenu:
    getin = runmenu(menu, parent)
    if getin == optioncount:
        exitmenu = True
    elif menu['options'][getin]['type'] == MENU:
          screen.clear()
          if menu['options'][getin][EXT] ==  'messages':
            menu['options'][getin]['options'] = messageChecker.organizeMess(menu['options'][getin]['ID'])
          processmenu(menu['options'][getin], menu)
          screen.clear()
    elif menu['options'][getin]['type'] == EXITMENU:
          exitmenu = True
    elif menu['options'][getin]['type'] == MID:
      x = None
      screen.clear()
      messages = messageChecker.readMess(menu['options'][getin]['ID'])
      fi = ''
      for mess in messages:
        mess = mess.encode('ascii', 'ignore').decode('ascii')
        fi += mess + '\n\n'
      screen.addstr(2,2, fi, curses.A_STANDOUT) 
      while x !=ord('\n'):
        x = screen.getch()
      screen.clear()

# Main program
fillMenu(menu_data)
processmenu(menu_data)
curses.endwin()
os.system('clear')
