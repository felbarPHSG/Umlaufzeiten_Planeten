add_library('minim') # Hinzufügen der "Minim" Library zum Abspielen von Audiodateien
a = -1
b = -1
start_rakete = 0
start_verfolgung = 0
presstime = 0
presstime2 = 0
angle_factor = [PI/88, PI/225, PI/365, PI/687, PI/4330, PI/10585] # Geschwindigkeit der Planeten
angle_list = [0, 0, 0, 0, 0, 0] # Winkel der Planeten, wichtig für Position und Counter  
counter_list = [0, 0, 0, 0, 0, 0] # Counter für Planeten
offset = [0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0, 0, 0]
offset_namen = [2, 1.3, 1.4, 1.6, 1.1, 1.1]
namen = ["Merkur", "Venus", "Erde", "Mars", "Jupiter", "Saturn"]


def setup():
    fullScreen()
    frameRate(120)
    global img_list
    global audio_list
    global vpoint
    global planet_size
    global radius
    ellipseMode(RADIUS)
    minim = Minim(this) # Laden der "Minim" Library
    img_list = [loadImage("Merkur.png"), loadImage("Venus.png"), loadImage("Erde.png"), loadImage("Mars.png"), loadImage("Jupiter.png"), loadImage("Saturn.png"), loadImage("Rakete.png"), loadImage("Astronaut.png"), loadImage("Ufo.png")]
    audio_list = [minim.loadFile("Countdown.mp3"), minim.loadFile("Laser.mp3")]
    # Vektorenpunkte der Himmelskörper festlegen, um anschliessend den Abstand zur Sonne zu berechnen
    vpoint = [PVector(width/2, height/2), PVector(width/2.2, height/2.2), PVector(width/2.4, height/2.4), PVector(width/2.6, height/2.6), PVector(width/2.9, height/2.9), PVector(width/3.2, height/3.2), PVector(width/3.65, height/3.65)]
    planet_size = [width/120, width/70, width/70, width/90, width/50, width/50]
    radius = [dist(vpoint[0][0], vpoint[0][1], vpoint[1][0], vpoint[1][1]), 
              dist(vpoint[0][0], vpoint[0][1], vpoint[2][0], vpoint[2][1]),
              dist(vpoint[0][0], vpoint[0][1], vpoint[3][0], vpoint[3][1]),
              dist(vpoint[0][0], vpoint[0][1], vpoint[4][0], vpoint[4][1]),
              dist(vpoint[0][0], vpoint[0][1], vpoint[5][0], vpoint[5][1]),
              dist(vpoint[0][0], vpoint[0][1], vpoint[6][0], vpoint[6][1])] # Abstand der Planeten zur Sonne

def draw():
    global speed
    global xpos
    global ypos
    background(10,10,45)
    speed = pow(mouseX/(0.5*width), 2)*4 # Geschwindigkeit nimmt auf der X-Achse nach rechts zu, nach links ab

    xpos = [vpoint[0][0] + sin(angle_list[0])*(radius[0]*1.2),
            vpoint[0][0] + sin(angle_list[1])*(radius[1]*1.2),
            vpoint[0][0] + sin(angle_list[2])*(radius[2]*1.2),
            vpoint[0][0] + sin(angle_list[3])*(radius[3]*1.2),
            vpoint[0][0] + sin(angle_list[4])*(radius[4]*1.2),
            vpoint[0][0] + sin(angle_list[5])*(radius[5]*1.2)] # x-Position der Planeten
    
    ypos = [vpoint[0][1] + cos(angle_list[0])*radius[0],
            vpoint[0][1] + cos(angle_list[1])*radius[1],
            vpoint[0][1] + cos(angle_list[2])*radius[2],
            vpoint[0][1] + cos(angle_list[3])*radius[3],
            vpoint[0][1] + cos(angle_list[4])*radius[4],
            vpoint[0][1] + cos(angle_list[5])*radius[5]] # y-Position der Planeten
    
    # Abrufen der unten definierten Funktionen
    umlaufbahnen()
    planetennamen()
    planets()
    sonne()
    ui_umlaufbahnen()
    ui_planetennamen()
    umrundungen()
    counter_reset()
    pfeil()
    exitbutton()
    rakete()
    verfolgung()
        
def umlaufbahnen(): # Wenn die rechte Maustaste gedrückt wird, werden die Planetenbahnen ein- oder ausgeblendet
    if a == 1:
        noFill()
        stroke(255,60)
        strokeWeight(width/300)
        for i in range(0, 6):
            ellipse(vpoint[0][0], vpoint[0][1], radius[i]*1.2, radius[i])
        
def planetennamen(): # Wenn die linke Maustaste gedrückt wird, werden die Planetennamen ein- oder ausgeblendet
    if b == 1:
        fill(255)
        textSize(width/100)
        textAlign(CENTER)
        for i in range(0, 6):
            text(namen[i], xpos[i], ypos[i]+planet_size[i]*offset_namen[i])
        
def sonne():
    stroke(240,120,50)
    strokeWeight(planet_size[4]/8)
    fill(255,230,5)
    ellipse(vpoint[0][0], vpoint[0][1], planet_size[4], planet_size[4])

def planets():
    imageMode(CENTER)
    for i in range(0, 6):
        image(img_list[i], xpos[i], ypos[i], planet_size[i], planet_size[i])
        angle_list[i] += angle_factor[i]*speed # Geschwindigkeit der Planeten
        if angle_list[i] > 2*PI: # Nach einer Umdrehung wird der Counter um 1 erhöht
            counter_list[i] += 1
            angle_list[i] = 0
        
def ui_umlaufbahnen():
    textAlign(LEFT)
    if a == 1: # auf Rechtsklick ändert sich der Text von "Umlaufbahnen ein" zu "Umlaufbahnen aus" und umgekehrt
        fill(255)
        textSize(width/90)
        textAlign(LEFT)
        text("Umlaufbahnen ein", width*0.86, height*0.24)
        stroke(255,59,119)
        strokeWeight(height/200)
        line(width*0.86, height*0.25, width*0.96, height*0.25)
    elif a == -1:
        fill(255)
        textSize(width/90)
        text("Umlaufbahnen aus", width*0.86, height*0.24)
    fill(255,59,119)
    textSize(width/150)
    text("Press Right Mouse Button", width*0.86, height*0.27)
    
def ui_planetennamen():
    textAlign(LEFT)
    if b == 1: # auf Linksklick ändert sich der Text von "Planetennamen ein" zu "Planetennamen aus" und umgekehrt
        fill(255)
        textSize(width/90)
        text("Planetennamen ein", width*0.86, height*0.14)
        stroke(255,59,119)
        strokeWeight(height/200)
        line(width*0.86, height*0.15, width*0.962, height*0.15)
    elif b == -1:
        fill(255)
        textSize(width/90)
        text("Planetennamen aus", width*0.86, height*0.14)
    fill(255,59,119)
    textSize(width/150)
    text("Press Left Mouse Button", width*0.86, height*0.17)
    
# Ansicht für Anzahl Umrundungen der Planeten
def umrundungen():
    fill(255)
    textSize(width/70)
    textAlign(LEFT)
    text("Umrundungen", width*0.03, height*0.09)
    stroke(255)
    strokeWeight(height/200)
    line(width*0.03, height*0.1, width*0.13, height*0.1)
    textSize(width/100)
    for i in range(0, 6):
        text(namen[i] + ": ", width*0.03, height*offset[i])
        text(str(counter_list[i]), width*0.1, height*offset[i])
    fill(255,59,119)
    textSize(width/120)
    text("Press 'X' For Reset", width*0.03, height*0.45)
    
def counter_reset():
    if keyPressed:
        if key == "x" or key == "X": # Wenn die Taste x gedrückt wird, werden alle Counter auf 0 zurückgesetzt
            for i in range(0, 6):
                counter_list[i] = 0
            
def pfeil(): # Pfeil, der anzeigen soll, wie die Geschwindigkeit über die X-Achse variiert werden kann
    fill(255)
    stroke(255)
    line(width*0.86, height*0.85, width*0.96, height*0.85)
    line(width*0.86, height*0.85, width*0.87, height*0.86)
    line(width*0.86, height*0.85, width*0.87, height*0.84)
    line(width*0.96, height*0.85, width*0.95, height*0.86)
    line(width*0.96, height*0.85, width*0.95, height*0.84)
    textSize(width/130)
    text("slow", width*0.86, height*0.88)
    text("fast", width*0.95, height*0.88)
    
def mouseClicked():
    global a
    global b
    if mouseButton == RIGHT:
        a = a * -1
    if mouseButton == LEFT:
        b = b * -1
        
def exitbutton(): # Wenn der Exit-Button oben rechts geklickt wird, wird das Programm geschlossen
    noStroke()
    fill(255,59,119)
    rect(width*39/40, 0, width*1/40, width*1/40)
    stroke(255)
    line(width/1.02, height*0.01, width/1.005, height*0.035)
    line(width/1.005, height*0.01, width/1.02, height*0.035)
    if mouseX in range(width*39/40, width) and mouseY in range(0, width*1/40) and mousePressed == True:
        exit()

def rakete(): # Easter Egg 1: Beim Drücken der Taste 1 folgt zunächst ein Countdown für 10 Sekunden. Danach steigt eine Rakete in die Höhe.
    global start_rakete
    global presstime
    image(img_list[6], width/5, offset[6]+height*1.2, width/20, width/20)
    if keyPressed:
        if key == "1" and start_rakete == 0:
            start_rakete = 1
            presstime = millis()
            audio_list[0].rewind()
    if start_rakete == 1:
        audio_list[0].play()
        if presstime + 10000 <= millis():
            offset[6] -= height/225
        if offset[6] <= -height*1.2:
            offset[6] = 0
            start_rakete = 0

def verfolgung(): # Easter Egg 2: Beim Drücken der Taste 2 erscheint ein Astronaut, der von einem Alien verfolgt wird. Nach 2 Sekunden wird dieser vom Alien niedergeschossen.
    global start_verfolgung
    global presstime2
    image(img_list[7], offset[7]-width/20, height/2, width/40, width/40)
    image(img_list[8], offset[7]-width/4, height/2, width/40, width/40)
    if keyPressed:
        if key == "2" and start_verfolgung == 0:
            start_verfolgung = 1    
            presstime2 = millis()
            audio_list[1].rewind()
    if start_verfolgung == 1:
        offset[7] += width/300
        if presstime2 + 2000 <= millis():
            audio_list[1].play()
            offset[8] += width/299
            stroke(255,0,0)
            line(offset[7]-width/4+offset[8], height/2, offset[7]-width/4.5+offset[8], height/2)
        if offset[7]-width/4.5+offset[8] >= offset[7]-width/20:
            fill(255,0,0)
            arc(offset[7]-width/19.5, height/2, width/300, width/300, 0, 2*PI)
    if offset[7] >= width+width/4:
        offset[7] = 0
        start_verfolgung = 0
        offset[8] = 0
