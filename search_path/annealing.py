#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import copy
import random

import numpy as np
import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

from path_tools import euclidean_distance, default_record


def create_random_indexs(length, index_num):
    while True:
        index_range = range(length)
        indexs = random.sample(index_range, index_num)
        for index in indexs:
            if indexs.count(index) != 1:
                continue
        return indexs


def swap(points, cost_func=euclidean_distance):
    origin_points = np.copy(points)
    # create random index
    index1, index2 = create_random_indexs(origin_points.shape[0], 2)
    # swap
    tmp_point = np.copy(origin_points[index2])
    origin_points[index2] = origin_points[index1]
    origin_points[index1] = tmp_point
    # cal cost
    dist_cost = cost_func(origin_points)
    return dist_cost, origin_points


def reverse(points, cost_func=euclidean_distance):
    origin_points = np.copy(points)
    # create random index
    index1, index2 = create_random_indexs(origin_points.shape[0], 2)
    # reverse
    origin_points[index1: index2] = origin_points[index1: index2][::-1]
    # cal cost
    dist_cost = cost_func(origin_points)
    return dist_cost, origin_points


def transpose(points, cost_func=euclidean_distance):
    origin_points = np.copy(points)
    # create random index
    index1, index2, index3 = create_random_indexs(origin_points.shape[0], 3)
    index1, index2, index3 = sorted([index1, index2, index3])
    tmp_points = np.copy(origin_points[index1: index2])
    origin_points[index1: index1 + index3 - index2 + 1] = np.copy(origin_points[index2: index3 + 1])
    origin_points[index1 + index3 - index2 + 1: index3 + 1] = tmp_points
    # cal cost
    dist_cost = cost_func(origin_points)
    return dist_cost, origin_points


def accept_by_chance(delat_e, temperature):
    return math.exp(((-delat_e)/temperature)) > random.random()


def is_convergence(cost_list):
    convergence_len = 20
    if len(cost_list) > convergence_len:
        cost_array = np.asarray(cost_list[-convergence_len:])
        standard_deviation = np.std(cost_array)
        if standard_deviation < 0.00000001:
            return True
        else:
            return False
    else:
        return False


def anneal(points, cost_func=euclidean_distance, record_func=default_record, t_init=100, t_min=0.005, disturbance_num=100, attenuation_rate=0.99):
    t = float(t_init)
    result_dict = dict()

    origin_points = copy.deepcopy(points)
    origin_cost = cost_func(origin_points)

    min_points = origin_points
    min_cost = origin_cost

    cost_list = []
    record_list = [(origin_cost, np.copy(origin_points)), ]

    while t > t_min and not is_convergence(cost_list):
        for _ in range(disturbance_num):
            '''随机扰动disturbance_num次'''
            choice = np.random.randint(3)
            if choice == 0:
                disturb_func = swap
            elif choice == 1:
                disturb_func = reverse
            else:
                disturb_func = transpose

            dist_cost, dist_points = disturb_func(origin_points)
            delta_e = dist_cost - origin_cost
            if delta_e <= 0 or accept_by_chance(delta_e, t):
                origin_points = dist_points
                origin_cost = dist_cost
                if dist_cost <= min_cost:
                    min_points = dist_points
                    min_cost = dist_cost
        # 温度下降
        t *= attenuation_rate
        cost_list.append(min_cost)
        index = len(cost_list) - 1
        if record_func(index):
            record_list.append((min_cost, np.copy(min_points)))
    result_dict['min'] = (min_cost, np.copy(min_points))
    result_dict['record'] = record_list
    result_dict['cost_list'] = cost_list
    return result_dict


if __name__ == '__main__':
    pass