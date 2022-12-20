import cv2 as cv
cam_port = 0
cam = cv.VideoCapture(cam_port)
result, image = cam.read()
if result:
    cv.imshow("Spyware", image)
    cv.imwrite("The-Bad-Guys//Oh-spy.png", image)