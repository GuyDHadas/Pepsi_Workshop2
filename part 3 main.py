import numpy as np
import matplotlib.pyplot as plt
from euler_rocket import *


def kassam_in_air (dt , x_0 , y_0 , vx_0 , vy_0, friction_coefficient):
    x_n = x_0
    y_n = y_0
    vx_n = vx_0
    vy_n = vy_0
    x = []
    y = []
    while y_n > 10 ** (-9) or len(y)<2:
        x.append(x_n)
        y.append(y_n)
        x_n, y_n, vx_n, vy_n = part_three_rocket_iteration(x_n, y_n, vx_n, vy_n, dt, friction_coefficient):
    return x, y