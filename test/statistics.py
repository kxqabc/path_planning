#!/usr/bin/python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster as sc

from search_path.annealing import anneal
from cluster.cluster import get_cluster_result, divide_points
from item.entity import ClustersPerformanceItem


def cluster_performance(points, cluster, search_func, **kwargs):
    result_dict = dict()
    cluster_res_dict = get_cluster_result(points, cluster)
    labels = cluster_res_dict['labels']
    divided_dict = divide_points(points, labels)
    for label, divided_point in divided_dict.items():
        search_result = search_func(divided_point, **kwargs)
        result_dict[label] = search_result
    return result_dict


def log_to_item(result, cluster_name='default'):
    n_cluster = len(result)
    min_cost_list = []
    for label, result_dict in result.items():
        min_cost, _ = result_dict.get('min')
        min_cost_list.append(min_cost)
    min_cost_list = np.asarray(min_cost_list)
    item = ClustersPerformanceItem(cluster_name, n_cluster, np.sum(min_cost_list),
                                   min_cost_list, np.mean(min_cost_list), np.var(min_cost_list),
                                   np.max(min_cost_list), np.min(min_cost_list))

    return item


def kmeans_performance(points, cluster_nums=1):
    if cluster_nums < 1:
        raise ValueError("cluster_nums is invalid!")
    data_list = []
    for i in range(1, cluster_nums + 1):
        kmeans_cluster = sc.KMeans(n_clusters=i)
        search_kwargs = {
            'disturbance_num': 200,
            'attenuation_rate': 0.99,
        }
        result = cluster_performance(points, kmeans_cluster,
                                     anneal, **search_kwargs)
        item = log_to_item(result, cluster_name='Kmeans')
        data_list.append(item.to_str_list())
    return data_list