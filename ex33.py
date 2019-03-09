i = 0
numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#
# print "The numbers: "
#
# for num in numbers:
#     print num

def counter(number, increment):
    i = 0
    numbers = []
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "
    for num in numbers:
        print num
counter(20, 10)


def counter_function(number_b):
    empty_list = []
    i = 0
    for i in range(0,number_b):
        if i < number_b:
            print "At the top i is %d" % i
            empty_list.append(i)
            i += 1
            print "Numbers now: ", empty_list
    return empty_list

print counter_function(6)
