from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
import cameratransform as ct
import collections
from solid import *
from solid.utils import *
import math


scale_factor = 1.0


Point = collections.namedtuple("Point", ["x", "y", "z"])


def rectalinear_prism_to_vertices(w, l, h):
    x = -h
    y = w
    z = l
    return [
        [-x / 2, -y / 2, 0],
        [x / 2, -y / 2, 0],
        [x / 2, y / 2, 0],
        [-x / 2, y / 2, 0],
        [-x / 2, -y / 2, z],
        [x / 2, -y / 2, z],
        [x / 2, y / 2, z],
        [-x / 2, y / 2, z],
    ]


def vertices_to_polyhedron(vertices):
    faces = [
        [0, 1, 2, 3],  # bottom
        [4, 5, 1, 0],  # front
        [7, 6, 5, 4],  # top
        [5, 6, 2, 1],  # right
        [6, 7, 3, 2],  # back
        [7, 4, 0, 3],  # left
    ]
    print(vertices)

    return polyhedron(vertices, faces)


def lines_to_rotation(p1, p2):
    return math.atan((p1[0] - p2[0]) / (p1[1] - p2[1]))


def unfold_polyhedron(vertices, dxf):
    bottom = polygon
    dotted_line


def ames_transform(point, w):
    u = 15
    l = 21
    y = 10
    projection_point = np.append(np.array(point), 1)
    print(projection_point)

    transform = np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, (-2 / (w + 2 * l)), -1 / u, 1 + l / u - w / (w + 2 * l)],
        ]
    )
    # transform = transform.transpose()
    result = transform.dot(projection_point)
    scale = result.tolist()[3]
    print(scale)
    result = result / scale
    return result.tolist()[0:3]


width = 16.0
length = 10.0
height = 8.0

point_list = rectalinear_prism_to_vertices(width, length, height)
transformed_points = []
for p in point_list:
    transformed_points.append(ames_transform(p, width))

rectalinear_prism = vertices_to_polyhedron(point_list)
rectalinear_prism = translate([width * 2, 0, 0])(rectalinear_prism)
ames_room = vertices_to_polyhedron(transformed_points)

compare = cube()
compare = ames_room  # + rectalinear_prism

scad_render_to_file(compare, include_orig_code=True)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

for p in transformed_points:
    ax.scatter(p[0], p[1], p[2])


# plt.show()
