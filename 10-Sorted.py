# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Building and sorting an array. Write the program that asks us to type as many words as we want (one word per line, continuing until we just press Enter on an empty line) and then repeats the words back to us in alphabetical order. Make sure to test your program thoroughly; for example, does hitting Enter on an empty line always exit your program? Even on the first line? And the second?

# Hint: There’s a lovely array method that will give you a sorted version of an array: sorted(). Use it!

print("[System] Hi! Enter as many words as you want. One word per line until you press Enter on an empty line. This program will then repeat the words in alphabetical order. Ready?!")

words = []
while True:
	word = input('Enter a word: ')
	if word:
		words.append(word)
	else:
		break
print('Here are the words you entered in alphabetical order =>', sorted(words))
