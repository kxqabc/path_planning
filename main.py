#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as plt

import config
from cluster.cluster import get_point_clusters
from test.plot import plot_clusters_path
from utils.data_util import get_date_from_tsp, save_excel


if __name__ == '__main__':
    points_info, points = get_date_from_tsp(config.DATA_PATH, 'att48.tsp', 3)
    kmean_cluster = sc.KMeans(n_clusters=3)
    point_clusters = get_point_clusters(points, kmean_cluster)

    figure = plt.figure()
    axes1 = figure.add_subplot(111)
    plot_clusters_path(point_clusters, axes1)
    plt.show()