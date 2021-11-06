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
    
    #Venus
    strokeWeight(size_venus/6)
    fill(191,112,42)
    ellipse(x_venus, y_venus, size_venus, size_venus)
    angle_venus += (PI/225)*speed
    
    #Erde
    strokeWeight(size_erde/6)
    fill(44,108,191)
    ellipse(x_erde, y_erde, size_erde, size_erde)
    angle_erde += (PI/365)*speed 
        
    #Mars
    strokeWeight(size_mars/6)
    fill(191,69,57)
    ellipse(x_mars, y_mars, size_mars, size_mars)
    angle_mars += (PI/687)*speed
    
    #Jupiter
    strokeWeight(size_jupiter/6)
    fill(140,128,112)
    ellipse(x_jupiter, y_jupiter, size_jupiter, size_jupiter)
    angle_jupiter += (PI/4330)*speed
    
    #Saturn
    strokeWeight(size_saturn/6)
    fill(241,216,146)
    ellipse(x_saturn, y_saturn, size_saturn, size_saturn)
    strokeWeight(size_saturn/4)
    arc(x_saturn, y_saturn, size_saturn*1.5, size_saturn/3, -QUARTER_PI, PI+QUARTER_PI)
    angle_saturn += (PI/10585)*speed

def mouseClicked():
    global a
    global b
    if mouseButton == RIGHT:
        a = a * -1
    if mouseButton == LEFT:
        b = b * -1
    
