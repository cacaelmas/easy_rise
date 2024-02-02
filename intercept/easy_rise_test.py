import random
import time

import win32api
import win32gui

# The example starts here
from AutoHotPy import AutoHotPy  # we need to tell python that we are going to use the library


#TESTING
import cv2
import pytesseract
from PIL import ImageGrab
import os
import  numpy as np

import numpy as np


def nothing(x):
    pass

def enhance_contrast(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # Convert to LAB color space
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    l = clahe.apply(l)

    # Merge channels and convert back to BGR color space
    enhanced_lab = cv2.merge([l, a, b])
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    return enhanced_image

def enhance_contrast_grayscale(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to a grayscale image
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    enhanced_image = clahe.apply(image)

    return enhanced_image

def refine_red_extraction_and_debug(image, specific_red_rgb, save_path_prefix):
    # Ensure the save_path_prefix directory exists
    os.makedirs(os.path.dirname(save_path_prefix), exist_ok=True)

    img = image

    # # Create a window
    # cv2.namedWindow('image')
    #
    # # create trackbars for color change
    # cv2.createTrackbar('HMin', 'image', 0, 179, nothing)  # Hue is from 0-179 for Opencv
    # cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
    # cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
    # cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
    # cv2.createTrackbar('VMax', 'image', 0, 255, nothing)
    #
    # # Set default value for MAX HSV trackbars.
    # cv2.setTrackbarPos('HMax', 'image', 179)
    # cv2.setTrackbarPos('SMax', 'image', 255)
    # cv2.setTrackbarPos('VMax', 'image', 255)
    #
    # # Initialize to check if HSV min/max value changes
    # hMin = sMin = vMin = hMax = sMax = vMax = 0
    # phMin = psMin = pvMin = phMax = psMax = pvMax = 0
    #
    # output = image
    # wait_time = 33
    #
    # while (1):
    #
    #     # get current positions of all trackbars
    #     hMin = cv2.getTrackbarPos('HMin', 'image')
    #     sMin = cv2.getTrackbarPos('SMin', 'image')
    #     vMin = cv2.getTrackbarPos('VMin', 'image')
    #
    #     hMax = cv2.getTrackbarPos('HMax', 'image')
    #     sMax = cv2.getTrackbarPos('SMax', 'image')
    #     vMax = cv2.getTrackbarPos('VMax', 'image')
    #
    #     # Set minimum and max HSV values to display
    #     lower = np.array([hMin, sMin, vMin])
    #     upper = np.array([hMax, sMax, vMax])
    #
    #     # Create HSV Image and threshold into a range.
    #     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #     mask = cv2.inRange(hsv, lower, upper)
    #     output = cv2.bitwise_and(image, image, mask=mask)
    #
    #     # Print if there is a change in HSV value
    #     if ((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax)):
    #         print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (
    #         hMin, sMin, vMin, hMax, sMax, vMax))
    #         phMin = hMin
    #         psMin = sMin
    #         pvMin = vMin
    #         phMax = hMax
    #         psMax = sMax
    #         pvMax = vMax
    #
    #     # Display output image
    #     cv2.imshow('image', output)
    #
    #     # Wait longer to prevent freeze for videos.
    #     if cv2.waitKey(wait_time) & 0xFF == ord('q'):
    #         break
    #
    # cv2.destroyAllWindows()
    # exit(1)

    lower = np.array([18, 0, 0])
    upper = np.array([179, 255, 255])

    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"{save_path_prefix}output_img_00_NEW.png", output)

    image = output
    # Apply the mask to isolate red color
    isolated_red = cv2.bitwise_and(image, image, mask=mask)
    cv2.imwrite(f"{save_path_prefix}_03_isolated_red.png", isolated_red)

    # Convert to grayscale
    gray_image = cv2.cvtColor(isolated_red, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"{save_path_prefix}_04_gray.png", gray_image)

    # Enhance contrast using histogram equalization
    equalized_image = cv2.equalizeHist(gray_image)
    cv2.imwrite(f"{save_path_prefix}_05_equalized.png", equalized_image)

    # Background is black, text is white. just reverse and return
    #your code
    # Invert the image to get white background and black text
    inverted_image = cv2.bitwise_not(equalized_image)
    cv2.imwrite(f"{save_path_prefix}_06_inverted_for_ocr.png", inverted_image)

    new_img = enhance_contrast_grayscale(inverted_image)
    contrasted_image_path = f"{save_path_prefix}_07_contrasted_for_ocr.png"
    cv2.imwrite(contrasted_image_path, new_img)

    return inverted_image


def process_and_extract_text(screenshot, save_path_prefix):
    image = np.array(screenshot)
    specific_red_rgb = [239, 50, 110]  # The specific red of the text
    processed_image = refine_red_extraction_and_debug(image, specific_red_rgb, save_path_prefix)
    cv2.imwrite(f"{save_path_prefix}ocr_input_image.png", processed_image)

    text = pytesseract.image_to_string(processed_image, config='--psm 6')
    return text.strip()


# Setup paths and pytesseract executable location
save_path_prefix = 'C:\\Users\\pFFed\\PycharmProjects\\easyko'  # Update this path as needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'

# Define coordinates and dimensions for the image capture
x, y = 146, 1272
width, height = 400, 30

# Extract text
screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

debug_image_path = "first_debug_screenshot.png"
screenshot.save(debug_image_path)

# Convert screenshot to numpy array and change color space from RGB (PIL default) to BGR (OpenCV default)
image_array = np.array(screenshot)
image_array_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)  # Convert to BGR before saving with OpenCV

# Now, save with OpenCV
cv2.imwrite(f"{save_path_prefix}_first_debug_image.png", image_array_bgr)
extracted_text = process_and_extract_text(screenshot, save_path_prefix)
print(f"Extracted text: {extracted_text}")


# Use OpenCV to read the image for further processing
image = cv2.imread(debug_image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply CLAHE to enhance the contrast of the grayscale image
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
enhanced_image = clahe.apply(gray_image)

# Save the enhanced image for debugging
debug_enhanced_image_path = "debug_enhanced_screenshot.png"
cv2.imwrite(debug_enhanced_image_path, enhanced_image)
print(f"Enhanced grayscale screenshot saved to {debug_enhanced_image_path}")

# Extract text from the enhanced image using pytesseract
text = pytesseract.image_to_string(enhanced_image)
print("Extracted Text:")
print(text)
exit(1)

#END TESTING