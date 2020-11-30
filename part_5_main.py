import numpy as np
import matplotlib.pyplot as plt
from part_2_main import *
from part_3_main import *
from part_4_main import *
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


def find_minimal_distance(x_0_first, theta_0_first, x_0_second, theta_0_second,friction_first,friction_second):
    x_array_first, y_array_first = kassam_in_air(dt, x_0_first, y_0, v_0 * np.cos(theta_0_first * np.pi / 180),
                                     v_0 * np.sin(theta_0_first * np.pi / 180), friction_first)
    x_array_second, y_array_second = kassam_in_air(dt, x_0_second, y_0, v_0 * np.cos(theta_0_second * np.pi / 180),
                                     v_0 * np.sin(theta_0_second * np.pi / 180), friction_second)
    distances = []
    for i in range(min(len(x_array_first), len(x_array_second))):
        distances.append((x_array_first[i] - x_array_second[i])**2 + (y_array_first[i] - y_array_second[i])**2)
    return min(distances)


def min_distance_kassam(theta, prenct):
    x,y=kassam_in_air(dt,x_0,y_0,v_0 * np.cos(theta0 * np.pi / 180),
                                     v_0 * np.sin(theta0 * np.pi / 180),friction)
    #print(x[-1])
    loc=0.75*x[-1]
    #print(loc)
    return find_minimal_distance(x_0,theta0,loc,theta,friction,friction*prenct)


def part_five_secant_iteration(theta_n_minus_1, theta_n, f_n_minus_1, f_n):
    theta_n_plus_1 = theta_n - f_n * (theta_n - theta_n_minus_1) / (f_n - f_n_minus_1)
    return theta_n_plus_1


def part_5_secant_loop(prenct):
    theta_n_minus_1 = 110
    theta_n = 170
    f_values = [min_distance_kassam(theta_n_minus_1, prenct), min_distance_kassam(theta_n, prenct)]
    n = 1
    while np.abs(theta_n - theta_n_minus_1) > 0.01:
        theta_n_plus_1 = part_five_secant_iteration(theta_n_minus_1, theta_n, f_values[n-1], f_values[n])
        theta_n_minus_1 = theta_n
        theta_n = theta_n_plus_1
        f_values.append(min_distance_kassam(theta_n))
        n += 1
    return theta_n


def visual():
    theta=part_5_secant_loop()
    x, y = kassam_in_air(dt, x_0, y_0, v_0 * np.cos(theta0 * np.pi / 180),
                         v_0 * np.sin(theta0 * np.pi / 180), friction)
    x_tag,y_tag=kassam_in_air(dt,x_0,y_0,v_0 * np.cos(theta * np.pi / 180),
                                     v_0 * np.sin(theta * np.pi / 180),friction)
    distances = []
    for i in range(min(len(x), len(x_tag))):
        distances.append((x_tag[i] - x_tag[i]) ** 2 + (y[i] - y_tag[i]) ** 2)
    index=np.mask_indices(distances)
    x=x[0:index]
    y=y[0:index]
    x_tag=x_tag[0:index]
    y_tag=y_tag[0:index]
    plt.plot(x, y)
    plt.plot(x_tag,y_tag)
    plt.legend(['kassam','kipat barzel'])
    plt.xlabel(r'$x$  [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$y$  [$\mathrm{m}$]', size=15)
    plt.title("Part 5- visual")
    plt.grid()
    plt.show()
visual()

def sanity_check():
    print(part_5_secant_loop(1)) # we expect to get the same angel (50 degrees)