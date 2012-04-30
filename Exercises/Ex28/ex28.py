#Exercise 28: Boolean Practice


#1. True and True
print "#1. True and true: ",  True == True and True

#2. False and True
print "2. False and true: ", False == False and True

#"test" == "test"
print '4. \"test\" == \"test\": ', True == ("test"=="test")

print "5. 1==1 or 2!= 1: ", True == (1==1 or 2!=1)

print "6. True and 1==1: ", True == (True and 1==1)

#this was wrong, corrected
print "WRONG 7. False and 0 != 0: ", False == (False and 0 != 0)

print "8. True or 1 == 1: ", True == (True or 1 ==1)

print '9. \"test\" == \"testing\": ', False == ("test" == "testing")

print "10. 1 != 0 and 2==1: ", False == (1 != 0 and 2==1)

print '11. \"test\" != \"testing\": ', True == ("test" != "testing")

print '12. \"test\" == 1: ', False == ("test" == 1)

#this was wrong, but I caught it
print "WRONG? 13. not (True and False)", True == (not (True and False))

print "14. not (1==1 and 0 != 1)", False == (not (1==1 and 0!=1))

#this was wrong, but I caught it
print "WRONG? 15. not (10 == 1 or 1000 == 1000)", False == (not (10 ==1 or 1000 == 1000))

#this was wrong, corrected
print "WRONG! 16. not (1!= 10 or 3 == 4)", False == (not(1 != 10 or 3 ==4))

print '17. not (\"testing\" == \"testing\" and \"Zed|\" == \"Cool Guy\": ', True == (not ("testing" == "testing" and "Zed" == "Cool guy"))

print '18. 1 == 1 and not (\"testing\" == 1 or 1 == 0): ', True == (1==1 and not("testing" ==1 or 1==0))

#this was wrong, corrected
print 'WRONG! 19. \"chunky\" == \"bacon\" and not (3==4 or 3==3)', False == (("chunky" and "bacon") and not (3==4 or 3==3))

#this was wrong, corrected
print 'WRONG! 20. 3==3 and not (\"testing\" -- \"testing\" or \"Python\" == \"fun\": ', False == (3==3 and not ("testing" == "testing" or "Python" == "fun"))
