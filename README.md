# Gesture Controlled Virtual Camera

A real-time **gesture-controlled virtual camera system** built using **Python, OpenCV, MediaPipe, and OBS Virtual Camera**.

This project allows users to control **video on/off, zoom in–out, and background blur**
using **hand gestures**, without installing any plugin or extension inside
Zoom, Google Meet, or Microsoft Teams.

---

## 🎯 Project Objective

The objective of this project is to:
- Control webcam behavior using hand gestures
- Replace manual camera controls during meetings
- Work with any video conferencing app that supports webcams
- Demonstrate practical use of **computer vision and virtual devices**

---

## 🧠 How It Works

1. Webcam frames are captured using OpenCV  
2. MediaPipe detects hands and facial landmarks  
3. Gestures are interpreted using custom logic  
4. Frames are modified (zoom / blur / black screen)  
5. Modified frames are sent to **OBS Virtual Camera**  
6. Zoom / Meet / Teams uses OBS Virtual Camera as input  

---

## 🛠️ Tech Stack Used

| Technology | Purpose |
|----------|--------|
| Python | Core programming language |
| OpenCV | Video capture & image processing |
| MediaPipe | Hand & face detection |
| NumPy (1.23.5) | Numerical processing (ABI safe) |
| pyvirtualcam | Virtual camera frame output |
| OBS Virtual Camera | OS-level camera for meetings |

---

## 📁 Project Structure

zoom-gestures/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│ ├── handsutils.py
│ ├── fingerutils.py
│ ├── zoomutils.py
│ ├── faceutils.py
│ └── face_detection.py

---

## Gesture Controls

### 🎥 Video Control
| Gesture | Action |
|-------|--------|
| Closed fist ✊ | Video OFF (black screen) |
| Open hand ✋ | Video ON |

---

### 🔍 Zoom Control
| Gesture | Action |
|-------|--------|
| Thumb + Index pinch | Activate zoom |
| Fingers apart | Zoom IN |
| Fingers close | Zoom OUT |

---

### 🌫️ Background Blur
| Gesture | Action |
|-------|--------|
| Three fingers | Blur ON |
| Two fingers | Blur OFF |

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start OBS Virtual Camera
1. Open OBS Studio
2. Keep OBS running

### 4️⃣ Run the project
```bash
python main.py
```

## 🎥 Use in Zoom / Meet / Teams

In meeting app settings:
- Camera → OBS Virtual Camera
- No plugins or extensions required.

---

## ⚠️ Safe Runtime Logs

Logs like below are normal:
INFO: Created TensorFlow Lite XNNPACK delegate for CPU
WARNING: Feedback manager requires a model with a single signature inference

They do not indicate errors.

---

## 🚀 Future Improvements
- Adjustable gesture sensitivity
- Higher zoom levels
- Gesture overlay UI
- Executable build
- Configurable gesture mapping




