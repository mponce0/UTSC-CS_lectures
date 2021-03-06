
####################################################################
# @Title: Fibonacci functions
# @Author: Marcelo Ponce
# @Date: March 2021
####################################################################

def Fibonacci(n):
	'''Recursive definition of Fibonacci numbers'''

	if n >= 2:
		# recursive rule
		return (Fibonacci(n-1)+Fibonacci(n-2))
	elif ( n==0 or n==1 ):
		# base rule
		return n
	else:
		print("Error: Fibonacci nbrs defined for positive integers!")


def FibonacciSeq(n):
	'''Function to generate Fibonacci series'''

	for i in range(0,n+1):
		print(Fibonacci(i))


####################################################################
