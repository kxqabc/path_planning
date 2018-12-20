#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans, SpectralClustering, AffinityPropagation


def cluster_by_kmeans(points, cluster_num=3):
    clustering = KMeans(n_clusters=cluster_num)
    clustering.fit(points)
    labels = clustering.labels_
    return labels


def cluster_by_spectral(points, cluster_num=3):
    clustering = SpectralClustering(n_clusters=cluster_num)
    clustering.fit(points)
    labels = clustering.labels_
    return labels


def cluster_by_affinity(points, **kwargs):
    clustering = AffinityPropagation()
    clustering.fit(points)
    labels = clustering.labels_
    return labels

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