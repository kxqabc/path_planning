#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


PLOT_COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')


def plot_2d_points(points, labels=None):
    figure = plt.figure()
    ax = figure.add_subplot(111, aspect='equal')
    # labels为points对应的分类标记
    if labels is not None:
        label_dict = dict()
        for i, label in enumerate(labels):
            if label in label_dict.keys():
                label_dict[label].append(i)
            else:
                label_dict[label] = [i, ]
        for i, indexs in enumerate(label_dict.values()):
            ax.scatter(points[indexs, 0], points[indexs, 1], c=PLOT_COLORS[i])
    else:
        ax.scatter(points[:, 0], points[:, 1], c=PLOT_COLORS[0])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # plt.savefig("./pic/2d_points.png")
    plt.show()