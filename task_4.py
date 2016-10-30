#!/usr/bin/env python3

check = False
for i in range(11, 100000, 11):
    for j in range(2, 11):
        check = True if i % j == 1 else False
        if check is False:
            break
    if check:
        print(i)

