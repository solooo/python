#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def yang():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
y = yang()
for i in range(10):
    print(next(y))
