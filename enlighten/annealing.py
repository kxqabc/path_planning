#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import copy
import random

import numpy as np
import matplotlib
# matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


def cal_distence(points):
    sum_distence = 0
    for i in range(len(points) - 1):
        diff = points[i] - points[i + 1]
        distence = np.sqrt(np.sum(np.power(diff, 2)))
        sum_distence += distence
    return sum_distence


def disturbance_func(points, cost_func=cal_distence):
    origin_points = np.copy(points)
    indexs = range(origin_points.shape[0])
    index1, index2 = random.sample(indexs, 2)
    tmp_point = np.copy(origin_points[index2])
    origin_points[index2] = origin_points[index1]
    origin_points[index1] = tmp_point
    # cal cost
    dist_cost = cost_func(origin_points)
    return dist_cost, origin_points


def accept_by_chance(delat_e, temperature):
    return math.exp(((-delat_e)/temperature)) > random.random()


def anneal(cost_func, disturbance_func, points, t_init=100, alpha=1, t_min=0.005, disturbance_num=100, attenuation_rate=0.99):
    t = float(t_init)
    cost_list = []
    origin_points = copy.deepcopy(points)
    origin_cost = cost_func(origin_points)
    min_cost = origin_cost
    min_points = origin_points

    while t > t_min:
        for _ in range(disturbance_num):
            # print "origin: %s" % str(origin_points)
            '''随机扰动disturbance_num次'''
            dist_cost, dist_points = disturbance_func(origin_points)
            # print "dist: %s, %s" % (str(dist_cost), str(dist_points))
            # print "min_cost: %s" % str(min_cost)
            delta_e = dist_cost - origin_cost
            if delta_e <= 0 or accept_by_chance(delta_e, t):
                origin_points = dist_points
                origin_cost = dist_cost
                if dist_cost <= min_cost:
                    min_points = dist_points
                    min_cost = dist_cost
        # 温度下降
        t *= attenuation_rate
        cost_list.append(origin_cost)
    
    return min_points, cost_list


if __name__ == '__main__':
    points = np.random.randint(1, 100, size=(15, 1, 2))
    print points
    min_points, cost_list = anneal(cal_distence, disturbance_func, points, disturbance_num=20, attenuation_rate=0.9)
    print "cost_list:"
    print cost_list
    plt.plot(cost_list)
    plt.show()