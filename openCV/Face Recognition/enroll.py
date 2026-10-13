import cv2, os, sys
import numpy as np

name = "anaaya"

RECOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_recognition_sface_2021dec.onnx")
recognizer = cv2.FaceRecognizerSF.create(RECOG_PATH, "")

DETECTOR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models", "face_detection_yunet_2026may.onnx")
detector = cv2.FaceDetectorYN.create(DETECTOR_PATH, "", (320, 320), 0.75, 0.3, 5000)


DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "faces", name)
if not os.path.isdir(DIR_PATH):
    print(f"No folder for {name}")
    sys.exit()
dir_files = sorted([file for file in os.listdir(DIR_PATH) if file.lower().endswith(".png")])

if not dir_files: 
    print(f"no photos for {name}")
    sys.exit()

features = []
for file in dir_files:
    path = os.path.join(DIR_PATH, file)
    
    frame = cv2.imread(path)
    if frame is None:
        print(f"No frame for {file}")
        continue
    
    h, w = frame.shape[:2]
    detector.setInputSize((w, h))
    
    _, faces = detector.detect(frame)
    if faces is None or len(faces) != 1:
        print(f"Invalid faces for {file}")
        continue
    
    aligned = recognizer.alignCrop(frame, faces[0])
    
    feature = recognizer.feature(aligned)
    
    features.append(feature)

if not features:
    print("No features")
    sys.exit()
    
array = np.vstack(features)
EMBEDDING_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "embeddings")
os.makedirs(EMBEDDING_PATH, exist_ok=True)
np.save(os.path.join(EMBEDDING_PATH, name), array)
print(f"saved {len(features)} - skipped {len(dir_files) - len(features)}")

array = np.load(os.path.join(EMBEDDING_PATH, f"{name}.npy"))
matches = []
for i in range(len(array) - 1):
    for j in range(i+1, len(array)):
        matches.append(recognizer.match(array[i:i+1], array[j:j+1], cv2.FaceRecognizerSF_FR_COSINE))
    
print(min(matches), sum(matches) / len(matches), max(matches))