# Globale Variabeln
displayWidth = 1920
displayHeight = 1080

size_sonne = displayWidth/50
size_merkur = displayWidth/180

# Vektorenpunkte der Himmelskörper bestimmen
v_sonne = PVector(displayWidth/2, displayHeight/2)
v_merkur = PVector(displayWidth/2.2, displayHeight/2.2)

# Winkel zwischen Vektorenpunkten bestimmen + Radius
angle_merkur = PVector.angleBetween(v_sonne, v_merkur)
radius_merkur = dist(v_sonne[0], v_sonne[1], v_merkur[0], v_merkur[1])

def setup():
    fullScreen()
    ellipseMode(RADIUS)
    frameRate(120)
    
def draw():
    global angle_merkur
    background(255)

    #Sonne
    stroke(0)
    strokeWeight(size_sonne/8)
    fill(255)
    ellipse(v_sonne[0], v_sonne[1], size_sonne, size_sonne)
    
    #Positionierung
    x_merkur = v_sonne[0] + cos(angle_merkur)*(radius_merkur*1.2)
    y_merkur = v_sonne[1] + sin(angle_merkur)*radius_merkur
    
    #Merkur
    stroke(0)
    strokeWeight(size_merkur/8)
    fill(255)
    ellipse(x_merkur, y_merkur, size_merkur, size_merkur)
    angle_merkur += PI/88
