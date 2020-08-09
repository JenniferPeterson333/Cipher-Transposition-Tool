#We will use this generator function to find all possible permutations of the indicies of our matrix. The number of possible permutations in this case goes into the billions, and we don't want to store all of them before we examine them - it will take up too much memory. This is why we want to use a generator function - a function that returns an object which can then, using the special yield keyword, be iterated over to return as many results at a time as we want.

def all_possible_permutations(mylist):
    #Base case, if list only has one item left...
	if len(mylist) <= 1:
		yield mylist
	else:
        #Using the perm built-in function, we iterate recursively over mylist, finding the permutations on either side of the first item in each iteration as we place it in each index in the list.  
		for perm in all_possible_permutations(mylist[1:]):
			for i in range(len(perm)+1):
				yield perm[:i] + mylist[0:1] + perm[i:]

#Test and see if we can read a file. 
file = open("mattest.txt", "r")
print(file.read()) 
#Test and see if we can find all possible permutations of the indicies of the matrix in the file.
arrayofindices = (0, 1, 2, 3, 4)
genobjnumlist = all_possible_permutations(arrayofindices)
print ("input is", arrayofindices)
print ("output is:")
for i in genobjnumlist:
 	print(i)
