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