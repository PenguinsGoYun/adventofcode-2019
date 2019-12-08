#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    total = 0

    for line in sys.stdin:
        mass = int(line.strip())
        
        total += (mass // 3) - 2

    
    print(total)
