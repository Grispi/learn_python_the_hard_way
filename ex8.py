
# New variable
formatter = "%r %r %r %r"
formatter2 = "{} {} {} {}"

#Print the variable formatter + numbers
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it dind't sing.",
    "So I said goodnight."
)


print formatter2 .format(1, 2, 3, 4)
print formatter2 .format("one", "two", "three", "four")
print formatter2 .format(True, False, False, True)
print formatter2 .format(formatter2, formatter2, formatter2, formatter2)
print formatter2 .format(
    "I had this thing.",
    "That you could type up right.",
    "But it dind't sing.",
    "So I said goodnight."
)
