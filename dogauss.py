import cv2
import numpy as np

def DoG():
    #fn = raw_input("Enter image file name and path: ")
    #fn_no_ext = fn.split('.')[0]
    #outputFile = fn_no_ext+'DoG.jpg'
    #read the input file
    img = cv2.imread('jcBig3b.jpg')

    #run a 5x5 gaussian blur then a 3x3 gaussian blr
    blur9 = cv2.GaussianBlur(img,(9,9),0)
    blur7 = cv2.GaussianBlur(img,(7,7),0)

    #write the results of the previous step to new files
    cv2.imwrite('jc9x9.jpg', blur7)
    cv2.imwrite('jc7x7.jpg', blur9)

    DoGim = blur9 - blur7
    gray = cv2.cvtColor(DoGim, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayJCDoG.jpg', gray)
    
DoG()