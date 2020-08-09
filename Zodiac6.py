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
file = open("/home/nancy/zodiak/python/mattest.txt", "r")
print(file.read()) 
#Test and see if we can find all possible permutations of the indicies of the matrix in the file.
arrayofindices = (0, 1, 2, 3, 4)
genobjnumlist = all_possible_permutations(arrayofindices)
print ("input is", arrayofindices)
print ("output is:")
for i in genobjnumlist:
 	print(i)
#Test and see if we can create a list of strings using the readlines() function.
with open("/home/nancy/zodiak/python/mattest.txt", "r") as file:
	listofstrings = file.readlines()
print (listofstrings)
#Strip the newline character at the end.
newlist = []
for str in listofstrings:
	newlist.append(str.rstrip("\n"))
print (newlist)
#For each possible permutation, add each scrambled row to a string.
listofindices = [0, 1, 2, 3, 4]
genobjstr = all_possible_permutations(listofindices)
finalstring = ""
for j in genobjstr:
	print (j)
	for i in newlist:
		print (i)
		for k in j:
			print (i[k])
			finalstring += (i[k])
	print (finalstring)
	print ("\n")
