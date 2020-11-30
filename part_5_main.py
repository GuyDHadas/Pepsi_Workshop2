import numpy as np
import matplotlib.pyplot as plt
from part_2_main import *
from part_3_main import *
from euler_rocket import *

x_0 = 0
y_0 = 0
dt = 0.0001
v_0 = 350
theta0 = 50
friction = 0.0003348


def part_five_hit_location(theta, x_0):
    x_array, y_array = kassam_in_air(dt, x_0, y_0, v_0 * np.cos(theta * np.pi / 180),
                                     v_0 * np.sin(theta * np.pi / 180), friction)
    return x_array[-1]


def find_minimal_distance(x_0_first, theta_0_first, x_0_second, theta_0_second):
    x_array_first, y_array_first = kassam_in_air(dt, x_0_first, y_0, v_0 * np.cos(theta_0_first * np.pi / 180),
                                     v_0 * np.sin(theta_0_first * np.pi / 180), friction)
    x_array_second, y_array_second = kassam_in_air(dt, x_0_second, y_0, v_0 * np.cos(theta_0_second * np.pi / 180),
                                     v_0 * np.sin(theta_0_second * np.pi / 180), friction)
    distanve
    for i in range(min(len(x_array_first), len(x_array_second))):
        distances =



