#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


def euclidean_distance(points):
    sum_distance = 0.0
    length = len(points)
    for i in range(length):
        if i == length - 1:
            diff = points[i] - points[0]
        else:
            diff = points[i] - points[i + 1]
        distance = np.sqrt(np.sum(np.power(diff, 2)))
        sum_distance += distance
    return sum_distance


def default_record(index):
    if index % 10 == 0:
        return True
    return False

