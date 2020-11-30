import numpy as np
import matplotlib.pyplot as plt


G = 9.81


def part_one_rocket_iteration(x_n, y_n, vx_n, vy_n, dt):
    x_n1 = x_n + dt * vx_n
    y_n1 = y_n + dt * vy_n
    vx_n1 = vx_n + dt * 0
    vy_n1 = vy_n + dt * (-G)
