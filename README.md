# Face Recognition System

This project is a **facial recognition-based attendance system** built using Python, OpenCV, and the dlib library. It detects faces, recognizes them from a dataset, and marks attendance based on the recognized faces.

## Features:
- Real-time face detection using OpenCV.
- Face recognition from a pre-trained dataset.
- Attendance recording in a database (SQLite).

## Project Structure:
- **Lib/**: Python dependencies and packages.
- **attendance_system_facial_recognition/**: Core logic for face detection and recognition.
- **face_recognition_data/**: Stores datasets and training data.
- **db.sqlite3**: The SQLite database used for storing attendance records.

## Requirements:
Install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
