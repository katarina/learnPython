#Exercise 39: Doing things to lists

ten_things = "Apples Oranages Crows Telelphone Light Sugar"

print "Wait there's not 10 things in the list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

#print stuff
print "I am stuff[1]", stuff[1]
print "I am stuff -1", stuff[-1]
print "I am stuff pop", stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:6])
