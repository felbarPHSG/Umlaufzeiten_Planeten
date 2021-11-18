# globale Variablen
a = -1
b = -1
counter_merkur = 0
counter_venus = 0
counter_erde = 0
counter_mars = 0
counter_jupiter = 0
counter_saturn = 0

def settings():
    global size_sonne
    global size_merkur
    global size_venus
    global size_erde
    global size_mars
    global size_jupiter
    global size_saturn
    global v_sonne
    global v_merkur
    global v_venus
    global v_erde
    global v_mars
    global v_jupiter
    global v_saturn
    global angle_merkur
    global radius_merkur
    global angle_venus
    global radius_venus
    global angle_erde
    global radius_erde
    global angle_mars
    global radius_mars
    global angle_jupiter
    global radius_jupiter
    global angle_saturn
    global radius_saturn
    global width
    global height
    
    fullScreen()
    size_sonne = width/50
    size_merkur = width/120
    size_venus = width/70
    size_erde = width/70
    size_mars = width/90
    size_jupiter = width/50
    size_saturn = width/50

    # Vektorenpunkte der Himmelskörper bestimmen
    v_sonne = PVector(width/2, height/2)
    v_merkur = PVector(width/2.2, height/2.2)
    v_venus = PVector(width/2.4, height/2.4)
    v_erde = PVector(width/2.6, height/2.6)
    v_mars = PVector(width/2.9, height/2.9)
    v_jupiter = PVector(width/3.2, height/3.2)
    v_saturn = PVector(width/3.65, height/3.65)

    # Winkel zwischen Vektorenpunkten bestimmen + Radius
    angle_merkur = PVector.angleBetween(v_sonne, v_merkur)
    radius_merkur = dist(v_sonne[0], v_sonne[1], v_merkur[0], v_merkur[1])
    angle_venus = PVector.angleBetween(v_sonne, v_venus)
    radius_venus = dist(v_sonne[0], v_sonne[1], v_venus[0], v_venus[1])
    angle_erde = PVector.angleBetween(v_sonne, v_erde)
    radius_erde = dist(v_sonne[0], v_sonne[1], v_erde[0], v_erde[1])
    angle_mars = PVector.angleBetween(v_sonne, v_mars)
    radius_mars = dist(v_sonne[0], v_sonne[1], v_mars[0], v_mars[1])
    angle_jupiter = PVector.angleBetween(v_sonne, v_jupiter)
    radius_jupiter = dist(v_sonne[0], v_sonne[1], v_jupiter[0], v_jupiter[1])
    angle_saturn = PVector.angleBetween(v_sonne, v_saturn)
    radius_saturn = dist(v_sonne[0], v_sonne[1], v_saturn[0], v_saturn[1])

def setup():
    global img_merkur
    global img_venus
    global img_erde
    global img_mars
    global img_jupiter
    global img_saturn
    fullScreen()
    ellipseMode(RADIUS)
    frameRate(120)
    img_merkur = loadImage("Merkur.png")
    img_venus = loadImage("Venus.png")
    img_erde = loadImage("Erde.png")
    img_mars = loadImage("Mars.png")
    img_jupiter = loadImage("Jupiter.png")
    img_saturn = loadImage("Saturn.png")

def draw():
    global speed
    background(10,10,45)
    speed = pow(mouseX/(0.5*width), 2)*5
    
    positionierung()
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
        
def positionierung():
    global x_merkur
    global y_merkur
    global x_venus
    global y_venus
    global x_erde
    global y_erde
    global x_mars
    global y_mars
    global x_jupiter
    global y_jupiter
    global x_saturn
    global y_saturn
    x_merkur = v_sonne[0] + sin(angle_merkur)*(radius_merkur*1.2)
    y_merkur = v_sonne[1] + cos(angle_merkur)*radius_merkur
    x_venus = v_sonne[0] + sin(angle_venus)*(radius_venus*1.2)
    y_venus = v_sonne[1] + cos(angle_venus)*radius_venus
    x_erde = v_sonne[0] + sin(angle_erde)*(radius_erde*1.2)
    y_erde = v_sonne[1] + cos(angle_erde)*radius_erde
    x_mars = v_sonne[0] + sin(angle_mars)*(radius_mars*1.2)
    y_mars = v_sonne[1] + cos(angle_mars)*radius_mars
    x_jupiter = v_sonne[0] + sin(angle_jupiter)*(radius_jupiter*1.2)
    y_jupiter = v_sonne[1] + cos(angle_jupiter)*radius_jupiter
    x_saturn = v_sonne[0] + sin(angle_saturn)*(radius_saturn*1.2)
    y_saturn = v_sonne[1] + cos(angle_saturn)*radius_saturn
        
def umlaufbahnen():
    if a == 1:
        noFill()
        stroke(255,60)
        strokeWeight(width/300)
        ellipse(v_sonne[0], v_sonne[1], radius_merkur*1.2, radius_merkur)
        ellipse(v_sonne[0], v_sonne[1], radius_venus*1.2, radius_venus)
        ellipse(v_sonne[0], v_sonne[1], radius_erde*1.2, radius_erde)
        ellipse(v_sonne[0], v_sonne[1], radius_mars*1.2, radius_mars)
        ellipse(v_sonne[0], v_sonne[1], radius_jupiter*1.2, radius_jupiter)
        ellipse(v_sonne[0], v_sonne[1], radius_saturn*1.2, radius_saturn)
        
def planetennamen():
    if b == 1:
        fill(255)
        textSize(width/100)
        textAlign(CENTER)
        text("Merkur", x_merkur, y_merkur+size_merkur*2)
        text("Venus", x_venus, y_venus+size_venus*1.3)
        text("Erde", x_erde, y_erde+size_erde*1.4)
        text("Mars", x_mars, y_mars+size_mars*1.6)
        text("Jupiter", x_jupiter, y_jupiter+size_jupiter*1.1)
        text("Saturn", x_saturn, y_saturn+size_saturn*1.1)
        
def sonne():
    stroke(240,120,50)
    strokeWeight(size_sonne/8)
    fill(255,230,5)
    ellipse(v_sonne[0], v_sonne[1], size_sonne, size_sonne)
    
def merkur():
    global angle_merkur
    global counter_merkur
    imageMode(CENTER)
    image(img_merkur, x_merkur, y_merkur, size_merkur, size_merkur)
    angle_merkur += (PI/88)*speed
    if angle_merkur > 2*PI:
        counter_merkur += 1
        angle_merkur = 0
        
def venus():
    global angle_venus
    global counter_venus
    image(img_venus, x_venus, y_venus, size_venus, size_venus)
    angle_venus += (PI/225)*speed
    if angle_venus > 2*PI:
        counter_venus += 1
        angle_venus = 0
        
def erde():
    global angle_erde
    global counter_erde
    image(img_erde, x_erde, y_erde, size_erde, size_erde)
    angle_erde += (PI/365)*speed 
    if angle_erde > 2*PI:
        counter_erde += 1
        angle_erde = 0
        
def mars():
    global angle_mars
    global counter_mars
    image(img_mars, x_mars, y_mars, size_mars, size_mars)
    angle_mars += (PI/687)*speed
    if angle_mars > 2*PI:
        counter_mars += 1
        angle_mars = 0
        
def jupiter():
    global angle_jupiter
    global counter_jupiter
    image(img_jupiter, x_jupiter, y_jupiter, size_jupiter, size_jupiter)
    angle_jupiter += (PI/4330)*speed
    if angle_jupiter > 2*PI:
        counter_jupiter += 1
        angle_jupiter = 0
        
def saturn():
    global angle_saturn
    global counter_saturn
    image(img_saturn, x_saturn, y_saturn, size_saturn, size_saturn)
    angle_saturn += (PI/10585)*speed
    if angle_saturn > 2*PI:
        counter_saturn += 1
        angle_saturn = 0 
        
def ui_umlaufbahnen():
    textAlign(LEFT)
    if a == 1:
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
    text("Press Left Mouse Button", width*0.86, height*0.17)
    
def ui_planetennamen():
    textAlign(LEFT)
    if b == 1:
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
    text("Press Right Mouse Button", width*0.86, height*0.27)
    
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
        if key == "x" or key == "X":
            counter_merkur = 0
            counter_venus = 0
            counter_erde = 0
            counter_mars = 0
            counter_jupiter = 0
            counter_saturn = 0
            
def pfeil():
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
        
def exitbutton():
    noStroke()
    fill(255,59,119)
    rect(width*39/40, 0, width*1/40, width*1/40)
    stroke(255)
    line(width/1.02, height*0.01, width/1.005, height*0.035)
    line(width/1.005, height*0.01, width/1.02, height*0.035)
    if mouseX in range(width*39/40, width) and mouseY in range(0, width*1/40) and mousePressed == True:
        exit()
