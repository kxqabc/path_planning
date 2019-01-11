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


def set_liquid_points(cluster_items):
    sum_distance = 0.0
    points_num = 0
    for cluster_item in cluster_items:
        sum_distance += cluster_item.min_distance
        points_num += len(cluster_item.points)
    avg_distance = sum_distance/len(cluster_items)
    for cluster_item in cluster_items:
        cluster_item.liquid_num = round(points_num * (cluster_item.min_distance - avg_distance) / sum_distance)
    # for cluster_item in cluster_items:
