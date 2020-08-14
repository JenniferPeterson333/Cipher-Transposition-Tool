import time
# The following gives the time in seconds
start_time = time.time()
# Your main program could be placed here which would take
# time to run. To simulate that, I will put in a delay
# of 10 seconds.
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
numberofwords = int(input("At least how many of the words do you want to have in your possible solution? Enter 1 or 2 etc. and press enter: "))
file = open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r")
with open("/home/nancy/zodiak/python/mat06-nospaces.txt", "r") as file:
	listofstrings = file.readlines()
newlist = []
for str in listofstrings:
	newlist.append(str.rstrip("\n"))
#Read dictionary file and do the same
file = open("/home/nancy/zodiak/python/ZodiacDictionary.txt", "r")
with open("/home/nancy/zodiak/python/ZodiacDictionary.txt", "r") as file:
	listofwords = file.readlines()
newwordlist = []
for str in listofwords:
	newwordlist.append(str.rstrip("\n"))
#Find the number of columns so we can figure out how many indicies we have and create a list of the indices.
numberofcolumns = len(newlist[0])
templist = range(numberofcolumns)
listofindices = []	
for i in templist:
	listofindices.append(i)
#For each possible permutation, add scrambled row to string, only looking at the first 50 permutations so as to not take up too much memory. 
genobjstr = all_possible_permutations(listofindices)
for j in genobjstr:
	counter = 0
	templist = []
	tempstring = ""
	finalstring = ""
	for i in newlist:
		for k in j:
			tempstring += (i[k])
	for w in newwordlist:
		if w in tempstring:
			counter += 1
			templist.append(w)
	if counter >= numberofwords:
		print (templist)
		finalstring += tempstring
		print (finalstring)
		print (counter, "word(s)")
		answer = input("Another permutation? Press y for yes and n for no and then press enter: ") 
		if answer == "y":
			continue
		else:
			break		

time.sleep(10)
end_time = time.time()
run_time_sec = end_time - start_time
run_time_hours = run_time_sec/3600.0
run_time_days = run_time_hours/24.0
print("Runtime is", run_time_sec, "sec =", run_time_hours, "hours =", run_time_days, "days")