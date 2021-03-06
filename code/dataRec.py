####################################################################
# @Title: Examples of fns to define "lists" recusively,
#	ie. using the original list
# @Author: Marcelo Ponce
# @Date: March 2021
####################################################################

###############################################################

def addList(lst, newElement, head=True):
	"""function to add elements to a list recursively"""
	# elements can be added at the beginning or the end of the list
	if head:
		lst = [newElement] + lst
	else:
		lst = lst + [newElement]
	return lst

def nestedList(lst, newElement):
	"""function to generate nested lists of new elements"""
	lst = list([lst, newElement])
	return lst

###############################################################

# examples
mylist=[0]
mynestedlist=[0]
for i in range(1,7):
	# create a list by appending elements
	mylist = addList(mylist,i)
	# create a nested list
	mynestedlist = nestedList(mynestedlist,i)

# display resulting lists
print("incremental list: ", mylist)
print("Nested list: ", mynestedlist)

# combine list
print("append list+nested list: ", addList(mylist,mynestedlist))
print("nest list+nested list: ", nestedList(mylist,mynestedlist))
