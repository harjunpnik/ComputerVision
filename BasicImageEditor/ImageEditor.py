import numpy as np
import cv2 as cv 

drawing = False # true if mouse is pressed
mode = 'r' # starts with 'r' for drawing rectangles, to change mode press 'l' or 'r' for line or rectangle
ix,iy = -1,-1

# mouse callback function
def draw_with_mouse(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            # Create temporary image copy and draw the line on the temporary image
            temp = previousImg.copy()
            if mode == 'r':
                cv.rectangle(temp,(ix,iy),(x,y),(0,255,0),2)                
            elif mode == 'l':
                cv.line(temp,(ix,iy),(x,y),(0,0,255),2)
            # Show temporary image
            cv.imshow('Image Editor',temp)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == 'r':
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        elif mode == 'l':
            cv.line(img,(ix,iy),(x,y),(0,0,255),2)

# Load in image and start mousecallback
img = cv.imread('man.jpg')
cv.namedWindow('Image Editor')
cv.setMouseCallback('Image Editor', draw_with_mouse)

# Loop until q is pressed
while(1):

    # if not drawing show current image
    if not drawing:
        previousImg = img.copy() # create snapshot for temporary image in draw_with_mouse
        cv.imshow('Image Editor',img)
    
    k = cv.waitKey(1) & 0xFF

    # keybinds for tools
    if k == ord('l'):
        mode = 'l' # Change mode
    elif k == ord('r'):
        mode = 'r' # Change mode
    elif k == ord('s'):
        cv.imwrite('man.jpg',img)
        print("Image saved!")
    elif k == ord('q'):
        break

cv.destroyAllWindows()