####################################################################
# @Title: Testing and profiling module for factorial functions
# @Author: Marcelo Ponce
# @Date: March 2021
####################################################################


# load factorials defns
from factorials import *

#######

def testingFn(FactFn):
	'''Function to test and profile factorials fns defines in factorials.py'''

	# load sys module to manipulate stack limits
	import sys

	# define some tests cases
	tests = [0, 1, 10, 100, 1e4]	#, 1e6]

	# need to adjust stack size, in particular for recursive calls
	# get the current value of stack for recursion calls
	origRecLim = sys.getrecursionlimit()
	# increase stack size for recursion calls by 10% above the largest value in the test case
	sys.setrecursionlimit(int(1.10*max(tests)))

	# run test cases
	for i in tests:
		# enforce the number to be an integer
		i = int(i)
		FactFn(i)

	# return stack to original value
	sys.setrecursionlimit(origRecLim)

########


def profSort(prof, key='cumulative', n=5):

	import pstats

	p = pstats.Stats(prof)
	p.sort_stats(key)
	p.print_stats(n)


def profileFactFns():
	'''Function to profile the implementation of factorial fns'''

	# load profiler
	import cProfile

        # Profile each implementation using the testing fn
	cProfile.run("testingFn(factorialIteractive)",'pIte')
	cProfile.run("testingFn(factorialRecursive)",'pRec')
	cProfile.run("testingFn(factorialBuiltin)",'pB1')
	cProfile.run("testingFn(factorialBuiltin2)",'pB2')

	profs = ['pIte','pRec', 'pB1', 'pB2']
	for prof in profs:
		profSort(prof,n=10)
	

########


# run test/profile cases if scripts is run from CLI
if __name__ == "__main__":
	profileFactFns()


####################################################################

