from drawingpanel import *
import time
def main():
    p = DrawingPanel(900, 500, background="light gray")
    ball = p.canvas.create_oval(430,10,470,50)
    xspeed = 2
    yspeed = 2
    while True:
        p.canvas.move(ball, xspeed, yspeed)
        pos = p.canvas.coords(ball)
        if pos[2] >=900 or pos[0] <0:
            xspeed = -xspeed
        if pos[3]>=500 or pos[1]<=0:
            yspeed=-yspeed
        p.update()
        time.sleep(0.01)
main()
    
