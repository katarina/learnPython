#Exercise 30: Else and If

people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take cars."
elif cars < people:
	print "we should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "we still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's staty home then."


