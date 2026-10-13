import cv2, math, os
import numpy as np

name = "anaaya"

cap = cv2.VideoCapture(0)
if not cap.isOpened(): raise Exception('cap not opened')
window = cv2.namedWindow('Camera')
ret, frame = cap.read()
if not ret: raise Exception('no ret')
DETECTOR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_detection_yunet_2026may.onnx") 
RECOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_recognition_sface_2021dec.onnx") 
WRITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces", f"{name}") 
h, w = frame.shape[:2]
detector = cv2.FaceDetectorYN.create(DETECTOR_PATH, "", (w, h), 0.75, 0.3, 5000)
recognizer = cv2.FaceRecognizerSF.create(RECOG_PATH, "")

while True:
    ret, frame = cap.read()
    if not ret: continue
    clean = frame.copy()
    _, faces = detector.detect(frame)
    if faces is not None:
        for face in np.asarray(faces):
            x, y, bw, bh = face[:4].astype(int) 
            color = (0, 255, 0)
            cv2.rectangle(frame, (x, y), (x + bw, y + bh), color, 3)
            
            score = face[14] 
            cv2.putText(frame, f"{score:.2f}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color)
            
            r = max(2, int(bw * 0.03))
            lex, ley = face[4:6].astype(int) 
            cv2.circle(frame, (lex, ley), r, color)
            
            rex, rey = face[6:8].astype(int) 
            cv2.circle(frame, (rex, rey), r, color)
            
            nx, ny = face[8:10].astype(int) 
            nr = max(4, int(bw * 0.06))
            cv2.circle(frame, (nx, ny), nr, color)
            
            mlx, mly, mrx, mry = face[10:14].astype(int) 
            cv2.line(frame, (mlx, mly), (mrx, mry), color, 3)
    
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key == 113: break
    elif key == 32: 
        n = 1
        while os.path.exists(os.path.join(WRITE_PATH, f"{n:03d}.png")): 
            n += 1
        path = os.path.join(WRITE_PATH, f"{n:03d}.png") 
        cv2.imwrite(path, clean)
        print('Saved to', path)

cap.release()
cv2.destroyAllWindows()