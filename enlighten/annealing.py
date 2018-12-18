#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import copy


def cost_func(points):
    pass


def disturbance_func(points):
    pass


def accept_by_chance(delat_e, temperature):
    pass


def anneal(cost_func, disturbance_func, points, t_init=100, alpha=1, t_min=0.05, disturbance_num=100, attenuation_rate=0.9):
    t = float(t_init)
    curr_cost = 0
    cost_list = []
    min_cost = sys.maxint
    origin_points = copy.deepcopy(points)
    

    while t > t_min:
        for _ in range(disturbance_num):
            '''随机扰动disturbance_num次'''
            dist_cost, dist_points = disturbance_func(origin_points)
            if dist_cost <= min_cost:
                origin_points = dist_cost
                min_cost = dist_cost
                curr_cost = min_cost
            else:
                is_accept = accept_by_chance(dist_cost - curr_cost, t)
                if is_accept:
                    origin_points = dist_cost
                    curr_cost = dist_cost
        # 温度下降
        t *= attenuation_rate
        cost_list.append(curr_cost)
    
    return origin_points, cost_list