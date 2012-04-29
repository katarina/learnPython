#Exercise 5: More Variables

#d - signed integer decimal
#i - signed integer decimal
#0 - unsigned octal
#u - unsigned decimal
#x - unsigned hexadecimal (lowercase)
#X - unsigned hexadecimal (uppercase)
#e - floating point exponential format (lowercase)
#E - floating point exponential format (uppercase)
#d - floating point decimal format
#F - floating point decimal format
#g - same as "e" if exponent is greater than -4 or less than precision, "f" otherwise
#G - same as "E" if exponent is greater than -4 or less than precision, "F" otherwise
#r - string (converts any python object using repr()).
#s - string (converts any python object using str()).
#% - no argument converted, results in a "%" character in the result
#http://docs.python.org/release/2.4.4/lib/typesseq-strings.html

my_name = "katarina"
my_age = 24
my_height = 62 #inches
my_weight = 118 #pounds
my_w = 118.3

print "Let's talk about %s" % my_name
print "I am %d inches tall" % my_height
#print "I am %d heavy" % my_weight
print "I am %f heavy" % my_w
print "I am %d old" % my_age

#print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height+ my_weight)
print "If I add %d, %d, and %f I get %f" % (my_age, my_height, my_w, my_age + my_height+ my_w)
