import numpy as np 
import math
import matplotlib.pyplot as plt

def func(x):
    return -5*x**2 + 30*x + 20

def return_basic_array(f, step, start, finish):
    dots = int((finish - start)/step)
    x_axis = []
    y_axis = []
    i=0
    while i < dots:
        y_axis.append(f(start + i*step))
        x_axis.append(start + i*step)
        i+=1

    plt.plot(x_axis, y_axis)
    plt.show()

    return x_axis, y_axis

def return_derivative_array(f, step, start, finish):
    dots = int((finish - start)/step)
    x_axis = []
    y_axis = []
    i=0
    while i < dots:
        dy = (f(start + i*step) - f(start + (i+1)*step))/step 
        y_axis.append(dy)
        x_axis.append(start + i*step)
        i+=1

    plt.plot(x_axis, y_axis)
    plt.show()

    return x_axis, y_axis

start = 0
finish = 8
step = 0.01

x1, y1 = return_basic_array(func, step, start, finish)
x2 , y2 = return_derivative_array(func, step, start, finish)

N = (finish - start)/step
i = 0
while i < N:
    if y1[i] < 0:
        print(x1[i])
        break
    i+=1

i = 0
while i < N:
    if y2[i] > 0:
        print(x2[i])
        break
    i+=1