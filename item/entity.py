#!/usr/bin/python
# -*- coding: utf-8 -*-


class ClustersPerformanceItem(object):
    def __init__(self, cluster_name=None, n_cluster=None, distance=None,
                 distances=None, avg_distance=None, variance=None, max=None, min=None):
        self.cluster_name = cluster_name
        self.n_cluster = n_cluster
        self.distance = distance
        self.distances = distances
        self.avg_distance = avg_distance
        self.variance = variance
        self.max = max
        self.min = min

    def to_str_list(self):
        attr_list = [self.cluster_name, self.n_cluster, self.distance,
                     self.distances, self.avg_distance, self.variance,
                     self.max, self.min]
        return [str(attr) for attr in attr_list]


class ClusterItem(object):
    def __init__(self, points, label, center):
        self.points = points
        self.label = label
        self.center = center
        self.min_path = None
        self.min_distance = None
        self.liquid_num = 0
        self.liquid_points = None

    def __str__(self):
        show = "**** ClusterItem str ****" + '\n'
        show += "[points]: length=" + str(len(self.points)) + '\n' + str(self.points)
        show += "[label]: " + str(self.label) + '\n'
        show += "[center]: " + str(self.center) + '\n'
        if self.min_distance:
            show += "[min_distance]: " + str(self.min_distance) + '\n'
        return show

