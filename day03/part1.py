#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    path0 = sys.stdin.readline().strip().split(',')
    path1 = sys.stdin.readline().strip().split(',')

    x = 0
    y = 0

    a = []
    for direction in path0:
        value = int(direction[1:])
        if direction[0] == 'R':
            a.append(((x, y), (x + value, y)))
            x += value
        elif direction[0] == 'L':
            a.append(((x, y), (x - value, y)))
            x -= value
        elif direction[0] == 'U':
            a.append(((x, y), (x, y + value)))
            y += value
        elif direction[0] == 'D':
            a.append(((x, y), (x, y - value)))
            y -= value
    
    x = 0
    y = 0
    
    b = []
    for direction in path1:
        value = int(direction[1:])
        if direction[0] == 'R':
            b.append(((x, y), (x + value, y)))
            x += value
        elif direction[0] == 'L':
            b.append(((x, y), (x - value, y)))
            x -= value
        elif direction[0] == 'U':
            b.append(((x, y), (x, y + value)))
            y += value
        elif direction[0] == 'D':
            b.append(((x, y), (x, y - value)))
            y -= value

    intersections = []

    for coords_a in a:
        # x-coords differ
        if coords_a[0][1] == coords_a[1][1]:
            for coords_b in b:
                if (coords_b[0][0] == coords_b[1][0]) \
                and ((coords_a[0][0] <= coords_b[0][0] and coords_b[0][0] <= coords_a[1][0]) or (coords_a[1][0] <= coords_b[0][0] and coords_b[0][0] <= coords_a[0][0])) \
                and ((coords_b[0][1] <= coords_a[0][1] and coords_a[0][1] <= coords_b[1][1]) or (coords_b[1][1] <= coords_a[0][1] and coords_a[0][1] <= coords_b[0][1])):
                    intersections.append( (coords_b[0][0], coords_a[0][1]) )

        # y-coords differ
        elif coords_a[0][0] == coords_a[1][0]:
            for coords_b in b:
                if (coords_b[0][1] == coords_b[1][1]) \
                and ((coords_a[0][1] <= coords_b[0][1] and coords_b[0][1] <= coords_a[1][1]) or (coords_a[1][1] <= coords_b[0][1] and coords_b[0][1] <= coords_a[0][1])) \
                and ((coords_b[0][0] <= coords_a[0][0] and coords_a[0][0] <= coords_b[1][0]) or (coords_b[1][0] <= coords_a[0][0] and coords_a[0][0] <= coords_b[0][0])):
                    intersections.append( (coords_a[0][0], coords_b[0][1]) )

    # print(intersections)

    total = float('inf')
    for intersection in intersections[1:]:
        if total > sum( [abs(intersection[0]), abs(intersection[1])] ):
            total = sum( [abs(intersection[0]), abs(intersection[1])] )
    
    print(total)