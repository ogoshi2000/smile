def setup():
    size(400,400)
    frameRate(20)
    fullScreen()

    
number=100
radius=300
circle_size=50
max_circle=80

def draw():
    global number,radius,circle_size,max_circle
    if g < max_circle/2:
        circle_size=g
    else:
        circle_size=max_circle-g
        
    k=frameCount%number
    if k < number/2:
        j=k
    else:
        j=number-k
    #background(random(125),random(125),random(125))
    background(0)
    
    
    fill(random(255),random(255),random(255),random(200,255))
    circle(radius*2+random(-5,5),radius*1.5+random(-5,5),radius/2*PI)
    fill(random(255),random(255),random(255),random(200,255))
    eyesize=random((radius/2*PI)*0.125,(radius/2*PI)*0.25)
    circle(radius*2-radius*0.4,radius*1.5,eyesize)
    circle(radius*2+radius*0.4,radius*1.5,eyesize)
    fill(0)
    pupille=random((radius/2*PI)*0.125)
    circle(radius*2+radius*0.4,radius*1.5,pupille)
    circle(radius*2-radius*0.4,radius*1.5,pupille)
    
    
    
    strokeWeight(random(50))
    stroke(0)
    line(radius*2-radius*0.4,radius*1.5+radius*0.4,radius*2+radius*0.4,radius*1.5+radius*0.4)
    noStroke()
    

    

        
        
