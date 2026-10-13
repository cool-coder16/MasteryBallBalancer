import cv2, math
import numpy as np
from datetime import datetime

def get_color(event, x, y, flags, param):
    global hsv, ret_color
    if event == cv2.EVENT_LBUTTONDOWN:
        ret_color = hsv[y, x] 
        print(ret_color)

def change_error(val):
    global errors
    errors = (val, val, val)

cap = cv2.VideoCapture(0)
if not cap.isOpened(): raise Exception('cap not opened')
ret_color = np.array([60, 138, 26])
window = cv2.namedWindow("Camera")
errors = (65, 65, 65)
cv2.setMouseCallback("Camera", get_color)
error_tb = cv2.createTrackbar("error", "Camera", errors[0], 255, change_error)
display = None
while True:    
    ret, frame = cap.read()
    if not ret: continue
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = frame.copy()
    inrange = hsv.copy()
    blurred = cv2.medianBlur(hsv, 9)
    display = inrange.copy()
    if ret_color is not None:
        low = ret_color - np.array(errors)
        high = ret_color + np.array(errors)
        inrange = cv2.inRange(blurred, low, high)
        
        inrange = cv2.morphologyEx(inrange, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
        inrange = cv2.morphologyEx(inrange, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11)))
        
        bgr = cv2.cvtColor(inrange, cv2.COLOR_GRAY2BGR)
        display = hsv.copy()
        contours, hierarchy = cv2.findContours(inrange, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        if not contours: continue
        
        contours = sorted(contours, key=lambda c: cv2.contourArea(c), reverse=True)
        c = contours[0]
        moment = cv2.moments(c)
        
        center = (moment['m10'] / moment['m00'], moment['m01'] / moment['m00'])
        center = (int(center[0]), int(center[1]))
        
        cv2.drawContours(display, contours, 0, (0, 0, 255), thickness=10, lineType=cv2.LINE_8)
        cv2.drawMarker(display, center, (0, 0, 255), cv2.MARKER_CROSS, 20, 4, cv2.LINE_4)
        window_center = (frame.shape[1] // 2, frame.shape[0] // 2)
        cv2.line(display, center, window_center, (255, 0, 0), 5)
        cv2.drawMarker(display, window_center, (0, 255, 0), cv2.MARKER_STAR, 20, 4, cv2.LINE_4)
        error = math.dist(center, window_center)
        
    cv2.imshow("Camera", display)
    
    
    
    key = cv2.waitKey(1)
    if key != -1:
        if key == 27:
            ret_color = None
        elif key == 32:
            cv2.imwrite(f"/Users/vivaan/Desktop/Mastery Project/openCV/Ball Tracker/images/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png", display)
            print("saved to", f"/Users/vivaan/Desktop/Mastery Project/openCV/Ball Tracker/images/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png")
        else: break

cap.release()
cv2.destroyAllWindows()