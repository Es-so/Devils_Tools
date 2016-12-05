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



menu_data = {
  'title': "Message Checker", 'type': MENU, 'subtitle': "Please select an option...",
  'options':[
        { 'title': "Unread messages", 'type': MENU, 'subtitle': "Please select an option...",
        'options': [
          { 'title': "author", 'type': COMMAND, 'command': 'uid' },
        ]
        },
        { 'title': "Sent messages", 'type': MENU, 'subtitle': "Please select an option...",
        'options': [
          { 'title': "author", 'type': COMMAND, 'command': 'ls' },
        ]
        },
        { 'title': "Send new message", 'type': COMMAND, 'command': 'clear' },
  ]
}


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
    
    if x >= ord('1') and x <= ord(str(optioncount+1)):
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

def processmenu(menu, parent=None):

  optioncount = len(menu['options'])
  exitmenu = False
  while not exitmenu: #Loop until the user exits the menu
    getin = runmenu(menu, parent)
    if getin == optioncount:
        exitmenu = True
    # elif menu['options'][getin]['type'] == COMMAND:
    #   curses.def_prog_mode()
    #   os.system('reset')
    #   screen.clear() 
    #   os.system(menu['options'][getin]['command'])
    #   screen.clear()
    #   curses.reset_prog_mode()
    #   curses.curs_set(1)
    #   curses.curs_set(0)
    elif menu['options'][getin]['type'] == MENU:
          screen.clear()
          processmenu(menu['options'][getin], menu) # display the submenu
          screen.clear()
    elif menu['options'][getin]['type'] == EXITMENU:
          exitmenu = True

# Main program
processmenu(menu_data)
curses.endwin()
os.system('clear')












