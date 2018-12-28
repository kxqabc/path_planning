#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

class ArrtWithIndex(object):
    index = 0

    def __init__(self, data=None):
        self.data = data
        self.index = ArrtWithIndex.index
        ArrtWithIndex.index += 1


class ClustersPerformanceItem(object):
    def __init__(self):
        self.cluster_name = ArrtWithIndex()
        self.n_cluster = ArrtWithIndex()
        self.distance = ArrtWithIndex()
        self.distances = ArrtWithIndex()
        self.avg_distance = ArrtWithIndex()
        self.variance = ArrtWithIndex()
        self.max = ArrtWithIndex()
        self.min = ArrtWithIndex()

    def to_list(self):
        val_list = ["" for _ in range(len(self.__dict__))]
        for key, val in self.__dict__.items():
            index = val.index
            val_list[index] = val.data
        return val_list