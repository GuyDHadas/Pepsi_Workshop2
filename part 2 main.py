import numpy as np
import matplotlib.pyplot as plt
from euler_rocket import *

x=0
y=0
dt=0.0001
v0=690
theta0=50


def kassam_in_vaccum(dt, x_0, y_0, v_x0, v_y0):
    x_n = x_0
    y_n = y_0
    v_xn = v_x0
    v_yn = v_y0
    x = []
    y = []
    while y_n > 10 ** (-9) or len(y)<2:
        x.append(x_n)
        y.append(y_n)
        x_n, y_n, v_xn, v_yn = part_two_rocket_iteration(x_n,y_n,v_xn,v_yn,dt)
    return x, y

if __name__ == '__main__':
    v_x0 = v0*np.cos(theta0*np.pi / 180.)
    v_y0 = v0*np.sin(theta0*np.pi / 180.)

    x,y = kassam_in_vaccum(dt,x,y,v_x0,v_y0)
    part_two_visualisation(x,y,dt)
    print(x[-1])



