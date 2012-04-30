#Exercise 13: Paramaters, Unpacking, Variables

from sys import argv

first = raw_input()
second = raw_input()
third = raw_input()

script, first, second, third = argv

print "The script is called:", script
print "Your first variables is:", first
print "Your second variable is:", second
print "Your third variable is:", third
