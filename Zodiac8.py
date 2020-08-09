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

#Read file, create a list of strings using the readlines() function, and strip the newline character at the end.
file = open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r")
with open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r") as file:
	listofstrings = file.readlines()
newlist = []
for str in listofstrings:
	newlist.append(str.rstrip("\n"))
#For each possible permutation, add each scrambled row to a string if it includes some common letter groupings, only looking at the first 50 permutations so as to not take up too much memory. 
listofindices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
genobjstr = all_possible_permutations(listofindices)
counter = 0
counterj = 0
for j in genobjstr:
	if counterj == 50:
		break
	counteri = 0
	counterk = 0	
	tempstring = ""
	finalstring = ""
	counterj += 1
	print ("counterj = ")
	print (counterj)
	print ("j = ")
	print (j)
	for i in newlist:
		if counteri == 10:
	 		break
		counteri += 1
		print ("counteri = ")
		print (counteri)
		print ("i = ")
		print (i)
		for k in j:
			counterk += 1
			print ("counterk = ")
			print (counterk)
			print ("k = ")
			print (k)
			print (i[k])
			tempstring += (i[k])
			print (tempstring)
	if "EA" and "ST" in tempstring:
		finalstring += tempstring
		counter += 1
		print (finalstring)
		print (counter)
