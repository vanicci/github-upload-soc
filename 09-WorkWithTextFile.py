# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Find something today in your life, that is a calculation. Go for a walk, look around the park, try to count something. Anything! And write a program about it. e.g. number of stairs, steps, windows, leaves estimated in the park, kids, dogs, estimate your books by bookshelf, toiletries, wardrobe.

# Working with text file (london stations lat long) for counting lines, words and characters

infile = open('C:/Users/Vanicci/toolkitten/summer-of-code/week-01/exercises/soc-wk1day4d-london-stations-lat-long.txt', 'r')
data = infile.read()
num_characters = len(data)
num_words = len(data.split())
num_lines = len(data.splitlines())
print('Data found in London Stations Lat Long Text File')
print('Number of characters:',num_characters)
print('Number of words:', num_words)
print('Number of lines:', num_lines)
