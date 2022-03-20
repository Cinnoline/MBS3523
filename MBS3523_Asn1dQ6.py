import cv2
print(cv2.__version__)

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
font = cv2.FONT_HERSHEY_SIMPLEX
EVT = 0
PNT1 = (0, 0)
PNT2 = (0, 0)


def draw_rectangle(event, x, y, flags, param):
    global EVT
    global PNT1, PNT2
    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x, y)
        EVT = event
    if event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x, y)
        EVT = event
    if event == cv2.EVENT_RBUTTONUP:
        EVT = event


cv2.namedWindow('MBS3523')
cv2.setMouseCallback('MBS3523', draw_rectangle)
while True:
    success, img = capture.read()
    cv2.putText(img, 'MBS3523 Assignment 1d - Q6     Name: ZHANG Jianru', (20, 50), font, 0.6, (255, 255, 0), 2)
    if EVT == 4:
        cv2.rectangle(img, PNT1, PNT2, (255, 0, 0), 2)
        roi = img[PNT1[1]:PNT2[1], PNT1[0]:PNT2[0]]
        cv2.imshow('ROI', roi)
    cv2.imshow('MBS3523', img)
    if EVT == 5:
        cv2.destroyWindow('ROI')
        EVT = 0
    if cv2.waitKey(5) & 0xff == 27:
        break
capture.release()
cv2.destroyAllWindows()
