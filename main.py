import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

#creating class for the buttons

class Button:
    def __init__(self,pos,width,height,Value):
        self.pos = pos
        self.width = width
        self.height = height
        self.Value = Value

    def draw(self,img):
         cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(225, 225, 225),cv.FILLED)
         cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50, 50, 50),3)
         cv.putText(img,self.Value,(self.pos[0]+20,self.pos[1]+70),cv.FONT_HERSHEY_SIMPLEX,2,(50,50,50),3)
    
    def checkClick(self,x,y):
        if (self.pos[0]<x<self.pos[0]+self.width) and self.pos[1]<y<self.pos[1]+self.height :
                     cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(225, 225, 225),cv.FILLED)
                     cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(50, 50, 50),3)
                     cv.putText(img,self.Value,(self.pos[0]+20,self.pos[1]+70),cv.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)

                     return True
        else: False

         



#Webcam 
cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


#creating button
# Creating button with list 
# button values

buttonValues = [['7','8','9','+'],
          ['4','5','6','-'],
          ['1','2','3','*'],
          ['.','0','/','=']]

buttonList = []
for x in range(4):
    for y in range(4):
     xpos = x*100 + 800
     ypos = y*100+150
     buttonList.append(Button((xpos,ypos),100,100,buttonValues[y][x]))

print(buttonList)
# variable
delayCounter = 0
myEquation = ''

Detector = HandDetector(detectionCon=0.8,maxHands=1)
# Loop
while True:
    success,img = cap.read()
    img = cv.flip(img,1)

    #Detection of hand
    hands, img = Detector.findHands(img,flipType = False)

    # for the screen 
    cv.rectangle(img,(800,70),(800+400,70+100),(225, 225, 225),cv.FILLED)
    cv.rectangle(img,(800,70),(800+400,70+100),(50, 50, 50),3)
    


    for button in buttonList:
        button.draw(img)

    #Check for hand
   
    if hands:
        lmList = hands[0]['lmList']
        tip1 =  lmList[8][:2]
        tip2 = lmList[12][:2]
        length, _, img = Detector.findDistance(tip1,tip2,img)
        x,y = tip1

        if length<40:
             for i,  button in enumerate(buttonList):
                  if button.checkClick(x,y) and delayCounter == 0:
                       myValue = buttonValues[int(i%4)][int(i/4)]
                       if myValue == "=":
                            myEquation = str(eval(myEquation))
                       else:
                           myEquation += myValue
                       delayCounter = 1
                                            

                       

 

    # avoiing duplicates
    if delayCounter !=0:
         delayCounter +=1
         if delayCounter > 20:
              delayCounter = 0


    #display the Equation
    cv.putText(img,myEquation,(810,130),cv.FONT_HERSHEY_SIMPLEX,2,(50,50,50),3)



    #Display image
    cv.imshow("image",img)
    key = cv.waitKey(1)

    if key == ord('c'):
         myEquation = ''

    if key == ord('q'):
         cv.destroyAllWindows()
         break



