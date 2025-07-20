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
```
### 3. Obtain Haar Cascade Classifier
The haarcascade_frontalface_default.xml file is essential for the face detection to work.

Download it: Visit the official OpenCV GitHub repository and download the file:
https://github.com/opencv/opencv/tree/master/data/haarcascades

Placement: Place this .xml file directly in the ANIMAL PREDICTION folder, alongside your funny_animals.py script.
### 4.Prepare Animal Images
The project needs specific image files for each animal you want to display.

Create animal_images Folder: If it doesn't exist, create a folder named animal_images inside your ANIMAL PREDICTION directory.

Source Images: Find or create images for each animal. .png files with transparent backgrounds are recommended for a better overlay effect, but .jpg files will also work.

Naming Convention: It is crucial that the filenames of your images exactly match the names used in the ANIMAL_IMAGE_MAP dictionary within your funny_animals.py script. For example, if your script maps "Sassy Sloth" to "sassy_sloth.png", then you must have a file named sassy_sloth.png in your animal_images folder.

Placement: Put all these animal image files inside the animal_images folder.
## 1. How to Run
Navigate to Project Directory:
Open your terminal or command prompt. Use the cd command to navigate to your ANIMAL PREDICTION project folder.

Example:

Bash

cd C:\Users\YASWINI PRIYA\OneDrive\Desktop\Animal_prediction
(Please replace this path with the actual location of your folder.)
## 2. Execute the Script:
Once in the correct directory, run the Python script using:

Bash

python funny_animals.py
A window showing your webcam feed will appear.
## 3.Enjoy the Show:
Position your face clearly in front of the camera. After a brief moment, a randomly selected animal image will appear above or near your detected face! The animal suggestion will periodically change as long as a face is detected.

## 4.Quit:
To close the application window, simply press the q key on your keyboard.

## Contributing
Feel free to fork this repository, explore its code, make improvements, and submit pull requests! Your contributions to make this project even funnier or more robust are welcome.

## License
This project is open-source. (You may consider adding a specific license like the MIT License if you wish to formally define how others can use, modify, and distribute your code.)
