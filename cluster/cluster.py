#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans, SpectralClustering, AffinityPropagation


def get_labels(points, cluster):
    cluster.fit(points)
    labels = cluster.labels_
    return labels


def divide_points(points, labels):
    label_dict = dict()
    for i, label in enumerate(labels):
        if label in label_dict.keys():
            label_dict[label].append(i)
        else:
            label_dict[label] = [i, ]
    for k, v in label_dict.items():
        label_dict[k] = np.copy(points[v])
    return label_dict


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