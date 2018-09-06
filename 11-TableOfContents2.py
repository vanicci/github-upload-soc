# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Table of contents. Write a table of contents program here. Start the program with a list holding all of the information for your table of contents (chapter names, page numbers, and so on). Then print out the information from the list in a beautifully formatted table of contents. Use string formatting such as left align, right align, center.

mylist = [["Chapter 1", "Getting Started", 1],
			["Chapter 2", "Numbers", 9],
			["Chapter 3", "Letters", 13],]

print(": Chapter of the Book : Subject Title     : Page Number :")

for item in mylist:
	print(":", item[0], " "*(18-len(item[0])),":",
		item[1], " "*(16-len(item[1])),":",
		item[2], " "*(10-len(str(item[2]))),":")
