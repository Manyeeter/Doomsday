import random
score = 0
tries = 2

#---------------------------------------------------------------------------------
#Runs the introduction
def intro():
    print("***********************************************************************")
    print("***********************************************************************")
    print("********************** WELCOME TO THE MUSIC QUIZ **********************")
    print("********** Get Points by Guessing the Correct Artist and Song *********")
    print("***********************************************************************")
    print("***********************************************************************\n\n")

#---------------------------------------------------------------------------------
#Opens file and only reads it 
s = open("songAndArtist.txt","r")

#---------------------------------------------------------------------------------
#Defines how many songs there are
def numOfSongs(s):
    length = len(s.readlines())
    return length

#---------------------------------------------------------------------------------
#Chooses a random line from .txt
intro()
numSongs = numOfSongs(s)
numSongs += 1
randomSong = random.randrange(1,numSongs)
#---------------------------------------------------------------------------------

s = open("songAndArtist.txt", "r")
for songs in range (0,randomSong):
    x = s.readline()

songInfo = x.split(",")

artist = songInfo[0]
song = songInfo[1]

print ("The artist is:\n"+artist,"\n")


#_________________________________
#finds song first letters
songName = song.split()
letters = []
for z in range (0,len(songName)):
    word = songName[z]
    letter = word[0:1]
    letters.append(letter)

print(letters)

songForResult = song.upper()
songForResult = str(songForResult)
songForResult1 = songForResult[:-1]

while tries > 0:
    userInput = input("\nPlease enter the song name: \n")
    userInput = userInput.upper()

    if tries == 2 and userInput == songForResult1:
        print("Great Succes\n\n")
        tries = 0
        score += 3
    elif tries == 1 and userInput == songForResult1:
        print("You barely got it\n\n")
        score += 1
        tries = 0
    else:
        print("you suck\n\n")
        tries -= 1


for c in range (6):
    print("***********************************************************************")