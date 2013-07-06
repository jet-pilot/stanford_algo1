import sys

inversions = 0

def merge(left, right):
	result = []

	i = j = 0

	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			global inversions
			inversions += len(left) - i
			
			result.append(right[j])
			j += 1

	result += left[i:]
	result += right[j:]

	return result	
	
def merge_sort(lst):
	if len(lst) < 2:
		return lst

	middle = len(lst) / 2

	left = merge_sort(lst[:middle])
	right = merge_sort(lst[middle:])

	return merge(left, right)
	
if  __name__ ==  "__main__" :
	with open(sys.argv[1]) as file:
		lines = file.readlines()
		
		numbers = [line.replace('\n', '') for line in lines]
		integers = [int(number) for number in numbers]
		
		result = merge_sort(integers)
		
		#inversions = result.index(integers[0])
		
		print inversions
	
