# 🎥 Face Detection using OpenCV

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Status](https://img.shields.io/badge/Status-Working-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A **real-time face detection system** built using **OpenCV and Haar Cascade Classifier**.  
The program captures frames from the webcam and detects faces in real time by drawing bounding boxes around them.

This project demonstrates **classical computer vision techniques** before deep learning-based detectors.

---

# 📊 Project Overview

| Feature | Description |
|------|-------------|
| 📷 Webcam Capture | Captures frames from the default webcam |
| 🧠 Face Detection | Uses Haar Cascade classifier |
| 🟦 Bounding Boxes | Draws rectangles around detected faces |
| 🟢 Detection Status | Displays if a face is detected |
| ⚡ Real-Time Processing | Runs continuously on video frames |

---

# 🧠 Detection Pipeline


Webcam
↓
Capture Frame
↓
Convert to Grayscale
↓
Haar Cascade Detection
↓
Draw Bounding Boxes
↓
Display Frame
↓
Repeat


---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Face_Detection.git
cd Face_Detection

pip install opencv-python

python face_detection.py

haarcascade_frontalface_default.xml

⚙️ Detection Parameters
Parameter	Purpose
scaleFactor	Image scaling between scans
minNeighbors	Controls false positives
minSize	Minimum detectable face size

Example:

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5,
    minSize=(30,30)
)
📷 Example Output

When a face is detected:

Face Detected

A bounding box appears around the face in the webcam window.

🚀 Future Improvements

Possible improvements:

Face recognition

Emotion detection

Mask detection

Replace Haar Cascade with deep learning detectors

Use YOLO / MTCNN / RetinaFace

📚 Learning Outcomes

This project helps understand:

Computer vision basics

Image preprocessing

Real-time video processing

Classical object detection

OpenCV fundamentals
