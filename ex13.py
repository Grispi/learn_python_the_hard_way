
from sys import argv

script, first, second, third = argv

a = raw_input("What is your name? ")
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your name is {}".format(a)
