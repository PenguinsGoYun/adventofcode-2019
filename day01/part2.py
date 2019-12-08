#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    total = 0

    for line in sys.stdin:
        mass = int(line.strip())
        
        while mass > 0:
            mass = (mass // 3) - 2
            if mass > 0:
                total += mass
    
    print(total)
