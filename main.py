#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from utils.data_util import get_date_from_tsp
from utils.plot_util import plot_2d_points
from enlighten.annealing import anneal, cal_distence, disturbance_func
from cluster.cluster import cluster_by_kmeans, cluster_by_spectral, cluster_by_affinity


if __name__ == '__main__':
    points_info, points = get_date_from_tsp('./data', 'att48.tsp')
    print points.shape
    print points
    print points_info
    # min_points, cost_list = anneal(cal_distence, disturbance_func, points, disturbance_num=50, attenuation_rate=0.99)
    # plt.plot(cost_list)
    # plt.show()
    labels = cluster_by_affinity(points)
    plot_2d_points(points, labels=labels)