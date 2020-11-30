import numpy as np
import matplotlib.pyplot as plt
from euler_rocket import *


G = 9.81

print("Guy is in the git project, update if you see this and write below")
print("ran was here")
print("Guy likes to eat " + str(np.pi))
print( "Omer has a unique sentence")


def kassam_in_vaccum(dt, x_0, y_0, v_x0, v_y0):
    x_n = x_0
    y_n = y_0
    v_xn = v_x0
    v_yn = v_y0
    x = []
    y = []
    while y_n > 10 ** (-6):
        x.append(x_n)
        y.append(y_n)
        x_n, y_n, v_xn, v_yn = part_one_rocket_iteration()
    return x, y



