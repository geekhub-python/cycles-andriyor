#!/usr/bin/env python3

for i in range(1, 27):
    if i % 5 == 0 and i != 0:
        print(chr(64 + i))
    else:
        print(chr(64 + i), end=' ')
