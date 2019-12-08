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
    
    print(intersections)
    # 1192, -569

    # print(a)
    # print(b)

    print(len(intersections))
    
    min_steps = float('inf')

    for intersection in intersections[1:]:
        x, y = intersection
        print("x: {} y: {}".format(x, y))
        print()

        steps_a = 0
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        for i in range(len(a)):
            if i:
                start_x = a[i-1][1][0]
                start_y = a[i-1][1][1]
            end_x = a[i][1][0]
            end_y = a[i][1][1]

            print("({}, {})".format(start_x, start_y))
            print("({}, {})".format(end_x, end_y))

            if ((start_x <= x and x <= end_x) or (end_x <= x and x <= start_x)) and ((start_y <= y and y <= end_y) or (end_y <= y and y <= start_y)):
                if start_x == end_x:
                    steps_a += abs(start_y - y)
                else:
                    steps_a += abs(start_x - x)
                print("steps_a: " + str(steps_a))
                break
            else:
                if start_x == end_x:
                    steps_a += abs(start_y - end_y)
                else:
                    steps_a += abs(start_x - end_x)

            print("steps_a: " + str(steps_a))

        steps_b = 0
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0

        for i in range(len(b)):
            if i:
                start_x = b[i-1][1][0]
                start_y = b[i-1][1][1]
            end_x = b[i][1][0]
            end_y = b[i][1][1]
            print("({}, {})".format(start_x, start_y))
            print("({}, {})".format(end_x, end_y))

            if ((start_x <= x and x <= end_x) or (end_x <= x and x <= start_x)) and ((start_y <= y and y <= end_y) or (end_y <= y and y <= start_y)):
                if start_x == end_x:
                    steps_b += abs(start_y - y)
                else:
                    steps_b += abs(start_x - x)
                    print("steps_b: " + str(steps_b))
                break
            else:
                if start_x == end_x:
                    steps_b += abs(start_y - end_y)
                else:
                    steps_b += abs(start_x - end_x)

            print("steps_b: " + str(steps_b))

        steps = steps_a + steps_b
        print("steps: " + str(steps))

        if steps < min_steps:
            min_steps = steps

    print()
    print(min_steps)

    print(a)
    print(b)

    print()
    print(intersections)

    print(total)