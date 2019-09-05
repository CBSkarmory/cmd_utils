#!/usr/bin/env python3

import sys

def err(error_code, error_message):
    print(f"[ERROR] {error_message}")
    sys.exit(error_code)

if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    if argc != 3:
        err(-1, "Expected 2 arguments: int, str")
    delta = argv[1]
    s = argv[2]
    shift = [chr(ord(c) + int(delta)) for c in s]
    print("".join(shift))
