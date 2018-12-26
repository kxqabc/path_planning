#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster as sc

from cluster.cluster import get_labels, divide_points
from search_path.annealing import anneal
import search_path.path_tools


def cluster_performance(points, cluster, search_func, **kwargs):
    result_dict = dict()
    labels = get_labels(points, cluster)
    divided_dict = divide_points(points, labels)
    for label, divided_point in divided_dict.items():
        search_result = search_func(divided_point, **kwargs)
        result_dict[label] = search_result
    return result_dict


def log_min_cost(result):
    min_cost_list = []
    for label, result_dict in result.items():
        min_cost, _ = result_dict.get('min')
        min_cost_list.append(min_cost)
        print "[result_info]: label%d cluster's min cost: %s" % (label, str(min_cost))
    min_cost_list = np.asarray(min_cost_list)
    var = np.var(min_cost_list)
    print "方差为：%f" % var


def kmeans_performance(points, cluster_nums=1):
    if cluster_nums < 1:
        raise ValueError("cluster_nums is invalid!")
    for i in range(1, cluster_nums):
        kmeans_cluster = sc.KMeans(n_clusters=i)
        search_kwargs = {
            'disturbance_num': 200,
            'attenuation_rate': 0.99,
        }
        result = cluster_performance(points, kmeans_cluster, anneal, **search_kwargs)
        log_min_cost(result)