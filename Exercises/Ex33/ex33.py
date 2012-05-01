#Exercise 33: While Loops

i = 0
numbers = []

def myLoop(a):
	i = 0
	while i < int(a):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

b = raw_input("> ")
myLoop(b)

for num in numbers:
	print num
