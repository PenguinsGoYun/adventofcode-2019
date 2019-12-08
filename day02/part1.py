#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    computer = list(map(int, sys.stdin.readline().strip().split(",")))
    
    computer[1] = 12
    computer[2] = 2

    for i in range(0, len(computer), 4):
        if computer[i] == 1:
            a = computer[computer[i+1]]
            b = computer[computer[i+2]]
            computer[computer[i+3]] = a + b
            continue
        if computer[i] == 2:
            a = computer[computer[i+1]]
            b = computer[computer[i+2]]
            computer[computer[i+3]] = a * b
            continue
        if computer[i] == 99:
            break

    print(computer[0])