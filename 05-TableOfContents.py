# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Table of contents. Here’s something for you to do in order to play around more with center, ljust, and rjust: write a program that will display a table of contents so that it looks like this:
# Chapter 1: Getting Started page 1 Chapter 2: Numbers page 9 Chapter 3: Letters page 13

mylist = [["Chapter 1", "Getting Started", 1],
			["Chapter 2", "Numbers", 9],
			["Chapter 3", "Letters", 13],]

print(": Chapter of the Book : Subject Title     : Page Number :")

for item in mylist:
	print(":", item[0], " "*(18-len(item[0])),":",
		item[1], " "*(16-len(item[1])),":",
		item[2], " "*(10-len(str(item[2]))),":")
