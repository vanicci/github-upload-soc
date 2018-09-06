# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Deaf grandma. Whatever you say to Grandma (whatever you type in), she should respond with this: HUH?! SPEAK UP, GIRL!

# unless you shout it (type in all capitals). If you shout, she can hear you (or at least she thinks so) and yells back:

# NO, NOT SINCE 1938!

# To make your program really believable, have Grandma shout a different year each time, maybe any year at random between 1930 and 1950. (This part is optional and would be much easier if you read the section on Python’s random number generator under the Math Object.) You can’t stop talking to Grandma until you shout BYE.

# Hint: Try to think about what parts of your program should happen over and over again. All of those should be in your while loop.

# Hint: People often ask me, “How can I make random give me a number in a range not starting at zero?” But you don’t need it to. Is there something you could do to the number random returns to you?

# Deaf grandma extended. What if Grandma doesn’t want you to leave? When you shout BYE, she could pretend not to hear you. Change your previous program so that you have to shout BYE three times in a row. Make sure to test your program: if you shout BYE three times but not in a row, you should still be talking to Grandma.

import random

no_goodbye = 0

while no_goodbye < 3:
	name = input("[Deaf Grandma] Hi! What is your name?: ")

	if name.isupper() is True:
		print("[Grandma shouting] NO, NOT SINCE" + " " + str(random.randint(1930, 1951)) + "!")
	else:
		print("[Grandma shouting] HUH?! SPEAK UP, GIRL!!!")

	if name == "BYE":
		print("[Grandma shouting] I STILL WANT TO TALK TO YOU!")
		no_goodbye += 1
	else:
		no_goodbye = 0
