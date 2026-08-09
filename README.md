# ⚔️ Rock-Paper-Scissors Detection (YOLOv8 + Gradio)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-black?logo=yolo)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange?logo=gradio)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-purple?logo=opencv)

An intelligent Computer Vision application that detects **Rock-Paper-Scissors** hand gestures in real-time and automatically determines the winner.

---

## ⚡ Key Features
* 🎯 **Accurate Gesture Detection:** Real-time recognition of `Rock`, `Paper`, and `Scissors` gestures.
* 🏆 **Automated Game Engine:** Spatial tracking (Left vs. Right player) with instant winner calculation.
* ⚡ **Resource Efficient:** Optimized webcam snapshot mode to keep CPU usage low and prevent overheating.

---

## 📊 Model Evaluation & Performance

The YOLOv8 model was validated on **604 images** containing **418 instances**, demonstrating high precision across all gesture classes:

| Class | Precision | Recall | mAP@50 | mAP@50-95 |
| :--- | :---: | :---: | :---: | :---: |
| **Overall (All)** | **97.2%** | **94.3%** | **96.0%** | **76.3%** |
| 📄 **Paper** | 97.6% | 93.8% | 94.6% | 76.0% |
| 🪨 **Rock** | 96.1% | 94.7% | 96.0% | 74.0% |
| ✂️ **Scissors** | 97.9% | 94.3% | 97.4% | 79.0% |

---

## 📁 Project Structure
```text
├── model/
│   └── best.pt                  # Trained YOLOv8 weights
├── notebooks/
│   └── training_notebook.ipynb  # Training & evaluation workflow
├── app.py                       # Main application logic & Gradio interface
├── requirements.txt             # Python dependencies
├── run_app.bat                  # One-click Windows launcher
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation

🚀 Quick Start
Option 1: One-Click Launch (Windows)
Double-click run_app.bat to automatically launch the app.

Option 2: Command Line 

# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py