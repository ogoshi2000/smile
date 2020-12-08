def setup():
    global img
    img = loadImage("jvhs.jpg")
    size(400,400,P3D)
    frameRate(20)
    fullScreen()


class crazySmiley():
    def __init__(self,img):
        
        self._eye_size = 25
        self._mouth_size = (10,25)
        self.face_color=(random(255),random(255),random(255))
        self.eye_color=(random(255),random(255),random(255),random(100,255))
        self.img=img
        self._eye_offset = 0
        self._pupil_offset = 0
        self._mouth_offset = 0
        

    @property
    def eye_size(self):
        return self._eye_size + self._eye_offset
    
    @property
    def pupil_size(self):
        return min(self.eye_size, self.eye_size/2 + self._pupil_offset)
    
    @property
    def mouth_size(self):
        return (self._mouth_size[0] + self._mouth_offset*1.3, self._mouth_size[1]+self._mouth_offset)
    
    def draw(self):
        self.head()
        self.eyes()
        self.mouth()

    def head(self):
        pushMatrix()
        noStroke()
        fill(*self.face_color)
        head=createShape(SPHERE,100)
        head.setTexture(self.img)
        shape(head)
        #sphere()
        stroke(1)
        popMatrix()
    
    def eyes(self):
        pushMatrix()
        translate(0,0,100)
        noStroke()
        fill(*self.eye_color)
        circle(25,0,self.eye_size)
        circle(-25,0,self.eye_size)
    
        pushMatrix()
        fill(0)
        translate(0,0,1)
        circle(25,0,self.pupil_size)
        circle(-25,0,self.pupil_size)
        stroke(0)
        popMatrix()
        popMatrix()
        
    def mouth(self):
        pushMatrix()
        translate(0,0,100)
        strokeWeight(self.mouth_size[0])
        line(-self.mouth_size[1],30,self.mouth_size[1],30)
        strokeWeight(1)
        popMatrix()
        
    def place(self,x=0,y=0,z=0,deg_x=0,deg_y=0,deg_z=0,zoom=1.0):
        pushMatrix()
        
        translate(x,y,z)
        
        rotateX(radians(deg_x))
        rotateY(radians(deg_y))
        rotateZ(radians(deg_z))
        
        scale(zoom)
        self.draw()
        popMatrix()
        
    def randomize(self,eyes=0,pupils=0,mouth=0):
        self._eye_offset = eyes*random(-1,1)
        self._pupil_offset = pupils*random(-1,1)
        self._mouth_offset = mouth*random(-1,1)
    
            
def encircle(radius,num):
    for i in range(num):
        x = radius*sin(i*2*PI/num)
        y = radius*cos(i*2*PI/num)
        yield (x,y)


def crazyWheel(cs,i,radius,num,img):
    for coord in encircle(radius,num):
        cs=crazySmiley(img)
        cs.randomize(mouth=6,eyes=5,pupils=10)
        cs.place(*coord,z=0,deg_y=i*3,zoom=2.0)

def lfo(period,shape='saw'):
    if shape=='saw':
        return abs(frameCount%period-period/2.0)/period
    elif shape=='square':
        return (frameCount//period)%2
    elif shape=='sine':
        return sin(frameCount*2*PI/period)


def draw():
    global img
    background(0)
    i=frameCount%360
    
    pushMatrix()
    translate(600,400,0)
    
    #rotate(i/50.0)
    cs = crazySmiley(img)
    cs.place()
    radius =100*(lfo(50,'sine')+1)
    num = int(5*lfo(50)+7)
    #crazyWheel(cs,-i,radius*2.0,num,img)
    
    #cs.place(i,i,i*10)
    #cs=crazySmiley()
    #cs.randomize(eyes=2,pupils=10,mouth=10)
    #cs.place(100-i,100-i,0,1+i*0.01)
    popMatrix()
    #saveFrame('frames/###.png')
