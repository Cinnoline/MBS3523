import cv2
print(cv2.__version__)

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
font = cv2.FONT_HERSHEY_SIMPLEX


def nil(p):
    pass


cv2.namedWindow('MBS3523')
cv2.createTrackbar('H Pos', 'MBS3523', 320, 640, nil)
cv2.createTrackbar('V Pos', 'MBS3523', 240, 480, nil)
while True:
    x = cv2.getTrackbarPos('H Pos', 'MBS3523')
    y = cv2.getTrackbarPos('V Pos', 'MBS3523')
    success, img = capture.read()
    cv2.putText(img, 'MBS3523 Assignment 1d - Q5     Name: ZHANG Jianru', (20, 50), font, 0.6, (255, 255, 0), 2)
    img = cv2.line(img, (0, y), (640, y), (255, 0, 0), 2)
    img = cv2.line(img, (x, 0), (x, 480), (255, 0, 0), 2)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(5) & 0xff == 27:
        break
capture.release()
cv2.destroyAllWindows()
