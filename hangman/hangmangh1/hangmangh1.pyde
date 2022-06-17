displayScreen = 0
timer = 0


def setup():
    global words, randomWord, word, wrongGuess, rightGuess, gameOver
    size(1000, 600)
    textAlign(CENTER)


def draw():
    background(0)    
    if displayScreen == 0:
        startScreen()    
    elif displayScreen == 1:
        gameScreen()


def startScreen():
    global timer
    
    textAlign(CENTER)
    timer += 1
    
    #Hangman Drawing
    stroke(255)
    fill(0)
    strokeWeight(10)
    line(80 - 40, 400, 200 - 40, 400)
    line(140 - 40, 400, 140 - 40, 200)
    line(140 - 40, 200, 240 - 40, 200)
    line(240 - 40, 200, 240 - 40, 220)
    ellipse(240 - 40, 250, 50, 50)
    line(240 - 40, 275, 240 - 40, 325)
    line(240 - 40, 325, 180, 355)
    line(240 - 40, 325, 220, 355)
    line(240 - 40, 310, 180, 290)
    line(240 - 40, 310, 220, 290)
    
    #Title
    fill(255)
    textSize(100)
    text("H A N G M A N", 620, 350)
    strokeWeight(8)
    line(260, 360, 340, 360)
    line(365, 360, 445, 360)
    line(470, 360, 550, 360)
    line(575, 360, 655, 360)
    line(680, 360, 770, 360)
    line(795, 360, 875, 360)
    line(900, 360, 980, 360)
    
    #Instructions
    fill(255, 0, 0)
    textSize(20)
    text("Instructions & Rules", 500, 40)
    textSize(15)
    text("Try to figure out an unknown word by guessing letters. The player is hanged (and loses)", 500, 70)
    text("when 7 wrong letters are guessed before the word is completed. Each blank is a letter", 500, 90)
    text("in the word. When a right letter is guessed, it replaces the blanks in the position of", 500, 110)
    text("the word. When a wrong letter is guessed, the letter appears at the bottom of the screen", 500, 130)
    text("and a body part is added. The game is won when all the letters of the word are guessed.", 500, 150)

    #Indicator to start game
    fill(255)
    textSize(25) 
    for i in range(15):
        if timer % 30 == i:
            text("Press SPACE to Start", 500, 500)
        
        
def gameScreen():
    global words, randomWord, word, wrongGuess, rightGuess, gameOver
    background(0)
    stroke(255)
    fill(255)
    
    #Hangman display 
    strokeWeight(10)
    line(40, 380, 160, 380)
    line(100, 380, 100, 100)
    line(100, 100, 200, 100)
    line(200, 100, 200, 140)


def keyPressed():
    global displayScreen
    if displayScreen == 0 and keyCode == 32:
        displayScreen = 1
