# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this: WHADDAYA MEAN "I WANT A RAISE"?!? YOU'RE FIRED!!

text = ""

while text != "I quit":
	text = input("[Angry Boss]What do you want from me?: ")
	print("WHADDAYA MEAN \"" + text + "\"  YOU'RE FIRED!!!")

print("Goodbye and the best of luck!")
