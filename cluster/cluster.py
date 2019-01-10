#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans, SpectralClustering, AffinityPropagation
from item.entity import ClusterItem


def get_cluster_result(points, cluster):
    cluster.fit(points)
    labels = cluster.labels_
    centers = cluster.cluster_centers_
    result_dict = {
        'labels': labels,
        'centers': centers
    }
    return result_dict


def divide_points(points, labels, centers):
    clusters = []
    label_dict = dict()
    for i, label in enumerate(labels):
        if label in label_dict.keys():
            label_dict[label].append(i)
        else:
            label_dict[label] = [i, ]
    for k, v in label_dict.items():
        cluster = ClusterItem(np.copy(points[v]), k, centers[k])
        clusters.append(cluster)
    return clusters


def get_point_clusters(points, cluster):
    result_dict = get_cluster_result(points, cluster)
    point_clusters = divide_points(points, result_dict['labels'], result_dict['centers'])
    return point_clusters


if __name__ == '__main__':
    data = np.random.rand(100, 2)
    print "shape: " + str(data.shape)
    print "data: " + str(data)
    estimator = KMeans(n_clusters=3)  # 构造聚类器
    estimator.fit(data)  # 聚类
    label_pred = estimator.labels_  # 获取聚类标签
    print "labels len: %d" % len(label_pred)
    print "labels: " + str(label_pred)
    centroids = estimator.cluster_centers_  # 获取聚类中心
    print "centroids: " + str(centroids)
    inertia = estimator.inertia_  # 获取聚类准则的总和
    print "inertia: " + str(inertia)