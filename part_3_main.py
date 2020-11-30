import numpy as np
import matplotlib.pyplot as plt
from euler_rocket import *


x=0
y=0
dt=0.0001
v0=690
theta0=50
friction=0.0003348



def kassam_in_air (dt , x_0 , y_0 , vx_0 , vy_0, friction_coefficient):
    x_n = x_0
    y_n = y_0
    vx_n = vx_0
    vy_n = vy_0
    x = []
    y = []
    while y_n > 10 ** (-9) or len(y) < 2:
        x.append(x_n)
        y.append(y_n)
        x_n, y_n, vx_n, vy_n = part_three_rocket_iteration(x_n, y_n, vx_n, vy_n, dt, friction_coefficient)
    return x, y

def part_three_check_converges(x_0 , y_0 , vx_0 , vy_0, friction_coefficient):
    log_dt_lst = np.linspace(-6, 1, 50)
    dt_lst = 10 ** log_dt_lst
    x=np.array([])
    for dt in dt_lst:
        x_tag,y=kassam_in_air(dt,x_0,y_0,vx_0,vy_0,friction)
        x=np.concatenate((x,[x_tag[-1]]))
    plt.loglog(dt_lst, x)
    plt.xlabel(r'$dt in log$ [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$x$ [$\mathrm{m}$]', size=15)
    plt.title("Part 3- x dest Converges? ")
    plt.grid()
    plt.show()



def visualisation(xA, yA, dt, name):
    t_array = np.array([n * dt for n in range(len(xA))])
    x_array = np.array(xA)
    y_array = np.array(yA)
    plt.plot(x_array, y_array)
    plt.xlabel(r'$x$ [$\mathrm{m}$]', size=15)
    plt.ylabel(r'$y$ [$\mathrm{m}$]', size=15)
    plt.title(name)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    v_x0 = v0*np.cos(theta0*np.pi / 180.)
    v_y0 = v0*np.sin(theta0*np.pi / 180.)

    xA,yA = kassam_in_air(dt,x,y,v_x0,v_y0, friction)
    visualisation(xA,yA,dt,"Part 3 - Rocket launch in air")
    xA, yA = kassam_in_air(dt, x, y, v_x0, v_y0, 0)
    visualisation(xA, yA, dt, "Part 3 - Rocket launch in vacuum")
    xA, yA = kassam_in_air(dt, x, y, v_x0, v_y0, 1)
    visualisation(xA, yA, dt, "Part 3 - Rocket launch in thick air")



