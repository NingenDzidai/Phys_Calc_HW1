import numpy as np
import math
import matplotlib.pyplot as plt

t1 = 0 
t2 = 0

def func(x):
	return -2 + x**0.5

def bisection(f, a, b, d):
	N = 0
	while b - a > d:

		if func(a) == 0:
			break
		if func(b) == 0:
			break

		dx = (b-a)/2
		if np.sign(func(a + dx)) != np.sign(func(b)):
			a = a + dx
		else:
			b = a + dx
		N+=1

	print(b)
	return N


def derivative(f, x):
	d = 0.001
	return (f(x+d) - f(x))/d

def Newton(f, a, b, d):
	N = 0
	while abs(f(b)) > d:
		b = b - f(b)/derivative(f, b)
		N+=1
	
	print(b)
	return N

eps = 0.01 
a = -10 
b = 10
n1 = []
n2 = []
epsilon = []

while eps < 0.1:
	eps += 0.01
	n1.append(bisection(func, a, b, eps))
	n2.append(Newton(func, a, b, eps))
	epsilon.append(eps)

print(n1)
print(n2)

plt.plot(n1, epsilon)
plt.show()
plt.plot(n2, epsilon)
plt.show()