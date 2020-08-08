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

string=("abc")
stringlist=("a","b","c")
numlist=(1,2,3)
genobjstring=all_possible_permutations(string)
genobjstringlist=all_possible_permutations(stringlist)
genobjnumlist=all_possible_permutations(numlist)
#Show that our generator function generated an object.
print ("The generated objects are:")
print (genobjstring)
print (genobjstringlist)
print (genobjnumlist)
print ("**************")
#Show that we can iterate over the object - and that we can generate possible permutations with a string, list of strings, and list of numbers.
print ("input is", string)
print ("output is:")
for i in genobjstring:
	print(i)
print ("**************")
print ("input is", stringlist)
print ("output is:")
for i in genobjstringlist:
	print(i)
print ("**************")
print ("input is", numlist)
print ("output is:")
for i in genobjnumlist:
	print(i)
