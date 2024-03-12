#!/usr/bin/python3

for i in range(90, 64, -1):
    print("{:c}".format(i if i % 2 == 1 else i + 32), end='')
