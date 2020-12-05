def setup():
    size(400,400)
    frameRate(20)
    fullScreen()

class crazySmiley():
    def __init__(self):
        self._eye_size = 25
        self._mouth_size = (8,10)
        self.face_color=(random(255),random(255),random(255),random(150,255))
        self.eye_color=(random(255),random(255),random(255),random(255))

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
        noStroke()
        fill(*self.face_color)
        circle(0,0,100)
        stroke(0)
    
    def eyes(self):
        noStroke()
        fill(*self.eye_color)
        circle(25,0,self.eye_size)
        circle(-25,0,self.eye_size)
        fill(0)
        circle(25,0,self.pupil_size)
        circle(-25,0,self.pupil_size)
        stroke(0)
        
    def mouth(self):
        strokeWeight(self.mouth_size[0])
        line(-self.mouth_size[1],30,self.mouth_size[1],30)
        strokeWeight(1)
        
    def place(self,x,y,deg=0,zoom=1.0):
        pushMatrix()
        translate(x,y)
        rotate(radians(deg))
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


def crazyWheel(cs,i,radius,num):
    for coord in encircle(radius,num):
        cs=crazySmiley()
        cs.randomize(mouth=6,eyes=5,pupils=10)
        cs.place(*coord,deg=i*3,zoom=random(1.0,2.0))

def lfo(period,shape='saw'):
    if shape=='saw':
        return abs(frameCount%period-period/2.0)/period
    elif shape=='square':
        return (frameCount//period)%2
    elif shape=='sine':
        return sin(frameCount*2*PI/period)
    
def draw():
    translate(600,400)
    background(0)
    i=frameCount%300
    pushMatrix()
    rotate(-i/50.0)
    cs = crazySmiley()
    radius =100*(lfo(50,'sine')+1)
    num = int(20*lfo(50)+7)
    crazyWheel(cs,i,radius,num)
    
    #cs.place(i,i,i*10)
    #cs=crazySmiley()
    #cs.randomize(eyes=2,pupils=10,mouth=10)
    #cs.place(100-i,100-i,0,1+i*0.01)
    
    popMatrix()