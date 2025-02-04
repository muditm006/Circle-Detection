# Circle Detection

This repository contains Python programs designed to detect circles in images and videos. The objective is to process input media, identify the largest circles, and overlay them with visual markers. The project uses **OpenCV**, **NumPy**, and built-in image transformation methods for circle detection and perspective transformations.

## Features

- **Circle Detection in Images**  
  Detects circles in static images using the Hough Circle Transform and overlays them with visual markers.

- **Circle Detection in Videos**  
  Processes video frames in real-time to detect and highlight rolling objects (e.g., a rolling can).

- **Perspective Transformations**  
  Applies perspective transformations to adjust the input image or video for better circle detection.

- **Real-Time Visualization**  
  Displays processed images or video frames with detected circles highlighted.

## File Descriptions

- **can_1.py**  
  Processes static images to detect and highlight circles. Includes:
  - Perspective transformations for specific image dimensions.
  - Circle detection using the Hough Circle Transform.
  - Visual overlays (circles and bounding rectangles) on detected objects.
  - Displays side-by-side comparisons of original and processed images.

- **can.py**  
  Processes video files to detect circles in real-time. Includes:
  - Frame-by-frame analysis of video footage.
  - Circle detection using the Hough Circle Transform.
  - Visual overlays (circles and center points) on detected objects.
  - Real-time display of processed video frames.

- **README.md**  
  Provides an overview of the project, its features, file descriptions, and usage instructions.

## How to Use

1. Clone this repository to your local machine:
git clone https://github.com/muditm006/Circle-Detection.git
cd Circle-Detection

2. Install the required Python libraries:
pip install numpy opencv-python

3. To process an image:
- Run `can_1.py` with the path to your image file:
  ```
  python can_1.py --image path/to/your/image.jpg
  ```
- View the original image alongside the processed image with detected circles.

4. To process a video:
- Replace `'roll.MOV'` in `can.py` with the path to your video file.
- Run `can.py`:
  ```
  python can.py
  ```
- View the real-time detection of circles in the video frames.

5. Press `q` during video processing to exit.

## Libraries Used

- **OpenCV**: For image processing, circle detection, and transformations.
- **NumPy**: For numerical operations and array manipulations.
- **argparse**: For command-line argument parsing (used in `can_1.py`).

## Notes

This project demonstrates advanced image processing techniques using Python's OpenCV library. It is designed for detecting circular objects in both static images and dynamic videos, with customizable parameters for circle size, detection thresholds, and more.
