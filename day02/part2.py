#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    memory = list(map(int, sys.stdin.readline().strip().split(",")))
    
    computer = memory

    # Trial and Error LMAO
    computer[1] = 40
    computer[2] = 19

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