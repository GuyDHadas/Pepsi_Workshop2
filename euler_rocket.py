import numpy as np
import matplotlib.pyplot as plt



G = 9.81


def part_two_rocket_iteration(x_n, y_n, vx_n, vy_n, dt):
    x_n1 = x_n + dt * vx_n
    y_n1 = y_n + dt * vy_n
    vx_n1 = vx_n + dt * 0
    vy_n1 = vy_n + dt * (-G)
    return x_n1, y_n1, vx_n1, vy_n1


def part_two_visualisation(x, y, dt):
    t_array = np.array([n * dt for n in range(len(x))])
    x_array = np.array(x)
    y_array = np.array(y)
    plt.plot(x_array, y_array)
    plt.xlabel(r'$x$ [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$y$ [$\mathrm{m}$]', size=15)
    plt.title('Part 2 - Rocket launch in vacuum')
    plt.grid()
    plt.show()



def part_three_rocket_iteration(x_n, y_n, vx_n, vy_n, dt, friction_coefficient):
    x_n1 = x_n + dt * vx_n
    y_n1 = y_n + dt * vy_n
    vx_n1 = vx_n - dt * (friction_coefficient * vx_n * np.sqrt(vx_n**2 + vy_n**2))
    vy_n1 = vy_n - dt * (G + friction_coefficient * vy_n * np.sqrt(vx_n**2 + vy_n**2))
    return x_n1, y_n1, vx_n1, vy_n1


