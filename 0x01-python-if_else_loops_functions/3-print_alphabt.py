#!/usr/bin/python3
for ch in range(26):
    if ch != 4 and ch != 16: # ignore for e and q
        print("{:s}".format(chr(ch + ord('a'))), end="")
