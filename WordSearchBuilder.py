import random #Using the random library for placing the letters into the grid randomly
import pyperclip

f = open("words.txt", "r") #importing the txt document that contains all the words that'll be used in the puzzle

newContent = [] #this will be the array where the verified words will go
locations=[]
count = 0 #simple count to be used in for loops when needed
word = "" #temp string variable to place a word into and verify it
x = 15 #sets the x to the grid

y = 15 #sets the y to the grid

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #An array containing the full english alphabet

#gridX = ['A','B','C','D','E','F','H','I'] #An array to go on top of the grid to show column number
gridX = []
for letter in alphabet:
    if count != x:
        count += 1
        letter = letter.upper()
        gridX.insert(count - 1, letter)
#gridY = ['1','2','3','4','5','6','7','8'] #An array to go at the side of the grid to show the row number
gridY = []
for count in range(y):
    if count != y:
        count += 1
        gridY.insert(count - 1, count)

lettersInGrid = []

def initalizeArray():
    for i in range(y):
        lettersInGrid.insert(i, [])
        for j in range(x):
            lettersInGrid[i].insert(j, " ")

content = f.readlines() #Sets the content of the txt document into the initial unchecked array

for line in content: #The start of the verification process
    count += 1 
    word = "{}".format(line.strip()) #sets the first value in the "Content" array to the temp string variable, it also uses the .strip() so that the \n at the end of each word is removed
    if word.islower() == True: #if statement to check if the letters in the word are all lowercase
        pass #If they're all lowercase the statement will be passed as nothing needs to be done
    else:
        word = word.lower() #it will change the letters into lowercase
    if len(word)>x: #checks the length of the word and makes sure it doesnt exceed the grid size
        print("word in words.txt too long: {}".format(word)) #Will print a message telling the user a word in the list is too long and will tell them which one
    else:
        newContent.insert(count - 1, word) #once the word has been verified and formated the word will be added into the "newContent" array

newContent = sorted(newContent, key=len, reverse=True)
print(newContent)
print (lettersInGrid)

def randomizeGrid():
    outputString = "" #A string to create the grid and also add the random letters into it
    for i in range (y): 
        for j in range (x):
            if lettersInGrid[i][j] == " ":
                lettersInGrid[i][j] = alphabet[random.randint(0, len(alphabet)-1)]

def wordRangeX(word):
    maxX = x - len(word)
    return maxX

def wordRangeY(word):
    maxY = y - len(word)
    return maxY
    
# for word in newContent:
#     print(wordRangeX(word))
#     print(wordRangeY(word))

tempArray = []
for i in range(y):
    tempArray.insert(i, [])

def outputGridFromArray():
    gridplace = "   " #A string for placing the outside letters and numbers next the the grid in
    outputString = "" #A string to create the grid and also add the random letters into it


    for i in gridX: #for loop for placing in the "gridX" array on top of the grid
        gridplace = gridplace + "  " + i + " " #Places in the contents of the array above the grid
    print (gridplace)

    for i in range (y): 
        outputString = " {} | ".format(gridY[i])
        print ("    " + "_ "*(x * 2))
        for j in range (x):
            #outputString = outputString + alphabet[random.randint(0, len(alphabet)-1)] + " | "
            outputString = outputString + lettersInGrid[i][j].lower() + " | "
        print(outputString)

def inputWordsToArrayHoriz(word, rerun):
    
    startLocation = 0
    height = 0
    count = 0
    activeLocation = False
    runAttempt = 0
    while activeLocation == False :
        startLocation = random.randint(0, wordRangeX(word))
        height = random.randint(0, y - 1)
        
    
        activeLocation = True
        for i in range(len(word)):
            if lettersInGrid[height][(startLocation + i)] != " ":
                activeLocation = False
                runAttempt += 1

        if(rerun == True & runAttempt == 50):
            break
        elif (rerun == False & runAttempt == 50):
            print("Attempting Vert")
            inputWordsToArrayVert(word, True)


    if random.randint(0,1) == 0:
        for letter in word: # normal
            #print(height, startLocation + count, letter)
            #print(lettersInGrid[height][(startLocation + count)])
            lettersInGrid[height][(startLocation + count)] = letter.upper()
            #print(lettersInGrid)
            count = count + 1
    else:
        count = len(word) # reverse, reverse
        for letter in word:
            #print(height, startLocation + count, letter)
            #print(lettersInGrid[height][(startLocation + count )])
            lettersInGrid[height][(startLocation +count - 1)] = letter.upper()
            #print(lettersInGrid)
            count = count - 1

    
    locationData = [height + 1, gridX[startLocation], len(word), 0]
    locations.append(locationData)
    outputGridFromArray()
        
def inputWordsToArrayVert(word, rerun):
    startHeight = 0
    location = 0
    count = 0
    activeLocation = False
    runAttempt = 0
    while activeLocation == False :
        startHeight = random.randint(0, wordRangeY(word))
        location = random.randint(0, x - 1)

        activeLocation = True
        for i in range(len(word)):
            if lettersInGrid[startHeight + i][(location)] != " ":
                activeLocation = False
                runAttempt+= 1

        if(rerun == True & runAttempt == 50):
            break
        elif (rerun == False & runAttempt == 50):
            print("Attempting Horiz")
            inputWordsToArrayVert(word, True)
        


    if random.randint(0,1) == 0:
        for letter in word:
            #print(startHeight + count, location , letter)
            #print(lettersInGrid[(startHeight + count)][location])
            lettersInGrid[(startHeight + count)][location] = letter.upper()
            #print(lettersInGrid)
            count = count + 1
    else:
        count = len(word)
        for letter in word:
            #print(startHeight + count, location , letter)
            #print(lettersInGrid[(startHeight + count)][location])
            lettersInGrid[(startHeight + count - 1)][location] = letter.upper()
            #print(lettersInGrid)
            count = count - 1

    
    locationData = [startHeight + 1, gridX[location],  len(word),  1]
    locations.append(locationData)
    outputGridFromArray()

initalizeArray()


for word in newContent:
    if random.randint(0,1) == 0:
        inputWordsToArrayHoriz(word, False)
    else:
        inputWordsToArrayVert(word, False)

outputGridFromArray()

randomizeGrid()





def outputToHTMLTable(lettersInGrid):
    
    h = open("Header.txt", "r")
    header_txt = h.read()
    h.close()
    r = open("Footer.txt", "r")
    footer_txt = r.read()
    r.close()

    result =  open("Wordsearch.txt", "w")

    outputString = "<table>"
    for i in range(len(lettersInGrid[0])):
        outputString+="<tr>"
        for j in range(len(lettersInGrid[i])):
            outputString+="<td>"
            if(ord (lettersInGrid[i][j]) < 91):
                outputString+="<button onclick='this.style.color = " + '"green"' + "'>"
                outputString+=lettersInGrid[i][j].lower()
                outputString+='</button>'
            else:
                outputString+="<button onclick='this.style.color = " + '"red"' + "'>"
                outputString+=lettersInGrid[i][j].lower()
                outputString+='</button>'
            outputString+="</td>"
        outputString+="</tr>"
    outputString+="</table>"
    outputString+="\n<b><u>Words To Find</u></b>\n"
    
    for line in content: #The start of the verification process
        outputString+="<p>"
        word = "{}".format(line.strip())
        outputString+=word.lower()
        outputString+="</p>"

    result.write(header_txt + outputString + footer_txt)
    result.close()
    print(outputString)
    pyperclip.copy(outputString)
    spam = pyperclip.paste()


outputGridFromArray()

print(locations)
print(lettersInGrid)



outputToHTMLTable(lettersInGrid)


f.close()
