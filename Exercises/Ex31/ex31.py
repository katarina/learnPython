#Exercise 31: Making Decisions

print "You enter a dark room with two doors. Do you do through door #1 or door #2?"
door = raw_input("> ")

if door == "1":
	print "There's a gian bear here eating cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats yours face off!"
	elif bear == "2":
		print "The bear eats your legs off!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3 Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jellow!"
	else:
		print "The insanity rots your eyes."

else:
	print "You stumble and fall on a knife and die."
