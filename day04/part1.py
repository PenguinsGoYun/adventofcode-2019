#!/usr/bin/env python3

import sys

def check_adjacent_digits(n):

    n = str(n)

    for i in range(len(n) - 1):
        if int(n[i]) == int(n[i+1]):
            return True

    return False

def check_increasing_digits(n):
    
    n = str(n)

    for i in range(len(n) - 1):
        if int(n[i]) > int(n[i+1]):
            return False
    
    return True

if __name__ == "__main__":
    for line in sys.stdin:
        start, end = map(int, line.strip().split('-'))

        count = 0

        for n in range(start, end + 1):
            if not check_adjacent_digits(n):
                continue
            elif not check_increasing_digits(n):
                continue
            else:
                count += 1
        
        print(count)