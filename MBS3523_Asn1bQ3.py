import cv2
print(cv2.__version__)
capture = cv2.VideoCapture(0)
dx = 2
dy = 1
edge = 80
posx = 128
posy = 128
capture.set(3, 640)
capture.set(4, 480)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    success, img = capture.read()
    img = cv2.rectangle(img, (posx, posy), (posx+edge, posy+edge), (200, 16, 216), 2)
    cv2.putText(img, 'MBS3523 Assignment 1b - Q3     Name: ZHANG Jianru', (20, 50), font, 0.6, (255, 255, 0), 2)
    cv2.imshow('Frame', img)
    posx += dx
    posy += dy
    if posx+edge >= 640 or posx <= 0:
        dx = -dx
    if posy+edge >= 480 or posy <= 0:
        dy = -dy
    if cv2.waitKey(5) & 0xff == 27:
        break
capture.release()
cv2.destroyAllWindows()
