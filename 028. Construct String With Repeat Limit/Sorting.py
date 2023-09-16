from collections import Counter
def repeatLimitedString(s: str, repeatLimit: int) -> str:

	# First, we want to know how many times each character appears in the string "s"
	freq = Counter(s)

	# A list of all the characters in the string
	charList = [key for key in freq]

	# Sort the charList
	charList.sort()

	# Output string to return
	output = []

	# To keep track of the largest character at any time
	i = len(charList) - 1

	# What was the previous character
	prevCharacter = ''

	while len(output) != len(s):

		# If previous character is not the same as character at "i" index in charList
		if prevCharacter != charList[i]:

			# How many times we can use this character in a row
			repeatedCount = 0

			# Now, we can put at most "repeatLimit" characters in output
			while repeatedCount < repeatLimit and freq[charList[i]] > 0:
				output.append(charList[i])
				freq[charList[i]] -= 1
				repeatedCount += 1

			# Update the previous character
			prevCharacter = charList[i]

			# If the frequency of character at "i" is already 0, we can decrement "i"
			if freq[charList[i]] == 0: 

				# Decrement i
				i -= 1

		# If previous character is the same as character at "i" index in charList
		else:
			# We cannot use it again at this point
			# So, we have to use the second greatest character at this time, if it exists
			# If the second greater does not exist, break as there is no longer string possible

			# secondGreatest
			j = i - 1

			# We can only use a character if its frequency is not already 0
			while j >= 0 and freq[charList[j]] == 0: j -= 1

			# If j goes out of bounds, then there is no longer string possible at this point
			if j < 0: break

			# Otherwise, we can use the character at index "j" in charList
			# We will only put one instance of this second character in the output
			# Because we want as many greater characters as possible in the beginning of the output string
			output.append(charList[j])

			# Update the previous character
			prevCharacter = charList[j]

			# Reduce the frequency in the dictionary
			freq[charList[j]] -= 1

	# Return the output string
	return "".join(output)


s = "aababab"
repeatLimit = 2

print("Output -> ", repeatLimitedString(s, repeatLimit))