#!/usr/bin/env python3
from typing import List


def cycleme(ans: List, start: List, end: List):
    """
    For the following transformation:
    1 2 3 4 5  = star
    2 5 4 3 1  = end
    and first ans is [first_element]
    method must return 1, 2, 5
    """
    trans = end[ans[-1]-1]
    if trans in ans:
        return ans
    else: 
        ans.append(trans) 
        cycleme(ans, start, end)
    return ans

def notation(start: List, end: List):
    """
    Returns transformation on cycle notation
    """
    if len(start) != len(end):
        print("Length of array don't match")
        return 1
  
    if start != list(range(1, len(start)+1)):
        print("First array must be ordered from 1 to n")
        return 1

    if set(end) != set(list(range(1, len(start)+1))):
        print("Second array must contain all numbers from 1 to n")
        return 1

    print("Original transformation")
    print([start, end])
    print()
    cycles = []
    for elem in start:
        if elem in [value for sublist in cycles for value in sublist]:
            continue
        ans = cycleme([elem], start, end)
        cycles.append(ans)
    print("Cycle notation transformation")
    print(cycles)
    return 0


start = list(map(int, input().split(",")))
end = list(map(int, input().split(",")))
notation(start, end)
