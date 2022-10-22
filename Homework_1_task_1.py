import numpy as np 
import math
import matplotlib.pyplot as plt

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
	
def return_2derivative_array(f, step, start, finish):
	h = 0.01
	dots = int((finish - start)/step)
	x_axis = []
	y_axis = []
	i=0
	while i < dots:
		f2 = (f(start + i*step) - f(start + (i+1)*step))/step 
		f1 = (f(start + h + i*step) - f(start + h + (i+1)*step))/step
		dy = (f1 - f2)/h
		y_axis.append(dy)
		x_axis.append(start + i*step)
		i+=1
	plt.plot(x_axis, y_axis)
	plt.show()
	
def func(x):
	return math.exp(-2*x)

start = -2
finish = 2
step = 0.1

return_basic_array(func, step, start, finish)
return_derivative_array(func, step, start, finish)
return_2derivative_array(func, step, start, finish)