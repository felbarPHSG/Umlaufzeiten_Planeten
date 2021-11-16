# Globale Variabeln
displayWidth = 1920
displayHeight = 1080

size_sonne = displayWidth/50
size_merkur = displayWidth/180
size_venus = displayWidth/130
size_erde = displayWidth/130
size_mars = displayWidth/155
size_jupiter = displayWidth/100
size_saturn = displayWidth/110
a = -1
b = -1
counter_merkur = 0
counter_venus = 0
counter_erde = 0
counter_mars = 0
counter_jupiter = 0
counter_saturn = 0

# Vektorenpunkte der Himmelskörper bestimmen
v_sonne = PVector(displayWidth/2, displayHeight/2)
v_merkur = PVector(displayWidth/2.2, displayHeight/2.2)
v_venus = PVector(displayWidth/2.4, displayHeight/2.4)
v_erde = PVector(displayWidth/2.7, displayHeight/2.7)
v_mars = PVector(displayWidth/3, displayHeight/3)
v_jupiter = PVector(displayWidth/3.3, displayHeight/3.3)
v_saturn = PVector(displayWidth/3.75, displayHeight/3.75)

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
    fullScreen()
    ellipseMode(RADIUS)
    frameRate(120)
    
def draw():
    background(10,10,45)
    speed = pow(mouseX/(0.5*displayWidth), 2)*3
    global angle_merkur
    global angle_venus
    global angle_erde
    global angle_mars
    global angle_jupiter
    global angle_saturn   
    global counter_merkur 
    global counter_venus
    global counter_erde
    global counter_mars
    global counter_jupiter
    global counter_saturn
    
    #Positionierung
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
    
    #Umlaufbahnen
    if a == 1:
        noFill()
        stroke(255,60)
        strokeWeight(displayWidth/300)
        ellipse(v_sonne[0], v_sonne[1], radius_merkur*1.2, radius_merkur)
        ellipse(v_sonne[0], v_sonne[1], radius_venus*1.2, radius_venus)
        ellipse(v_sonne[0], v_sonne[1], radius_erde*1.2, radius_erde)
        ellipse(v_sonne[0], v_sonne[1], radius_mars*1.2, radius_mars)
        ellipse(v_sonne[0], v_sonne[1], radius_jupiter*1.2, radius_jupiter)
        ellipse(v_sonne[0], v_sonne[1], radius_saturn*1.2, radius_saturn)
    
    #Planetennamen
    if b == 1:
        fill(255)
        textSize(displayWidth/100)
        text("Merkur", x_merkur-40, y_merkur+40)
        text("Venus", x_venus-35, y_venus+40)
        text("Erde", x_erde-25, y_erde+40)
        text("Mars", x_mars-30, y_mars+40)
        text("Jupiter", x_jupiter-35, y_jupiter+50)
        text("Saturn", x_saturn-40, y_saturn+40)
   
    #Sonne
    stroke(240,120,50)
    strokeWeight(size_sonne/8)
    fill(255,230,5)
    ellipse(v_sonne[0], v_sonne[1], size_sonne, size_sonne)
      
    #Merkur
    stroke(255)
    strokeWeight(size_merkur/6)
    fill(115,63,18)
    ellipse(x_merkur, y_merkur, size_merkur, size_merkur)
    angle_merkur += (PI/88)*speed
    if angle_merkur > 2*PI:
        counter_merkur += 1
        angle_merkur = 0
    
    #Venus
    strokeWeight(size_venus/6)
    fill(191,112,42)
    ellipse(x_venus, y_venus, size_venus, size_venus)
    angle_venus += (PI/225)*speed
    if angle_venus > 2*PI:
        counter_venus += 1
        angle_venus = 0
    
    #Erde
    strokeWeight(size_erde/6)
    fill(44,108,191)
    ellipse(x_erde, y_erde, size_erde, size_erde)
    angle_erde += (PI/365)*speed 
    if angle_erde > 2*PI:
        counter_erde += 1
        angle_erde = 0
        
    #Mars
    strokeWeight(size_mars/6)
    fill(191,69,57)
    ellipse(x_mars, y_mars, size_mars, size_mars)
    angle_mars += (PI/687)*speed
    if angle_mars > 2*PI:
        counter_mars += 1
        angle_mars = 0
    
    #Jupiter
    strokeWeight(size_jupiter/6)
    fill(140,128,112)
    ellipse(x_jupiter, y_jupiter, size_jupiter, size_jupiter)
    angle_jupiter += (PI/4330)*speed
    if angle_jupiter > 2*PI:
        counter_jupiter += 1
        angle_jupiter = 0
    
    #Saturn
    strokeWeight(size_saturn/6)
    fill(241,216,146)
    ellipse(x_saturn, y_saturn, size_saturn, size_saturn)
    strokeWeight(size_saturn/4)
    arc(x_saturn, y_saturn, size_saturn*1.5, size_saturn/3, -QUARTER_PI, PI+QUARTER_PI)
    angle_saturn += (PI/10585)*speed
    if angle_saturn > 2*PI:
        counter_saturn += 1
        angle_saturn = 0    
    
    #Umlaufbahnen ein-/ausschalten
    if a == 1:
        fill(255)
        textSize(displayWidth/90)
        text("Umlaufbahnen ein", displayWidth*0.86, displayHeight*0.24)
        stroke(255,59,119)
        strokeWeight(5)
        line(displayWidth*0.86, displayHeight*0.25, displayWidth*0.96, displayHeight*0.25)

    elif a == -1:
        fill(255)
        textSize(displayWidth/90)
        text("Umlaufbahnen aus", displayWidth*0.86, displayHeight*0.24)
        
    fill(255,59,119)
    textSize(displayWidth/150)
    text("Press Left Mouse Button", displayWidth*0.86, displayHeight*0.17)
        
    #Planetennamen ein-/ausschalten
    if b == 1:
        fill(255)
        textSize(displayWidth/90)
        text("Planetennamen ein", displayWidth*0.86, displayHeight*0.14)
        stroke(255,59,119)
        strokeWeight(5)
        line(displayWidth*0.86, displayHeight*0.15, displayWidth*0.962, displayHeight*0.15)
    
    elif b == -1:
        fill(255)
        textSize(displayWidth/90)
        text("Planetennamen aus", displayWidth*0.86, displayHeight*0.14)
        
    fill(255,59,119)
    textSize(displayWidth/150)
    text("Press Right Mouse Button", displayWidth*0.86, displayHeight*0.27)
        
    #Umrundungen
    fill(255)
    textSize(displayWidth/70)
    text("Umrundungen", displayWidth*0.03, displayHeight*0.09)
    stroke(255)
    strokeWeight(5)
    line(displayWidth*0.03, displayHeight*0.1, displayWidth*0.13, displayHeight*0.1)
    textSize(displayWidth/100)
    text("Merkur: ", displayWidth*0.03, displayHeight*0.15)
    text(str(counter_merkur), displayWidth*0.1, displayHeight*0.15)
    text("Venus: ", displayWidth*0.03, displayHeight*0.2)
    text(str(counter_venus), displayWidth*0.1, displayHeight*0.2)
    text("Erde: ", displayWidth*0.03, displayHeight*0.25)
    text(str(counter_erde), displayWidth*0.1, displayHeight*0.25)
    text("Mars: ", displayWidth*0.03, displayHeight*0.3)
    text(str(counter_mars), displayWidth*0.1, displayHeight*0.3)
    text("Jupiter: ", displayWidth*0.03, displayHeight*0.35)
    text(str(counter_jupiter), displayWidth*0.1, displayHeight*0.35)
    text("Saturn: ", displayWidth*0.03, displayHeight*0.4)
    text(str(counter_saturn), displayWidth*0.1, displayHeight*0.4)
    fill(255,59,119)
    textSize(displayWidth/120)
    text("Press 'X' For Reset", displayWidth*0.03, displayHeight*0.45)
    
    # Counter Reset
    if keyPressed:
        if key == "x" or key == "X":
            counter_merkur = 0
            counter_venus = 0
            counter_erde = 0
            counter_mars = 0
            counter_jupiter = 0
            counter_saturn = 0
    
    # Pfeil
    fill(255)
    stroke(255)
    line(displayWidth*0.86, displayHeight*0.85, displayWidth*0.96, displayHeight*0.85)
    line(displayWidth*0.86, displayHeight*0.85, displayWidth*0.87, displayHeight*0.86)
    line(displayWidth*0.86, displayHeight*0.85, displayWidth*0.87, displayHeight*0.84)
    line(displayWidth*0.96, displayHeight*0.85, displayWidth*0.95, displayHeight*0.86)
    line(displayWidth*0.96, displayHeight*0.85, displayWidth*0.95, displayHeight*0.84)
    textSize(displayWidth/130)
    text("slow", displayWidth*0.86, displayHeight*0.88)
    text("fast", displayWidth*0.95, displayHeight*0.88)

def mouseClicked():
    global a
    global b
    if mouseButton == RIGHT:
        a = a * -1
    if mouseButton == LEFT:
        b = b * -1
