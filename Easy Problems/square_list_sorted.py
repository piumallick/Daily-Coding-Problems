#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:52:44 2020

@author: piumallick
"""

# Daily Coding Problem: Problem #118 [Easy]

"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and 
give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def sqaure_list_sorted(nums):
    return sorted([nums[i] ** 2 for i in range(len(nums))])


# Testing

arr1 = [-9, -2, 0, 2, 3]
print(sqaure_list_sorted(arr1))
# Output -> [0, 4, 4, 9, 81]

arr2 = [-9, -8, -7, 0, -2]
print(sqaure_list_sorted(arr2))
# Output -> [0, 4, 49, 64, 81]


# Time Complexity -> O(n) - Linear Scan
# Space Complexity -> O(1) - In-place Calculation & Sorting
