#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster as sc

from utils.data_util import get_date_from_tsp, save_excel
from utils.plot_util import plot_2d_points, plot_path, colour, save
from search_path.annealing import anneal
from search_path.path_tools import euclidean_distance
from cluster.cluster import divide_points, get_labels
from test.statistics import cluster_performance, log_min_cost
from item.statistics_item import ClustersPerformanceItem


def test_anneal(points):
    min_points, cost_list, intermediate_points = anneal(euclidean_distance, points,
                                                        disturbance_num=200,
                                                        attenuation_rate=0.99)
    print "min_cost: %s" % str(cost_list.pop())
    plt.plot(cost_list)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u"循环次数-总路径长度 统计图")
    print "len of cost list: %d" % len(cost_list)
    plt.savefig('./pic/anneal.png')
    # for k, v in intermediate_points.items():
    #     plot_path(v, str(k), title=u'第%d次循环,路径总长度=%.2f' % (200*k, cost_list[k]))
    return min_points


def test_kmean_cluster(points, axes):
    kmeans_cluster = sc.KMeans(n_clusters=2)
    labels = get_labels(points, kmeans_cluster)
    label_dict = divide_points(points, labels)
    for label, divided_points in label_dict.items():
        plot_2d_points(divided_points, axes, color=colour(label), title=u"Kmeans")


def test_meanshift_cluster(points, axes):
    bandwidth = sc.estimate_bandwidth(points, n_samples=len(points), quantile=0.2)
    print "bandwidth: %f" % bandwidth
    meanshift_cluster = sc.MeanShift(bandwidth=bandwidth, seeds=np.asarray([[7000, 3000], [3000, 2000]]), bin_seeding=True)
    labels = get_labels(points, meanshift_cluster)
    label_dict = divide_points(points, labels)
    for label, divided_points in label_dict.items():
        plot_2d_points(divided_points, axes, color=colour(label), title=u"mean shift")
    save('meanshift')


if __name__ == '__main__':
    points_info, points = get_date_from_tsp('./data', 'att48.tsp', 3)
    # print points.shape
    # print points
    # print points_info
    # min_points = test_anneal(points)
    # test_cluster(points)

    # index_info, index_array = get_opt_result('./data', 'att48.opt.tour', 1)
    # index_array = np.reshape(index_array, index_array.shape[0])
    # index_list = index_array.tolist()
    # index_list = [int(index) - 1 for index in index_list[:-1]]
    # print index_list
    # plot_path(points[index_list, :], 'best')
    # print points[index_list[1:13]]
    # distence = euclidean_distance(points[index_list[2:19], :])
    # print distence

    # figure = plt.figure()
    # axes1 = figure.add_subplot(211)
    # axes2 = figure.add_subplot(212)
    # kmeans_cluster = sc.KMeans(n_clusters=2)
    # anneal_kwargs = {
    #     'disturbance_num': 200,
    #     'attenuation_rate': 0.99,
    # }
    # result = cluster_performance(points, kmeans_cluster, anneal, **anneal_kwargs)
    # log_min_cost(result)
    items = ClustersPerformanceItem()
    items.cluster_name.data = "k means"
    val_list = items.to_list()
    print val_list