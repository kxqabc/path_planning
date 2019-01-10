#!/usr/bin/python
# -*- coding: utf-8 -*-

import sklearn.cluster as sc
import matplotlib.pyplot as plt

from utils.plot_util import plot_2d_points, plot_path, colour, save, PLOT_COLORS
from cluster.cluster import divide_points, get_cluster_result
from search_path.annealing import anneal
from search_path.path_tools import euclidean_distance


def plot_clusters_path(clusters, axes):
    for cluster in clusters:
        path_plan_res_dict = anneal(cluster.points, euclidean_distance, disturbance_num=200, attenuation_rate=0.99)
        cluster.min_distance = path_plan_res_dict['min'][0]
        cluster.min_path = path_plan_res_dict['min'][1]
        path_color = colour(cluster.label)
        plot_2d_points(cluster.points, axes, color=path_color, title=u"Kmeans")
        plot_path(cluster.min_path, axes, color=path_color)
        print cluster