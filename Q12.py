def palindrome(str):
	if str[0:]==str[::-1]:
		return "Palindrome!"
	else:
		return "Not palindrome!"

a=input('Enter a string ')
print(palindrome(a))