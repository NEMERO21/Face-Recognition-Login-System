# Face-Recognition-Login-System
This is a face recognition login system implemented using Python programming language and various libraries such as OpenCV, face recognition, tkinter, and PIL. The system provides an option to register a new user and to login. The system captures the video feed from the instance when login was clicked and opens a new window which shows the captured picture, a text bar to enter the name of the person, an accept button to save the picture, and a try again button to go back to the first window. When Accept is clicked, the software returns to the first window and displays a message box saying User was successfully registered. When Login is clicked, it again captures the pic from the video feed and compares it from the database. If a match is found, a message box saying Welcome, [username] is displayed, otherwise, a message box saying User not found, Register user is shown.

Requirements
Python 3
OpenCV
face recognition
tkinter
PIL

Installation
1. Clone the repository using the following command:
   git clone https://github.com/NEMERO21/Face-Recognition-Login-System.git

2. Install the required libraries using the following command:
   pip install opencv-python face-recognition tkinter Pillow
   
   
Usage
1. Open a terminal and navigate to the project directory.

2. Run the following command to start the face recognition login system:
   python face_recognition_login_system.py
   
3. The system will open a window displaying the live video feed from the camera.

4. Click on the "Register new user" button to register a new user. The system will capture the video feed from the instance when login was clicked and opens a new window which shows the captured picture, a text bar to enter the name of the person, an accept button to save the picture, and a try again button to go back to the first window.

5. When Accept is clicked, the software returns to the first window and displays a message box saying User was successfully registered.

6. Click on the "Login" button to login. The system will again capture the pic from the video feed and compare it from the database. If a match is found, a message box saying Welcome, [username] is displayed, otherwise, a message box saying User not found, Register user is shown.
