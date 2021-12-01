# globale Variablen
add_library('minim') # Abspielen von Audiodateien mit Hilfe der "Minim" Library
a = -1
b = -1
start_rakete = 0
offset_rakete = 0
start_verfolgung = 0
offset_verfolgung = 0
offset_laser = 0
presstime = 0
presstime2 = 0
counter_venus = 0
counter_merkur = 0
counter_erde = 0
counter_mars = 0
counter_jupiter = 0
counter_saturn = 0
angle_merkur = 0
angle_venus = 0
angle_erde = 0
angle_mars = 0
angle_jupiter = 0
angle_saturn = 0
    
def setup():
    fullScreen()
    global img_merkur
    global img_venus
    global img_erde
    global img_mars
    global img_jupiter
    global img_saturn
    global img_rakete
    global img_astronaut
    global img_ufo
    global countdown
    global laser
    fullScreen()
    ellipseMode(RADIUS)
    frameRate(120)
    # Bilder für Planeten laden
    img_merkur = loadImage("Merkur.png")
    img_venus = loadImage("Venus.png")
    img_erde = loadImage("Erde.png")
    img_mars = loadImage("Mars.png")
    img_jupiter = loadImage("Jupiter.png")
    img_saturn = loadImage("Saturn.png")
    img_rakete = loadImage("Rakete.png")
    img_astronaut = loadImage("Astronaut.png")
    img_ufo = loadImage("Ufo.png")
    minim = Minim(this)
    countdown = minim.loadFile("Countdown.mp3")
    laser = minim.loadFile("Laser.mp3")

def draw():
    global speed
    global v_dict
    global merkur_dict
    global venus_dict
    global erde_dict
    global mars_dict
    global jupiter_dict
    global saturn_dict
    background(10,10,45)
    speed = pow(mouseX/(0.5*width), 2)*4 # Geschwindigkeit nimmt auf der X-Achse nach rechts zu, nach links ab

    # Dictionary für Vektorpunkte der Himmelskörper, um nachher den Abstand zwischen Planeten und Sonne zu berechnen
    v_dict = {
              'sonne' : PVector(width/2, height/2),
              'merkur' : PVector(width/2.2, height/2.2),
              'venus' : PVector(width/2.4, height/2.4),
              'erde' : PVector(width/2.6, height/2.6),
              'mars' : PVector(width/2.9, height/2.9),
              'jupiter' : PVector(width/3.2, height/3.2),
              'saturn' : PVector(width/3.65, height/3.65)
              }

    #Dictionaries für Planeten: Grösse, Abstand zur Sonne, Positionen x und y 
    merkur_dict = {
                   'size' : width/120,
                   'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['merkur'][0], v_dict['merkur'][1]),
                   'x' : v_dict['sonne'][0] + sin(angle_merkur)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['merkur'][0], v_dict['merkur'][1])*1.2),
                   'y' : v_dict['sonne'][1] + cos(angle_merkur)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['merkur'][0], v_dict['merkur'][1]),
                   }
    
    venus_dict = {
                   'size' : width/70,
                   'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['venus'][0], v_dict['venus'][1]),
                   'x' : v_dict['sonne'][0] + sin(angle_venus)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['venus'][0], v_dict['venus'][1])*1.2),
                   'y' : v_dict['sonne'][1] + cos(angle_venus)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['venus'][0], v_dict['venus'][1])
                   }
    
    erde_dict = {
                 'size' : width/70,
                 'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['erde'][0], v_dict['erde'][1]),
                 'x' : v_dict['sonne'][0] + sin(angle_erde)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['erde'][0], v_dict['erde'][1])*1.2),
                 'y' : v_dict['sonne'][1] + cos(angle_erde)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['erde'][0], v_dict['erde'][1])
                 }

    mars_dict = {
                 'size' : width/90,
                 'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['mars'][0], v_dict['mars'][1]),
                 'x' : v_dict['sonne'][0] + sin(angle_mars)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['mars'][0], v_dict['mars'][1])*1.2),
                 'y' : v_dict['sonne'][1] + cos(angle_mars)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['mars'][0], v_dict['mars'][1])
                 }
    
    jupiter_dict = {
                 'size' : width/50,
                 'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['jupiter'][0], v_dict['jupiter'][1]),
                 'x' : v_dict['sonne'][0] + sin(angle_jupiter)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['jupiter'][0], v_dict['jupiter'][1])*1.2),
                 'y' : v_dict['sonne'][1] + cos(angle_jupiter)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['jupiter'][0], v_dict['jupiter'][1])
                 }
    
    saturn_dict = {
                 'size' : width/50,
                 'radius' : dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['saturn'][0], v_dict['saturn'][1]),
                 'x' : v_dict['sonne'][0] + sin(angle_saturn)*(dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['saturn'][0], v_dict['saturn'][1])*1.2),
                 'y' : v_dict['sonne'][1] + cos(angle_saturn)*dist(v_dict['sonne'][0], v_dict['sonne'][1], v_dict['saturn'][0], v_dict['saturn'][1])
                 }
    
    # Abrufen der unten definierten Funktionen
    umlaufbahnen()
    planetennamen()
    sonne()
    merkur()
    venus()
    erde()
    mars()
    jupiter()
    saturn()
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
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], merkur_dict['radius']*1.2, merkur_dict['radius'])
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], venus_dict['radius']*1.2, venus_dict['radius'])
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], erde_dict['radius']*1.2, erde_dict['radius'])
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], mars_dict['radius']*1.2, mars_dict['radius'])
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], jupiter_dict['radius']*1.2, jupiter_dict['radius'])
        ellipse(v_dict['sonne'][0], v_dict['sonne'][1], saturn_dict['radius']*1.2, saturn_dict['radius'])
        
def planetennamen(): # Wenn die linke Maustaste gedrückt wird, werden die Planetennamen ein- oder ausgeblendet
    if b == 1:
        fill(255)
        textSize(width/100)
        textAlign(CENTER)
        text("Merkur", merkur_dict['x'], merkur_dict['y']+merkur_dict['size']*2)
        text("Venus", venus_dict['x'], venus_dict['y']+venus_dict['size']*1.3)
        text("Erde", erde_dict['x'], erde_dict['y']+erde_dict['size']*1.4)
        text("Mars", mars_dict['x'], mars_dict['y']+mars_dict['size']*1.6)
        text("Jupiter", jupiter_dict['x'], jupiter_dict['y']+jupiter_dict['size']*1.1)
        text("Saturn", saturn_dict['x'], saturn_dict['y']+saturn_dict['size']*1.1)
        
def sonne():
    size_sonne = width/50
    stroke(240,120,50)
    strokeWeight(size_sonne/8)
    fill(255,230,5)
    ellipse(v_dict['sonne'][0], v_dict['sonne'][1], size_sonne, size_sonne)
    
def merkur():
    global angle_merkur
    global counter_merkur
    imageMode(CENTER)
    image(img_merkur, merkur_dict['x'], merkur_dict['y'], merkur_dict['size'], merkur_dict['size'])
    angle_merkur += (PI/88)*speed
    if angle_merkur > 2*PI: # Wenn der Planet die Sonne einmal umkreist hat (2*PI), wird der Counter um eins erhöht
        counter_merkur += 1
        angle_merkur = 0
        
def venus():
    global angle_venus
    global counter_venus
    image(img_venus, venus_dict['x'], venus_dict['y'], venus_dict['size'], venus_dict['size'])
    angle_venus += (PI/225)*speed
    if angle_venus > 2*PI:
        counter_venus += 1
        angle_venus = 0
        
def erde():
    global angle_erde
    global counter_erde
    image(img_erde, erde_dict['x'], erde_dict['y'], erde_dict['size'], erde_dict['size'])
    angle_erde += (PI/365)*speed 
    if angle_erde > 2*PI:
        counter_erde += 1
        angle_erde = 0
        
def mars():
    global angle_mars
    global counter_mars
    image(img_mars, mars_dict['x'], mars_dict['y'], mars_dict['size'], mars_dict['size'])
    angle_mars += (PI/687)*speed
    if angle_mars > 2*PI:
        counter_mars += 1
        angle_mars = 0
        
def jupiter():
    global angle_jupiter
    global counter_jupiter
    image(img_jupiter, jupiter_dict['x'], jupiter_dict['y'], jupiter_dict['size'], jupiter_dict['size'])
    angle_jupiter += (PI/4330)*speed
    if angle_jupiter > 2*PI:
        counter_jupiter += 1
        angle_jupiter = 0
        
def saturn():
    global angle_saturn
    global counter_saturn
    image(img_saturn, saturn_dict['x'], saturn_dict['y'], saturn_dict['size'], saturn_dict['size'])
    angle_saturn += (PI/10585)*speed
    if angle_saturn > 2*PI:
        counter_saturn += 1
        angle_saturn = 0 
        
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
    text("Merkur: ", width*0.03, height*0.15)
    text(str(counter_merkur), width*0.1, height*0.15)
    text("Venus: ", width*0.03, height*0.2)
    text(str(counter_venus), width*0.1, height*0.2)
    text("Erde: ", width*0.03, height*0.25)
    text(str(counter_erde), width*0.1, height*0.25)
    text("Mars: ", width*0.03, height*0.3)
    text(str(counter_mars), width*0.1, height*0.3)
    text("Jupiter: ", width*0.03, height*0.35)
    text(str(counter_jupiter), width*0.1, height*0.35)
    text("Saturn: ", width*0.03, height*0.4)
    text(str(counter_saturn), width*0.1, height*0.4)
    fill(255,59,119)
    textSize(width/120)
    text("Press 'X' For Reset", width*0.03, height*0.45)
    
def counter_reset():
    global counter_merkur
    global counter_venus
    global counter_erde
    global counter_merkur
    global counter_mars
    global counter_jupiter
    global counter_saturn
    if keyPressed:
        if key == "x" or key == "X": # Wenn die Taste x gedrückt wird, werden alle Counter auf 0 zurückgesetzt
            counter_merkur = 0
            counter_venus = 0
            counter_erde = 0
            counter_mars = 0
            counter_jupiter = 0
            counter_saturn = 0
            
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
    global offset_rakete
    global start_rakete
    global presstime
    image(img_rakete, width/5, offset_rakete+height*1.2, width/20, width/20)
    if keyPressed:
        if key == "1" and start_rakete == 0:
            start_rakete = 1
            presstime = millis()
            countdown.rewind()
    if start_rakete == 1:
        countdown.play()
        if presstime + 10000 <= millis():
            offset_rakete -= height/225
        if offset_rakete <= -height*1.2:
            offset_rakete = 0
            start_rakete = 0

def verfolgung(): # Easter Egg 2: Beim Drücken der Taste 2 erscheint ein Astronaut, der von einem Alien verfolgt wird. Nach 2 Sekunden wird dieser vom Alien niedergeschossen.
    global offset_laser
    global start_verfolgung
    global offset_verfolgung
    global presstime2
    image(img_astronaut, offset_verfolgung-width/20, height/2, width/40, width/40)
    image(img_ufo, offset_verfolgung-width/4, height/2, width/40, width/40)
    if keyPressed:
        if key == "2" and start_verfolgung == 0:
            start_verfolgung = 1    
            presstime2 = millis()
            laser.rewind()
    if start_verfolgung == 1:
        offset_verfolgung += width/300
        if presstime2 + 2000 <= millis():
            laser.play()
            offset_laser += width/299
            stroke(255,0,0)
            line(offset_verfolgung-width/4+offset_laser, height/2, offset_verfolgung-width/4.5+offset_laser, height/2)
        if offset_verfolgung-width/4.5+offset_laser >= offset_verfolgung-width/20:
            fill(255,0,0)
            arc(offset_verfolgung-width/19.5, height/2, width/300, width/300, 0, 2*PI)
    if offset_verfolgung >= width+width/4:
        offset_verfolgung = 0
        start_verfolgung = 0
        offset_laser = 0
