# Hand Gesture Recognition System

This project is a hand gesture recognition system implemented in Python using the OpenCV and Mediapipe libraries.
The system is capable of recognizing and interpreting various hand gestures such as "yo," "awesome," "peace," "stop" 
and more.

## Description

The Hand Gesture Recognition System utilizes computer vision techniques to detect and analyze hand movements in 
real-time video input. It leverages the power of OpenCV and Mediapipe libraries to extract hand landmarks and track 
their positions. These landmarks are then used to recognize specific hand gestures and perform corresponding actions 
or provide relevant feedback.

## Features

- Real-time hand gesture recognition:
  The system can detect and recognize hand gestures in real-time, providing instantaneous feedback.
- Multiple gesture recognition:
  It supports a range of hand gestures, including "yo," "awesome," "peace," "stop," and more. Additional gestures can
  be added easily.
- Hand landmark detection:
  The system employs Mediapipe library to extract hand landmarks accurately, allowing precise gesture recognition.
- User-defined actions:
  Each recognized gesture can trigger a specific action or perform a desired function based on the application
  requirements.
- Easy integration: The system is implemented in Python, making it compatible with various platforms and easy to
  integrate into existing projects.

## Requirements

- Python (version >= 3.x)
- OpenCV (version >= 4.x)
- Mediapipe (version >= 0.8.7)

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/hand-gesture-recognition.git

2. Navigate to the project directory:

   cd hand-gesture-recognition

3. Install the required dependencies using pip:

   pip install -r requirements.txt

## Usage

1. Run the main script:

   python main.py

2. The system will start capturing video from the default camera and display the real-time hand gesture recognition
   output.

3. Perform different hand gestures within the camera frame, and the system will recognize and display the recognized
   gesture on the screen.

4. Customize the actions associated with each gesture in the code as per your requirements.


## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your modifications.
4. Commit and push your changes to your fork.
5. Submit a pull request, explaining your changes in detail.

Please ensure your code adheres to the existing coding style and includes appropriate documentation and test cases.

## Acknowledgments

This project was inspired by the work of the open-source computer vision community and the contributions made by the 
developers of OpenCV and Mediapipe.
