from sys import argv

script, input_file = argv

#read in the file
def print_all(f):
	print f.read()

#read the file backwards
def rewind(f):
	f.seek(0)

#open the file that is being passed
current_file = open(input_file)

def print_a_line(line_count, f):
	print line_count, f.readline()

#print what is within the file
print "First let's prnt the whole file:\n"
print_all(current_file)

#read in the file backwards
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

#i have 4 lines, but this only prints 3
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
