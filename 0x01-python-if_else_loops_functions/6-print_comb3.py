#!/usr/bin/python3

for digit1 in range(99):
    for digit2 in range(digit1 + 1, 100):
        print(f"{digit1:02d} {digit2:02d}", end=", " if digit1 < 98 or digit2 < 99 else "\n")
