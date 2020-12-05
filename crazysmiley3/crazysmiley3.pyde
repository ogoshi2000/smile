def setup():
    size(400,400)
    frameRate(30)
    fullScreen()

    
number=100
radius=300
circle_size=50
max_circle=80

def draw():
    global number,radius,circle_size,max_circle
    g=(frameCount%max_circle)
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
    
    #rotation face
    i=(frameCount%1000)
    x=sin(2*PI/1000-i)*20
    y=cos(2*PI/1000-i)*20

    
    
    
    fill(random(255),random(255),random(255),random(200,255))#main circle face
    circle(radius*2+random(-5,5),radius*1.5+random(-5,5),radius/2*PI)
    
    fill(random(255),random(255),random(255),random(200,255))#eyes 
    eyesize=random((radius/2*PI)*0.125,(radius/2*PI)*0.25)
    circle(x+radius*2-radius*0.4,y+radius*1.5,eyesize)
    circle(x+radius*2+radius*0.4,y+radius*1.5,eyesize)
    fill(0)
    pupille=random((radius/2*PI)*0.125)
    circle(x+radius*2+radius*0.4,y+radius*1.5,pupille)
    circle(x+radius*2-radius*0.4,y+radius*1.5,pupille)
    
    strokeWeight(random(50))#mouth
    stroke(0)
    l=random(0.1,0.3)
    line(x+radius*2-radius*l,y+radius*1.5+radius*0.4,x+radius*2+radius*l,y+radius*1.5+radius*0.4)
    noStroke()
    
    #outer circles
    for i in range(0,j): 
        x=(2*PI/j*i)
        x2=(2*PI/j*i)
        radius2=radius*1.25
        radius3=radius*1.5
        noStroke()
        fill(random(255),random(255),random(255),random(200,255))
        circle(sin(x)*radius+radius*2,cos(x)*radius+radius*1.5,random(circle_size/2,circle_size))
        fill(random(255),random(255),random(255),random(200,255))
        circle(cos(x2)*radius2+radius*2,sin(x2)*radius2+radius*1.5,random(circle_size/2,circle_size*1.25))
        fill(random(255),random(255),random(255),random(200,255))
        circle(sin(x2)*radius3+radius*2,cos(x2)*radius3+radius*1.5,random(circle_size/2,circle_size*1.5))
        
        
