# Dog Breed Classifier

## Inspiration
As dog lovers and machine learning enthusiasts, I wanted to create an application that could identify dog breeds from images. This project combines my love for dogs with the power of AI to create a user-friendly tool for dog breed identification.

## What it does
The Dog Breed Classifier is a desktop application that allows users to upload an image of a dog, and using a trained machine learning model, it predicts the breed of the dog in the image. The application provides the top three most likely breed predictions along with their confidence percentages.

## How to use it
1. Clone the repository to your local machine.
2. Ensure you have all the required dependencies installed (see requirements.txt). <strong>Requires python 3.8+</strong>
3. Run the `GUI.py` file to launch the application.
4. Click on "Choose Image" to select a dog image from your computer.
5. Click "Detect" to see the breed predictions.

## How I built it
This application was developed using:
- Python for the backend logic and machine learning model
- PyQt5 for the graphical user interface
- TensorFlow and Keras for training and deploying the machine learning model
- OpenCV and Pillow for image processing
- Git LFS for managing large files (like the trained model)
- The training code can be found [here](https://github.com/PraisEneh/Dog-Breed-Classifier)

## Challenges I ran into
Some of the major challenges I faced included:
- Ensuring cross-platform compatibility between Windows and macOS
- Managing large files (like the trained model) with Git LFS
- Further finetuning, using frozen weights, for more nuanced predictions
- Optimizing the model for both accuracy and speed

## Accomplishments that I'm proud of
I'm particularly proud of:
- Creating a user-friendly interface that makes AI accessible to non-technical users
- Achieving high accuracy of 90% in breed prediction across a wide range of dog breeds
- Successfully implementing a cross-platform application that works on both Windows and macOS

## What I learned
Through this project, I gained valuable experience in:
- Developing cross-platform desktop applications with PyQt5
- Training and fine-tuning deep learning models for image classification
- Handling large files in Git repositories
- Integrating complex backend systems with user-friendly front-end interfaces

## What's next for Dog Breed Classifier
I have several ideas for future enhancements:
- Expanding the database to include more rare dog breeds
- Implementing a feature to identify multiple dogs in a single image
- Adding a feature to provide more information about each identified breed via RAG and LLMs
- Developing a web version of the application for on-the-go breed identification
