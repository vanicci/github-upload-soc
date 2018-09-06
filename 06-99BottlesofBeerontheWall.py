# Vanessa Dunford
# Github: https://github.com/vanicci
# Linkedin: https://www.linkedin.com/in/vanessa-dunford-08ab7663/
# Youtube: http://bit.ly/JoinMeOnYouTube
# Twitter: https://twitter.com/vaniccilondon

# Write a program that prints out the lyrics to that beloved classic, “99 Bottles of Beer on the Wall.”

song = ''
for n in range(99,0,-1):
    s1 = str(n) +(' bottles' if n != 1 else ' bottle')
    s2 = (str(n-1) if n-1 != 0 else 'no more')+(' bottles' if n!=2 else ' bottle')
    song += '%s of beer on the wall, %s of beer. \n\
Take one down and pass it around, %s of beer on the wall.\n\n' % (s1,s1,s2)

song += 'No more bottles of beer on the wall, no more bottles of beer. \n\
Go to the store and buy some more, 99 bottles of beer on the wall.'

print(song)
