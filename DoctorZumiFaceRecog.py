import cv2
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'XXX.XXX.XX.XX'  # ADD HOST IP
s.bind((host, 5560))
s.listen(5)

# Start capturing video
vid_cam = cv2.VideoCapture(0)
vid_cam2 = cv2.VideoCapture(1)
# Detect object in video stream using Haarcascade Frontal Face
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

dividingFactor = 2
var = None
count = 0

print("Server has loaded; you are now able to join")
# Start looping
while True:
    # socket starts now
    clientsocket, address = s.accept()
    # print(f"Connection from {address} has been established.")
    _, image_frame = vid_cam.read()
    _, image_frame2 = vid_cam2.read()

    height, width, layers = image_frame.shape
    height2, width2, layers2 = image_frame2.shape

    # comment this line if you want the fullsize window
    image_frame = cv2.resize(image_frame, (int(width / dividingFactor), int(height / dividingFactor)))
    image_frame2 = cv2.resize(image_frame2, (int(width2 / dividingFactor), int(height2 / dividingFactor)))

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image_frame2, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 6, 0)
    eyes = eye_detector.detectMultiScale(gray, 1.3, 0, 1)

    faces2 = face_detector.detectMultiScale(gray2, 1.3, 15, 0)
    eyes2 = eye_detector.detectMultiScale(gray2, 1.3, 1, 1)
    # now our endpoint knows about the OTHER endpoint.

    if faces2 != ():
        var = "Not wearing"
    elif faces2 == () and eyes2 != ():
        var = "Wearing"
    else:
        var = "bleh"

    if var:
        if var is "Wearing":
            # FULL_MESSAGE ↓↓↓↓↓
            clientsocket.send(bytes("Wearing", "utf-8"))
            time.sleep(10)
        elif var is "Not wearing":
            # FULL_MESSAGE ↓↓↓↓↓
            clientsocket.send(bytes("Not wearing", "utf-8"))
            time.sleep(25)
        else:
            clientsocket.send(bytes("bleh", "utf-8"))

