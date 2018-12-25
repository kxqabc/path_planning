#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


PLOT_COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')


def plot_2d_points(points, labels=None):
    figure = plt.figure()
    ax = figure.add_subplot(111, aspect='equal')
    # labels为points对应的分类标记
    if labels is not None:
        for k, v in labels.items():
            k %= len(PLOT_COLORS)
            ax.scatter(v[:, 0], v[:, 1], c=PLOT_COLORS[k])
    else:
        ax.scatter(points[:, 0], points[:, 1], c='r')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax.set_title(u'船数已知（=3）的划分结果图')
    plt.savefig("./pic/2d_points.png")
    plt.show()


def plot_path(points, file_name, title='default'):
    figure = plt.figure()
    ax = figure.add_subplot(111, aspect='equal')
    # plot points
    ax.scatter(points[:, 0], points[:, 1], c='r')
    # plot line
    ax.plot(points[:, 0], points[:, 1], c='b', linewidth=1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax.set_title(title)
    plt.savefig("./pic/" + file_name + '.png')
    # plt.show()


def plot_path_new(axes, points, index):
    index %= len(PLOT_COLORS)
    axes.scatter(points[:, 0], points[:, 1], c=PLOT_COLORS[index])
    axes.plot(points[:, 0], points[:, 1], c=PLOT_COLORS[index], linewidth=1)
