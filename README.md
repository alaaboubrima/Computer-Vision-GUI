# Computer Vision Project

This repository contains a comprehensive implementation of various image processing techniques using Python and OpenCV, integrated into a PyQt5 GUI application. The project covers a range of operations including histogram manipulation, image segmentation, histogram equalization, dynamic range expansion, and more.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases various computer vision techniques implemented in Python using OpenCV, wrapped in a PyQt5-based GUI for easy interaction. The application allows users to load images, perform operations such as histogram analysis, image inversion, segmentation, and more, and visualize the results directly.

## Features

### 1. **File Browsing and Image Loading**
   - Load images in different formats like `.png`, `.jpg`, etc.
   - Display the loaded image with dimensions.

### 2. **Histogram Operations**
   - **Histogram Calculation**: Compute and display the histogram of an image.
   - **Cumulative Histogram**: Compute and display the cumulative histogram.
   - **Normalized Histogram**: Display the histogram normalized by the total number of pixels.

### 3. **Image Manipulation**
   - **Inversion**: Invert the grayscale values of an image.
   - **Segmentation**: Segment the image based on user-defined intensity thresholds.
   - **Histogram Equalization**: Perform histogram equalization to enhance the image contrast.
   - **Dynamic Range Expansion**: Expand the dynamic range of an image for better contrast.
   - **Image Translation**: Translate the intensity values of the image.
   - **Quantization**: Perform color and grayscale quantization using k-means clustering.

### 4. **Advanced Operations**
   - **Median Quantization**: Apply median quantization to both color and grayscale images.
   - **Uniform Quantization**: Perform uniform quantization on images.
   - **Connected Component Labeling**: Label connected components in a binary image.
   - **Video Processing**: Load and play videos, with options to extract frames.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/computer-vision-project.git
   cd computer-vision-project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python TAI_Algorithmes.py
   ```

## Usage

1. **Loading an Image**: Use the "Browse" button to load an image from your local machine.
2. **Performing Operations**: Choose from the available operations (e.g., Histogram, Inversion, Segmentation) from the GUI and visualize the results in real-time.
3. **Saving Results**: Results can be saved or further processed as required.


## Dependencies

- OpenCV
- NumPy
- Matplotlib
- PyQt5

Install the dependencies using:
```bash
pip install -r requirements.txt
```