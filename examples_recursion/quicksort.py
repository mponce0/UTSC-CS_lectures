def QuickSort(arr, verbose=False):

    elements = len(arr)
    
    if elements < 2:	# Base case
        return arr
    
    current_position = 0  #Position of the partitioning element

    for i in range(1, elements):  #Partitioning loop
        if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp  #Brings pivot to it's appropriate position

    if verbose:
        print(arr[0:current_position],arr[current_position],
              arr[current_position+1:elements])

    left = QuickSort(arr[0:current_position],verbose) #Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position+1:elements],verbose) #Sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr


########


# run example cases if script is run from CLI
if __name__ == "__main__":
	array_to_be_sorted = [4,2,7,3,1,6]
	print("Original Array: ",array_to_be_sorted)
	print("Sorted Array: ",QuickSort(array_to_be_sorted,verbose=True))

####################################################################
