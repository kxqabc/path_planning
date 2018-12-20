#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import numpy as np


def get_date_from_tsp(path, file_name):
    if path.endswith(os.sep):
        file_name = path + file_name
    else:
        file_name = os.sep.join((path, file_name))
    info = dict()
    points = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()     # 去除两端的空格
            if line.find(":") != -1:
                info_tag, info_content = line.split(":")
                info[info_tag] = info_content
            elif line == 'NODE_COORD_SECTION':
                pass
            elif line == 'EOF':
                break
            else:
                axes = line.split(" ")
                if len(axes) != 3:
                    continue
                points.append([float(axes[1]), float(axes[2])])
    point_array = np.asarray(points, dtype=float)
    return info, point_array
