#!/usr/bin/env python3

import sys as s

if __name__ == "__main__":
    i: int = 1
    print("=== Command Quest ===")
    print(f"Program name: {s.argv[0]}")
    if len(s.argv) < 2:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(s.argv) - 1}")
        while i < len(s.argv):
            print(f"Argument {i}: {s.argv[i]}")
            i += 1
    print(f"Total arguments: {len(s.argv)}\n")
