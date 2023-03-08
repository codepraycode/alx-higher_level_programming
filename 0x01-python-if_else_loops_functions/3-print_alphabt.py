#!/usr/bin/python3
for ch in range(26):
  # ignore for e and q
  if ch == 4 or ch == 16: continue
  print("{:s}".format(chr(ch + ord('a'))), end="")
