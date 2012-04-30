#Exercise 16: Reading and Writing Files

from sys import argv

scipt, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'a')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

print "Im going to write these to the file."

target.write("I am line 1: %s \nI am line 2: %s \nI am line3: %s" % (line1, line2, line3))

print "And finally, we close it."
target.close()
