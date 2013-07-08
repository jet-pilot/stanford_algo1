import sys

comparisons = 0

def qsort(list):

	if len(list) == 0: 
		return list
	else:
		pivot = list[0]

	lesser = qsort([x for x in list[1:] if x < pivot])
	greater = qsort([x for x in list[1:] if x >= pivot])

	global comparisons
	comparisons += len(list) - 1

	return lesser + [pivot] + greater
		
if  __name__ ==  "__main__" :
	with open(sys.argv[1]) as file:
		lines = file.readlines()
		
		numbers = [line.replace('\n', '') for line in lines]
		integers = [int(number) for number in numbers]
		
		#Question 2
		
		#integers[0], integers[len(integers) - 1] = integers[len(integers) - 1], integers[0] 
		
		#Question 3
		
		# first = integers[0] 
		# second = integers[len(integers) / 2 - 1]
		# third = integers[len(integers) - 1]
		
		# pivot = sorted([first, second, third])[1]
		# pivot_index = integers.index(pivot)
		
		# integers[0], integers[pivot_index] = integers[pivot_index], integers[0]
		
		result = qsort(integers)
		
		print comparisons