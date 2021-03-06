####################################################################
# @Title: Multiple definitions of factorial functions using recursion,
#	iterations, and builtin functions
# @Author: Marcelo Ponce
# @Date: March 2021
####################################################################

def factorialIteractive(num):
	'''Function to compute factorial using the iterative product implementation'''

	fact = 1

	# iteration to compute product
	# i.e. n! = 1*2*3*...*(n-1)*n
	for n in range(2, num + 1):
		fact = fact * n

	return fact


def factorialRecursive(num):
	'''Function to compute factorial using a recursive implementation'''

	# base condition: if n=0 or 1 --> n!=1
	if num < 2:
		return 1
	else:
		return num * factorialRecursive(num-1)


def factorialBuiltin(num):
	'''Function to compute factorials using the factorial bulitin fn'''

	from math import factorial

	return factorial(num)


def factorialBuiltin2(num):
	'''Function to compute factorials using the prod fn from numpy'''

	import numpy as np

	if num == 0:
		return 1
	else:
		return np.prod(np.arange(1,num+1))


####################################################################

