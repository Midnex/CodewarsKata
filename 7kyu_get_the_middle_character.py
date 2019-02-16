# is python3, but won't run on their site
# when i test with python 3 i get no errors, when i try to put it through their online 2.7.6 version i get errors. can you help with this?

def get_middle(s):
	length = len(s)
	mid = int(length/2)
	if length <=2:
		return s
	elif length % 2 == 0:
		return s[mid-1:mid+1]
	else:
		return s[mid]
		
s = "testing"
get_middle(s)


"""
Instructions
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"

#Input
A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output
The middle character(s) of the word represented as a string.

"""