#Exercise 6: Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "dont't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Istn't that joke so funny! %r"

print joke_evaluation % hilarious

w = "this is the left side of ..."
e = "a stright with a right side."

print w + e 
