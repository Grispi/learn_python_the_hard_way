def checklist():
    print "Did you start your function definition with def?, write Y(yes) or N(no)"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "It has to star with def"
    print "Does your function name have only characters and _ (underscore) characters?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "Change the name!"
    print "Did you put an open parenthesis ( right after the function name?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "You have to do it!"
    print "Did you put your arguments after the parenthesis ( separated by commas?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "You have to do it!"
    print "Did you make each argument unique (meaning no duplicated names)?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "You have to do it!"
    print "Did you put a close parenthesis and a colon ): after the arguments?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "You have to do it!"
    print "Did you indent all lines of code you want in the function four spaces? No more, no less."
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "You have to do it!"
    print "Did you 'end' your function by going back to writing with no indent (dedenting we call it)?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "So do it!"


    print 'When you run ("use" or "call") a function, check these things:'

    print "Did you call/use/run this function by typing its name?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "So do it!"
    print "Did you put the ( character after the name to run it?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "So do it!"
    print "Did you put the values you want into the parenthesis separated by commas?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "So do it!"
    print "Did you end the function call with a ) character?"
    answer = raw_input()
    if answer == "Y":
        print "perfect go on.."
    else:
        print "So do it!"





checklist()





# print "May I ask your age?"
# age = int(raw_input())
# #int in order to convert to a number - input create a string
#
# if age >= 18 and age <25:
#     print "You can rent a car with extra fee"
# elif age>= 25:
#     print "You can rent a car"
# else:
#     print "You cannot rent a car"
