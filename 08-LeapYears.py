# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Leap years. Write a program that asks for a starting year and an ending year and then puts all the leap years between them (and including them, if they are also leap years).

# Leap years are years divisible by 4 (like 1984 and 2004). However, years divisible by 100 are not leap years (such as 1800 and 1900) unless they are also divisible by 400 (such as 1600 and 2000, which were in fact leap years). What a mess!

print("Hi! Welcome to this Leap-year program. Enter a starting year and an ending year and then the system will put all the leap years between them. Ready?!")

start = int(input("Enter starting year: "))
end = int(input("Enter ending year: "))

print ("Here are the Leap years between", start, "and", end, ":")

def leap(start, end):
	while start <= end:
	    if start % 4 == 0 and start % 100 != 0:
	       print(start)
	    if start % 100 == 0 and start % 400 == 0:
	       print(start)
	    start += 1

leap(start, end)
