#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from utils.data_util import get_date_from_tsp
from utils.plot_util import plot_2d_points, plot_path, plot_path_new
from enlighten.annealing import anneal, euclidean_distance, swap, reverse, transpose
from cluster.cluster import cluster_by_kmeans, divide_points


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


def test_cluster(points):
    labels = cluster_by_kmeans(points, cluster_num=3)
    label_dict = divide_points(points, labels)
    plot_2d_points(points, labels=label_dict)
    figure = plt.figure()
    ax = figure.add_subplot(111)
    dist_sum = 0.0
    for index, divided_points in label_dict.items():
        min_points, cost_list, intermediate_points = anneal(euclidean_distance, divided_points,
                                                            disturbance_num=200,
                                                            attenuation_rate=0.99)
        dist_sum += cost_list.pop()
        # print "len of cost list: %d" % len(cost_list)
        # ax.plot(cost_list, color='red', linestyle='--')
        plot_path_new(ax, min_points, index)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(u"聚类处理后的多艘无人船路径规划结果图")
    plt.savefig('./pic/multi_path.png')
    # print "sum distence: %.2f" % dist_sum
    # min_points, cost_list, intermediate_points = anneal(euclidean_distance, points,
    #                                                     disturbance_num=200,
    #                                                     attenuation_rate=0.99)
    # print "min distence: %.2f" % cost_list[-1]
    # ax.plot(cost_list[:-50], color='blue', linestyle='--')
    # plt.rcParams['font.sans-serif'] = ['SimHei']
    # plt.title(u"非聚类(蓝)与聚类(红)处理后的收敛效果图")
    # plt.savefig('./pic/static.png')
    # plt.show()


if __name__ == '__main__':
    points_info, points = get_date_from_tsp('./data', 'att48.tsp')
    # print points.shape
    # print points
    # print points_info
    # min_points = test_anneal(points)
    # test_cluster(points)