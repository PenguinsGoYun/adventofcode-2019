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

def check_adjacent_digits_onlytwo(n):

    n = str(n)

    count = {}

    for d in n:
        count[d] = count.get(d, 0) + 1

    if 2 in count.values():
        return True
    
    return False

if __name__ == "__main__":
    for line in sys.stdin:
        start, end = map(int, line.strip().split('-'))

        passwords = []
        count = 0

        for n in range(start, end + 1):
            if not check_adjacent_digits(n):
                continue
            elif not check_increasing_digits(n):
                continue
            else:
                passwords.append(n)
        
        for n in passwords:
            if check_adjacent_digits_onlytwo(n):
                count += 1

        print(count)
