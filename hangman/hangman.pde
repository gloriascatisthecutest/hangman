displayScreen = 0
timer = 0

def setup():
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
    
    textSize(25)
    for i in range(15):
        if timer % 30 == i:
            text("Press SPACE to Start", 500, 500)
        
        
def gameScreen():
    background(0)
