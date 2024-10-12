import pgzrun

#screen and title
WIDTH = 600
HEIGHT = 600
TITLE = "Bouncy ball"
#gravity
GRAVITY = 500

class  Circle():
    def __init__(self,x,y,radius,colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.vx = 10
        self.vy = 0   
        
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.colour)
        
    
    

#object            
circle1 = Circle(200,300,50,"Green")

#functions
def draw():
    screen.clear()
    circle1.draw()
def update(dt):
    circle1.x = circle1.x + circle1.vx * dt
    uy = circle1.vy 
    circle1.vy += GRAVITY * dt
    circle1.y += (uy + circle1.vy) * 0.5 * dt



    

pgzrun.go()

    

        



