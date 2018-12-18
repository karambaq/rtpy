import numpy as np
import random

cos = np.cos
sin = np.sin


def create_matrix(mat_type='rotation',
                  angle=None,
                  axis=None,
                  reflect_axis=None,
                  mx=None, my=None, mz=None,
                  tx=None, ty=None, tz=None,
                  direction=None,
                  alpha=None,
                  beta=None):
    d = direction
    if mat_type == 'rotation':
        if axis == 'x':
            mat = np.array([
                [1, 0,          0,           0],
                [0, cos(angle), -sin(angle), 0],
                [0, sin(angle), cos(angle),  0],
                [0, 0,          0,           1]
            ]
            )
        elif axis == 'y':
            mat = np.array([
                [cos(angle),  0, sin(angle), 0],
                [0,           1, 0,          0],
                [-sin(angle), 0, cos(angle), 0],
                [0,           0, 0,          1]
            ]
            )
        elif axis == 'z':
            mat = np.array([
                [cos(angle), -sin(angle), 0, 0],
                [sin(angle), cos(angle),  0, 0],
                [0,          0,           1, 0],
                [0,          0,           0, 1]
            ]
            )
    if mat_type == 'scale':
        if d == 1:
            mat = np.array([
                [mx, 0,  0,  0],
                [0, my, 0,  0],
                [0, 0,  mz, 0],
                [0, 0,  0,  1],
            ]
            )
        else:
            mat = np.array([
                [1 / mx, 0,      0,      0],
                [0,      1 / my, 0,      0],
                [0,      0,      1 / mz, 0],
                [0,      0,      0,      1],
            ]
            )

    if mat_type == 'reflection':
        mat = np.array([
            [-1 if axis == 'x' else 1, 0, 0, 0],
            [0, -1 if axis == 'y' else 1, 0, 0],
            [0, 0, -1 if axis == 'z' else 1, 0],
            [0, 0, 0, 1]
        ]
        )
    if mat_type == 'translation':
        mat = np.array([
            [1, 0, 0, d * tx],
            [0, 1, 0, d * ty],
            [0, 0, 1, d * tz],
            [0, 0, 0,      1]
        ]
        )
    if mat_type == 'perspective':
        mat = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, .4],
            [0, 0, 0, 1]
        ]
        )
    if mat_type == 'orto':
        if axis == 'z':
            mat = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]
            ]
            )
        elif axis == 'y':
            mat = np.array([
                [1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]
            )
        elif axis == 'x':
            mat = np.array([
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]
            )

    return mat
