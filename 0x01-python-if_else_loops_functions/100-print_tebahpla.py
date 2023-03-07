#!/usr/bin/python3
def run_main():
    for ch in range(65+25, 64, -1):
        print(chr(ch + 32 if (ch % 2 == 0) else ch), end="")


if __name__ == "__main__":
    run_main()
