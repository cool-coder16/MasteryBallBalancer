import cv2, os, sys
import numpy as np

DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "embeddings")
files = {}
for file in os.listdir(DIR_PATH):
    if file.endswith(".npy"): files[file[:-4]] = np.load(os.path.join(DIR_PATH, file))

RECOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_recognition_sface_2021dec.onnx")
recognizer = cv2.FaceRecognizerSF.create(RECOG_PATH, "")

DETECTOR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_detection_yunet_2026may.onnx")
detector = cv2.FaceDetectorYN.create(DETECTOR_PATH, "", (320, 320), 0.75, 0.3, 5000)

RECOG_THRESHOLD = 0.500

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("cap not opened")
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("no ret")
        continue
    
    clean = frame.copy()
    
    h, w = frame.shape[:2]
    detector.setInputSize((w, h))
    
    _, faces = detector.detect(frame)
    if faces is not None and len(faces) >= 1:
        for face in np.asarray(faces):
            aligned = recognizer.alignCrop(clean, face)
            
            feature = recognizer.feature(aligned)
            
            scores = {}
            for person in files.keys():
                scores[person] = []
                for f in files[person]:
                    score = recognizer.match(feature, f)
                    scores[person].append(score)
                
                scores[person] = sorted(scores[person], reverse=True)
                scores[person] = np.mean(scores[person][:5])
            
            best_name = max(scores, key=scores.get) # type: ignore
            best_score = scores[best_name]
            
            print(scores)
            
            if best_score >= RECOG_THRESHOLD:
                x, y, bw, bh = face[:4].astype(int)
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 3)
                cv2.putText(frame, f"{best_name} - {best_score:.4f}", (x, y - 5), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0))
            else:
                x, y, bw, bh = face[:4].astype(int)
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 0, 255), 3)
                cv2.putText(frame, "UNKNOWN", (x, y - 5), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255))
    
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()