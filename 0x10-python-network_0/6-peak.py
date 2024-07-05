#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_nums):
    """Return a peak in a list of unsorted integers."""
    if list_nums == []:
        return None

    length = len(list_nums)
    if length == 1:
        return list_nums[0]
    elif length == 2:
        return max(list_nums)

    m = int(length / 2)
    peak = list_nums[m]
    if peak > list_nums[m - 1] and peak > list_nums[m + 1]:
        return peak
    elif peak < list_nums[m - 1]:
        return find_peak(list_nums[:m])
    else:
        return find_peak(list_nums[m + 1:])
