#!/usr/bin/env python3

import cv2
import numpy as np
import sys

symbols_list = ["#", "-", "*", ".", "+", "o"]
threshold_list = [0, 50, 100, 150, 200]

def print_out_ascii(array):
    """Prints the coded image with symbols."""
    for row in array:
        for e in row:
            print(symbols_list[int(e) % len(symbols_list)], end="")
        print()

def img_to_ascii(image):
    """Converts an image to ASCII representation."""
    if image is None:
        raise ValueError("Error: Unable to load the image. Check if the file path is correct and the image exists.")

    # Resizing parameters
    height, width = image.shape
    new_width = int(width / 20) 
    new_height = int(height / 40)

    # Resize image to fit the printing screen
    resized_image = cv2.resize(image, (new_width, new_height))

    thresh_image = np.zeros(resized_image.shape)

    for i, threshold in enumerate(threshold_list):
        # Assign corresponding values according to the index of threshold applied
        thresh_image[resized_image > threshold] = i
    return thresh_image

if __name__ == "__main__":
    # Default image path
    image_path = "sample_image.png"

    if len(sys.argv) == 2:
        print(f"Using {sys.argv[1]} as Image Path\n")
        image_path = sys.argv[1]

    # Load the image
    image = cv2.imread(image_path, 0)

    if image is None:
        print(f"Error: Unable to read image at '{image_path}'.\nCheck if the file exists and the path is correct.")
        sys.exit(1)

    # Convert to ASCII and print
    ascii_art = img_to_ascii(image)
    print_out_ascii(ascii_art)
