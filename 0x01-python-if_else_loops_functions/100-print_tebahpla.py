#!/usr/bin/python3
for ch in range(65+25, 64, -1):
    print(f"{chr(ch + 32 if (ch % 2 == 0) else ch)}", end="")
