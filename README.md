# Image Background Remover

This Streamlit application allows users to upload an image and remove its background. The app uses the `rembg` library to process the image and provides options to view the original and processed images side by side. Users can also download the processed image with the background removed.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)


## Features

- Upload and process images to remove their background.
- Display original and processed images side by side.
- Download the processed image directly from the app.
- Size validation to ensure the uploaded image does not exceed 5MB.

## Installation

To install and run the project on your local machine, follow these steps:

1. Clone this repository or download the zip file.
   
   ```bash
   git clone https://github.com/yourusername/image-background-remover.git
## Usage
1. After running the app, go to the sidebar and use the "Upload the image" button to upload an image file (JPG, JPEG, or PNG).
2. If the image file size exceeds 5MB, you will receive a warning. Ensure the image size is within the limit.
3. The app will display the original and processed images side by side.
4. Click the "Download Image" button in the sidebar to download the processed image with the background removed.
## Dependencies
- Streamlit: For creating the web application interface.
- rembg: For removing the background from images.
- PIL (Pillow): For image processing.
- io: For handling image byte streams.
