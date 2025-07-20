# ANIMAL PREDICTION: My Spirit Animal (Probably Not)

## Project Overview

This is a fun Python project that uses your webcam to detect faces and then humorously projects a corresponding animal image onto the video feed. It's designed to bring a smile to your face by giving you a random "spirit animal" based on face detection!

## Features

* **Real-time Face Detection:** Utilizes OpenCV's pre-trained Haar Cascade classifiers for efficient face detection in live webcam streams.
* **Dynamic Animal Suggestions:** When a face is detected, a random "spirit animal" is chosen from a curated list of funny and interesting animals.
* **Image Projection:** Instead of just text, the actual picture of the suggested animal is dynamically resized and overlaid onto the webcam stream, appearing above or near your detected face. This creates a visually engaging and amusing effect.
* **User-Friendly Interaction:** Simple to run and interact with, requiring only a webcam and a few key presses to start and stop.

## Setup and Installation

### Prerequisites

* **Python 3.x:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
* **Webcam:** A functional webcam connected to your computer.

### 1. Project Files

Ensure your project directory is structured as follows:
ANIMAL PREDICTION/
├── funny_animals.py         # The main Python script
├── haarcascade_frontalface_default.xml # OpenCV's pre-trained face detection model
└── animal_images/           # This folder contains all your animal picture files
├── sassy_sloth.png
├── goofy_goat.png
└── ... (include all your animal image files here)
### 2. Install Dependencies

Open your terminal or command prompt and run the following command to install the necessary Python library:

```bash
pip install opencv-python
