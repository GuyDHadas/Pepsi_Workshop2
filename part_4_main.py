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


def hit_location(theta):
    x_array, y_array = kassam_in_air(dt, x_0, y_0, v_0 * np.cos(theta * np.pi / 180),
                                     v_0 * np.sin(theta * np.pi / 180), friction)
    return x_array[-1]


def vis_hit_location():
    hit = []
    for theta in range(1, 90, 2):
        hit.append(hit_location(theta))
    plt.plot(range(1, 90, 2), hit)
    plt.xlabel(r'$\theta$', size=15)
    plt.ylabel(r'$x_\mathrm{{hit}}$ [$\mathrm{m}$]', size=15)
    plt.title("Part 4 - location hit as a function of the angle")
    plt.grid()
    plt.show()



def function_to_find_root(theta, x_dest):
    return x_dest - hit_location(theta)


def secant_iteration(theta_n_minus_1, theta_n, f_n_minus_1, f_n):
    theta_n_plus_1 = theta_n - f_n * (theta_n - theta_n_minus_1) / (f_n - f_n_minus_1)
    return theta_n_plus_1


def show_theta():
    x_0=hit_location(50)
    x_last=hit_location(70)
    x_lst=np.arange(x_last,x_0,abs((x_last-x_0)/20))
    theta=np.array([])
    for x in x_lst:
        theta=np.concatenate((theta,[secant_loop(x)]))
    plt.plot(x_lst, theta)
    plt.xlabel(r'$x$  [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$theta$', size=15)
    plt.title("Part 4- theta as x ")
    plt.grid()
    plt.show()


def secant_loop(x_dest):
    theta_n_minus_1 = 35
    theta_n = 89.99
    f_values = [hit_location(theta_n_minus_1), hit_location(theta_n)]
    n = 1
    while np.abs(theta_n - theta_n_minus_1) > 0.01:
        theta_n_plus_1 = secant_iteration(theta_n_minus_1, theta_n, f_values[n-1], f_values[n])
        theta_n_minus_1 = theta_n
        theta_n = theta_n_plus_1
        f_values.append(function_to_find_root(theta_n, x_dest))
        n += 1
    return theta_n


if __name__ == '__main__':
    show_theta()
    #vis_hit_location()
#print(secant_loop(3418.4854))



