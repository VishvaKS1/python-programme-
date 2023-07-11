# Python3 code to convert a tuple
# into a string using a for loop


def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = ('p', 'y', 't', 'h', 'o', 'n')
str = convertTuple(tuple)
print(str)
