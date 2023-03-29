import numpy as np
from math import floor
import time

def calcHist(my_array):
	'''
	Builds a histogram.

	Args: my_array -- input array
	'''
	my_hist = np.zeros(10)

	for elem in my_array:
		elem_idx = floor(elem / 100) #index of mt_array's element in my_hist array
		my_hist[elem_idx] += 1

	return my_hist

def calcTime(iters=100):
	'''
	Calculates the time of the maximum, minimum and
	average time of the histogram.

	Args: iters -- number of iterations
	'''
	max_time = 0
	min_time = 10**3
	avr_time = 0

	for i in range(iters):
		X = np.random.randint(low=0, high=999, size=10**6) #Array of 10^6 random integers from 0 to 999

		#Measuring build time
		start = time.time()
		calcHist(X)
		end = time.time()

		run_time = end - start #Build time of hist

		#Calculating max, min and average run time
		if max_time < run_time:
			max_time = run_time

		elif min_time > run_time:
			min_time = run_time
		avr_time += run_time

	avr_time /= iters
	return (max_time, min_time, avr_time)

#Output result
times = calcTime()
print (f'Максимальное время выполнения: {round(times[0], 5)}\nМинимальное время выполнения: {round(times[1], 5)}\nСреднее время выполнения: {round(times[2], 5)}\n')