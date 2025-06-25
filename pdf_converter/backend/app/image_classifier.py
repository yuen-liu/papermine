# image_classifier.py
# Handles classification of images as plot, table, or figure

from PIL import Image
import numpy as np
import pytesseract

def classify_image(image):
    # Convert to grayscale and numpy array
    gray = image.convert('L')
    arr = np.array(gray)
    h, w = arr.shape
    aspect_ratio = w / h
    # Heuristic: wide and short = table, tall = figure, square = plot
    if aspect_ratio > 1.5:
        return 'table'
    elif 0.8 < aspect_ratio < 1.2:
        # Try to detect if it's a plot (has axes/lines)
        # Heuristic: check for lines (edges)
        edges = np.mean(np.abs(np.diff(arr, axis=0))) + np.mean(np.abs(np.diff(arr, axis=1)))
        if edges > 10:
            return 'plot'
        else:
            return 'figure'
    else:
        # If a lot of text, likely a table
        text = pytesseract.image_to_string(image)
        if len(text.split()) > 10:
            return 'table'
        return 'figure' 