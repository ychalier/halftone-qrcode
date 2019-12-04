import qrcode
import cv2 as cv
import numpy as np

qrWitdh = 37
#Quantity of white blocks in a box
"""patterns = 
        [
            #0block
            [   
                [
                    [0,0,0],
                    [0,0,0],
                    [0,0,0]
                ]
            ],
            #1block
            [
                [
                    [1,0,0],
                    [0,0,0],
                    [0,0,0]
                ],
                [
                    [0,1,0],
                    [0,0,0],
                    [0,0,0]
                ],
                [
                    [0,0,1],
                    [0,0,0],
                    [0,0,0]
                ],
                [
                    [0,0,0],
                    [1,0,0],
                    [0,0,0]
                ],
                [
                    [0,0,0],
                    [0,0,1],
                    [0,0,0]
                ],
                [
                    [0,0,0],
                    [0,0,0],
                    [1,0,0]
                ],
                [
                    [0,0,0],
                    [0,0,0],
                    [0,1,0]
                ],
                [
                    [0,0,0],
                    [0,0,0],
                    [0,0,1]
                ]
            ],
            #2blocks
            [
                [
                    [0,0,0],
                    [1,1,1],
                    [0,0,0]
                ],
                [
                    [0,1,0],
                    [0,1,0],
                    [0,1,0]
                ],
                [
                    [0,0,1],
                    [0,1,0],
                    [1,0,0]
                ],
                [
                    [1,0,0],
                    [0,1,0],
                    [0,0,1]
                ],
                [
                    [1,0,0],
                    [0,1,0],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [0,1,0],
                    [0,0,1]
                ],
                [
                    [1,0,1],
                    [0,1,0],
                    [0,0,0]
                ],
                [
                    [0,0,0],
                    [0,1,0],
                    [1,0,1]
                ]
            ],
            #3blocks
            [
                [
                    [0,0,0],
                    [1,1,1],
                    [0,1,0]
                ],
                [
                    [0,0,0],
                    [1,1,1],
                    [1,0,0]
                ],
                [
                    [0,0,0],
                    [1,1,1],
                    [0,0,1]
                ],
                [
                    [0,1,1],
                    [0,1,0],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [0,1,1],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [0,1,0],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [0,1,0],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [1,1,0],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [0,1,0],
                    [1,1,0]
                ],
                [
                    [1,0,1],
                    [0,1,0],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [1,1,0],
                    [1,0,0]
                ],
                [
                    [0,1,1],
                    [0,1,0],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [0,1,0],
                    [1,0,1]
                ],
                [
                    [0,0,1],
                    [0,1,0],
                    [1,1,0]
                ],
                [
                    [0,0,1],
                    [0,1,1],
                    [1,0,0]
                ]
            ],
            #4blocks
            [
                [
                    [1,0,1],
                    [0,0,0],
                    [1,0,1]
                ],
                [
                    [1,0,0],
                    [0,0,1],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [0,0,0],
                    [0,1,1]
                ],
                [
                    [1,0,0],
                    [0,0,1],
                    [0,1,1]
                ],
                [
                    [0,0,1],
                    [1,0,0],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [0,0,0],
                    [1,1,0]
                ],
                [
                    [0,0,1],
                    [1,0,0],
                    [1,1,0]
                ],
                [
                    [0,1,1],
                    [0,0,0],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [0,0,1],
                    [1,0,0]
                ],
                [
                    [0,1,1],
                    [0,0,1],
                    [1,0,0]
                ],
                [
                    [0,1,0],
                    [1,0,0],
                    [1,0,1]
                ],
                [
                    [0,1,1],
                    [1,0,0],
                    [0,0,1]
                ],
                [
                    [1,1,0],
                    [1,0,0],
                    [0,0,1]
                ],
                [
                    [0,1,0],
                    [1,0,1],
                    [0,1,0]
                ],
                [
                    [1,0,0],
                    [1,0,1],
                    [0,1,0]
                ],
                [
                    [0,0,1],
                    [1,0,1],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [1,0,1],
                    [1,0,0]
                ],
                [
                    [0,1,0],
                    [1,0,1],
                    [0,0,1]
                ],
                [
                    [0,1,0],
                    [0,0,1],
                    [1,1,0]
                ],
                [
                    [1,1,0],
                    [0,0,1],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [1,0,0],
                    [0,1,1]
                ],
                [
                    [0,1,1],
                    [1,0,0],
                    [0,1,0]
                ],
                [
                    [1,1,1],
                    [0,0,0],
                    [0,1,0]
                ],
                [
                    [0,1,0],
                    [0,0,0],
                    [1,1,1]
                ],
                [
                    [1,0,0],
                    [1,0,1],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [1,0,1],
                    [0,0,1]
                ],
                [
                    [1,1,0],
                    [0,0,0],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [0,0,1],
                    [0,0,1]
                ],
                [
                    [1,1,0],
                    [0,0,1],
                    [0,1,0]
                ],
                [
                    [0,0,1],
                    [1,0,1],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [0,0,1],
                    [1,1,0]
                ]
            ],
            #5block
            [
                [
                    [1,1,1],
                    [0,0,0],
                    [1,0,1]
                ],
                [
                    [1,1,1],
                    [0,0,0],
                    [0,1,1]
                ],
                [
                    [1,1,1],
                    [0,0,0],
                    [1,1,0]
                ],
                [
                    [1,0,0],
                    [1,0,1],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [1,0,0],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [1,0,1],
                    [1,0,0]
                ],
                [
                    [0,0,1],
                    [1,0,1],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [0,0,1],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [1,0,1],
                    [0,0,1]
                ],
                [
                    [0,1,0],
                    [1,0,1],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [0,0,1],
                    [0,1,1]
                ],
                [
                    [1,0,0],
                    [1,0,1],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [1,0,1],
                    [0,1,0]
                ],
                [
                    [1,1,0],
                    [1,0,1],
                    [0,0,1]
                ],
                [
                    [1,1,0],
                    [1,0,0],
                    [0,1,1]
                ]
            ],
            #6block
            [
                [
                    [1,1,1],
                    [0,0,0],
                    [1,1,1]
                ],
                [
                    [1,0,1],
                    [1,0,1],
                    [1,0,1]
                ],
                [
                    [1,1,0],
                    [1,0,1],
                    [0,1,1]
                ],
                [
                    [0,1,1],
                    [1,0,1],
                    [1,1,0]
                ],
                [
                    [0,1,1],
                    [1,0,1],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [1,0,1],
                    [1,1,0]
                ],
                [
                    [0,1,0],
                    [1,0,1],
                    [1,1,1]
                ],
                [
                    [1,1,1],
                    [1,0,1],
                    [0,1,0]
                ]
            ],
            #7block
            [
                [
                    [1,1,1],
                    [1,0,0],
                    [1,1,1]
                ],
                [
                    [1,1,1],
                    [0,0,1],
                    [1,1,1]
                ],
                ,
                [
                    [1,1,1],
                    [1,0,1],
                    [1,0,1]
                ],
                [
                    [1,0,1],
                    [1,0,1],
                    [1,1,1]
                ],
                [
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]
                ],
                [
                    [1,1,0],
                    [1,0,1],
                    [1,1,1]
                ],
                [
                    [0,1,1],
                    [1,0,1],
                    [1,1,1]
                ],
                [
                    [1,1,1],
                    [1,0,1],
                    [1,1,0]
                ]
            ],
            #8 white blocks
            [
                [
                    [1,1,1],
                    [1,0,1],
                    [1,1,1]
                ]
            ]
            
        ]
"""
from patterns import *
    
def makeQrcode(link, border = False):#concluida
    if border:
        qr = qrcode.QRCode(
            version = 5,
            error_correction = qrcode.constants.ERROR_CORRECT_M,
            box_size = 3,
            border = 4
        )
    else:
        qr = qrcode.QRCode(
        version = 5,
        error_correction = qrcode.constants.ERROR_CORRECT_M,
        box_size = 3
        ,
        border = 0
    )
    qr.add_data(link)
    qr.make(fit= True)
    return qr.make_image(fill_color="black", back_color="white")
    
def bestScore( x, y, tone=8):
    
    if x==0:
        x=1
    if y==0:
        y=1
    global rawQrCode
    global halftone
    lowestDiff = 255*9
    lowestIndex = 0
    difference = 0
    # print x,y,  (rawQrCode[ x][ y][0])//255,'old tone' ,tone
    #tone -= (rawQrCode[ x][ y][0])//255
    print 'newtone: ',tone
    for i in range( len( patterns[ tone])):
        difference += abs( patterns[ tone][ i][ 0][ 0]* 255- halftone[x-1][y-1])
        difference += abs( patterns[ tone][ i][ 0][ 1]* 255- halftone[x-1][y])
        difference += abs( patterns[ tone][ i][ 0][ 2]* 255- halftone[x-1][y+1])
        difference += abs( patterns[ tone][ i][ 1][ 0]* 255- halftone[x-1][y-1])
        difference += abs( patterns[ tone][ i][ 1][ 2]* 255- halftone[x-1][y+1])
        difference += abs( patterns[ tone][ i][ 2][ 0]* 255- halftone[x-1][y-1])
        difference += abs( patterns[ tone][ i][ 2][ 1]* 255- halftone[x-1][y])
        difference += abs( patterns[ tone][ i][ 2][ 2]* 255- halftone[x-1][y+1])
        # print "iteracao nro: ",i, "tom: ", tone, "x , y", x,y       
        if difference <= lowestDiff:
            lowestDiff = difference
            lowestIndex = i
        # print 'lowest', lowestIndex, 'diff', difference, 'lowDiff', lowestDiff   
        difference=0
    return lowestIndex

#CREATES QRCODE WITHOU BORDER, FOR EASIER MANIPULATIONS
rawQrCode = makeQrcode('http://www.ufrgs.br/ufrgs/inicial', border= False)
rawQrCode.save('rawQrBorderless.png')
rawQrCode= cv.imread('rawQrBorderless.png')


resizedQr = cv.resize( cv.imread('rawQrBorderless.png'), (3*qrWitdh, 3*qrWitdh))
img= cv.imread('jc2.png')
img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#CREATES 2 VERSIONS OF TERGET IMAGE, ONDE WITH THE RESOLUTUION OF DE QR E OTHER WITH 3 TIMES THAT
imgSmall= cv.resize( img,( qrWitdh, qrWitdh))
imgBig= cv.resize( img,( qrWitdh*3, qrWitdh*3))
cv.imwrite('jcBig.jpg',imgBig)

#concatena para 8 tons
for x in range( len( imgBig[0])):
    for y in range( len(imgBig)):
        imgBig[x][y]= -( -imgBig[x][y]// 32)*32-1
cv.imwrite('jcBig3b.jpg',imgBig)
cv.imwrite('jcSmall.jpg',imgSmall)

# var = makeQrcode('biribiri',border=True)
# var.save('teste salvamento.png')
# var= cv.imread('teste salvamento.png')

#CREATES HALFTONE FROM TARGET IMAGE
halftone = imgBig
for x in range( len( imgSmall)):
    i=x+1
    for y in range( len( imgSmall[0])):
        j=y+1
        tone= int(imgSmall[x][y] // 25.5844)
        print tone, y,rawQrCode[ (i*3-2)][ (j*3-2)][ 0]
        #print patternType, halftone[ (i*3-2)-1][ (j*3-2)-1]
        centerNode =( rawQrCode[ (i*3-2)][ (j*3-2)][ 0])/255
        halftone[ (i*3-2)][ (j*3-2)]= rawQrCode[ (i*3-2)][ (j*3-2)][ 0]
        
        if tone == 9 and centerNode == 0:
            tone = 8
        elif centerNode != 0 and tone != 0:
            tone = tone -1
        elif tone == 0:
            tone = 0

        patternType= bestScore((i*3-2), (j*3-2), tone)    #ESCOLHE O PADRAO COM MELHOR DIFERENCA
        print 'pattType:' ,patternType, 'tone', tone, 'center',centerNode
        halftone[ (i*3-2)-1][ (j*3-2)-1]= patterns[ tone][ patternType][ 0][ 0]* 255
        halftone[ (i*3-2)-1][ (j*3-2)]  = patterns[ tone][ patternType][ 0][ 1]* 255
        halftone[ (i*3-2)-1][ (j*3-2)+1]= patterns[ tone][ patternType][ 0][ 2]* 255
        halftone[ (i*3-2)][ (j*3-2)-1]  = patterns[ tone][ patternType][ 1][ 0]* 255
        halftone[ (i*3-2)][ (j*3-2)+1]  = patterns[ tone][ patternType][ 1][ 2]* 255
        halftone[ (i*3-2)+1][ (j*3-2)-1]= patterns[ tone][ patternType][ 2][ 0]* 255
        halftone[ (i*3-2)+1][ (j*3-2)]  = patterns[ tone][ patternType][ 2][ 1]* 255
        halftone[ (i*3-2)+1][ (j*3-2)+1]= patterns[ tone][ patternType][ 2][ 2]* 255

#Apply Mask
mask = cv.imread('mask.png')
for x in range( len( halftone)):
    for y in range( len( halftone[0])):
        if mask[ x][ y][ 0] == 255:
            halftone[ x][ y]= rawQrCode[ x][ y][ 0]

#create the QRcode with border
finalQrCodeBordered = cv.copyMakeBorder(
                 halftone, 
                 12, 
                 12, 
                 12, 
                 12, 
                 cv.BORDER_CONSTANT, 
                 value=255
              )

cv.imwrite('halftoned.png',finalQrCodeBordered)


