#defining the used formatters, with 4 formatters for 4 characters in the string
formatter = "%r %r %r %r"

#print out numbers for 4 formatters
print formatter % (1, 2, 3, 4)
#print out words for 4 formatters
print formatter % ("one", "two", "three", "four")
#print out Boolean arguments for 4 formatters
print formatter % (True, False, False, True)
#print out the above defined formatters for 4 formatters
print formatter % (formatter, formatter, formatter, formatter)
#print out string sentences for 4 formatters
print formatter % (
    "I had this thing",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
#single- and double quotes depending on the length of the strings? more efficient
