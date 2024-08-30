Hand Calculator with Virtual Buttons

This project implements a virtual calculator using hand detection and OpenCV libraries. It allows users to perform basic arithmetic operations by interacting with virtual buttons displayed on the screen.

Features:

Intuitive Interface: Provides a user-friendly grid of virtual buttons for numbers, operators, and an equal sign.
Accurate Hand Tracking: Utilizes OpenCV's HandTrackingModule to reliably detect hand movements and fingertip positions.
Smooth Interaction: Enables seamless button interaction by registering fingertip clicks within button areas.
Real-time Equation Display: Shows the current equation being built on the screen, providing visual feedback.
Dynamic Calculation: Evaluates the equation in real-time using Python's eval function upon pressing the equal sign.
Clear Functionality: Allows users to clear the current equation conveniently with the "c" key.
Exit Option: Provides a simple exit mechanism by pressing the "q" key.
Requirements:

Python 3.x
OpenCV (pip install opencv-python)
cvzone (pip install cvzone)
Instructions:

Installation: Install the necessary libraries using pip:

Bash
pip install opencv-python cvzone
Use code with caution.

Run the Script: Execute the Python script:

Bash
python hand_calculator.py  # Replace with your actual filename
Use code with caution.

Webcam Access: The script will access your webcam. Follow the on-screen instructions.

Interaction: Use your fingertip to click on virtual buttons to build your equation.

Clear/Exit: Press "c" to clear the equation or "q" to exit the program.

Code Breakdown:

1. Imports:

cv2 as cv: Imports OpenCV for image processing and video capture.
from cvzone.HandTrackingModule import HandDetector: Imports the hand detection module.
2. Button Class:

Defines a Button class to represent individual buttons:
__init__: Initializes the button with its position (x, y), width, height, and value.
draw: Draws the button rectangle and its value on the image.
checkClick: Checks if the provided coordinates (x, y) fall within the button area. If so, updates the button's color and returns True for visual feedback.
3. Webcam Setup:

cap = cv.VideoCapture(0): Creates a video capture object for the webcam.
cap.set(3, 1280) and cap.set(4, 720): Set the desired frame width (1280) and height (720) for the webcam video (optional, adjust as needed).
4. Button Creation:

buttonValues: A list of lists representing the button layout (numbers, operators, equal sign).
buttonList: Stores Button objects, creating a grid of buttons from buttonValues.
5. Variables:

delayCounter: Prevents repeated button presses due to lingering fingertip contact (initialized to 0).
myEquation: Stores the current equation being built (initialized as an empty string).
6. Hand Detection:

Detector = HandDetector(detectionCon=0.8, maxHands=1): Creates a hand detector object with a confidence threshold of 0.8 (80%) and limits detection to one hand.
7. Main Loop:

Captures a frame from the webcam and flips it horizontally for natural view (success, img = cap.read(), img = cv.flip(img, 1)).
Attempts to detect hands in the frame (hands, img = Detector.findHands(img, flipType=False)) and handles potential detection errors.
Draws a rectangle on the screen to display the equation (cv.rectangle(...)).
Iterates through buttonList to draw each button using the draw method.
If hands are detected:
Extracts the tip positions of the index and middle finger (lmList = hands[0]['lmList'], tip1 = lmList[8][:2], tip2 = lmList[12][:2]).
Calculates the distance between the fingertips (length, _, img = Detector.findDistance(tip1, tip2, img)) for potential button interaction.
Processes fingertip clicks:
Iterates through buttonList to check if a click falls within a button's area using button.checkClick(x, y).
If a button is clicked and delayCounter is 0 (to prevent repeated clicks due to lingering fingertip contact):
Extracts the button's value (myValue = buttonValues[int(i%4)][int(i/4)]).
If the value is "=", evaluates the equation using myEquation = str(eval(myEquation)).
Otherwise, appends the value to the myEquation string.
Sets delayCounter to 1 to temporarily disable button clicks.
8. Delay Counter:

Increments delayCounter in each loop iteration.
If delayCounter exceeds 20, resets it to 0 to allow for new button clicks.
9. Equation Display:

Displays the current myEquation on the screen using cv.putText(...).
10. Exit:

Checks for the "q" key press to exit the loop and close the windows.
