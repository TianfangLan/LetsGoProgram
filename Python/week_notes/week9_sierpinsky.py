from graphics import *
import time
# you need to download graphics.py and place it in the same folder as this code

def mid_point(p1, p2):
    '''(list, list) -> list
    returns the mid ppoint of two given points.
    '''
    p = []
    p.append((p1[0] + p2[0])/2)
    p.append((p1[1] + p2[1])/2)
    return p

def draw_sierpinski(order, p1, p2, p3, win):
    '''(Sierpinski_GUI, int, list, list, list)
    Draw a Sierpinski triangle with verticies p1, p2, p3)
    '''
    # base case: when we get to order of 1, we draw the triangle
    if order == 1:
        
        # create the line between two given point
        line = Line(Point(p1[0], p1[1]), Point(p2[0], p2[1])) 
        line.setWidth(2)
        
        # draw on the canvas
        line.draw(win)    

        line = Line(Point(p1[0], p1[1]), Point(p3[0], p3[1])) 
        line.draw(win)    

        line = Line(Point(p2[0], p2[1]), Point(p3[0], p3[1])) 
        line.draw(win)            
       
        # Add a delay to see how it draws
        time.sleep(0.01)
    else:
        # find the mid point between each two points
        m12 = mid_point(p1, p2)
        m23 = mid_point(p2, p3)
        m13 = mid_point(p3, p1)
        # Recursively draw the three triangles
        draw_sierpinski(order - 1, p1, m12, m13, win)
        draw_sierpinski(order - 1, m12, p2, m23, win)
        draw_sierpinski(order - 1, m13, m23, p3, win)

   
if (__name__ == "__main__"):
    
        # create a canvas to draw by providing the title and dimensions
        win = GraphWin('SierpinskyTree', 500, 500) 
        # x-coordinate for p1 = 250,  y-coordinate for p1 = 50
        p1 = [250, 50]
        p2 = [20,450]
        p3 = [480, 450]
        draw_sierpinski(5, p1, p2, p3, win)
        message = Text(Point(win.getWidth()/2, 20), 'Click anywhere inside the window to quit.')
        message.draw(win)
        win.getMouse()
        win.close()
        
