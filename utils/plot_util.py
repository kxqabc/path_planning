#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


PLOT_COLORS = ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')

plt.rcParams['font.sans-serif'] = ['SimHei']


def set_axes_info(axes, title, xlabel, ylabel):
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    if title:
        axes.set_title(title)
    return axes


def colour(label):
    label = abs(label) % len(PLOT_COLORS)
    color = PLOT_COLORS[label]
    return color


def plot_2d_points(points, axes, color=PLOT_COLORS[0], title=None, xlabel='X', ylabel='Y'):
    axes.scatter(points[:, 0], points[:, 1], c=color)
    return set_axes_info(axes, title, xlabel, ylabel)


def plot_path(points, axes, title=None, color=PLOT_COLORS[0], xlabel='X', ylabel='Y'):
    axes.plot(points[:, 0], points[:, 1], c=color, linewidth=1)
    return set_axes_info(axes, title, xlabel, ylabel)


def save(file_name):
    base_path = './pic/'
    plt.savefig(base_path + file_name + '.png')