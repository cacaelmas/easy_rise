# -*- coding: utf-8 -*-
"""
@author: Emilio Moretti
Copyright 2013 Emilio Moretti <emilio.morettiATgmailDOTcom>
This program is distributed under the terms of the GNU Lesser General Public License.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
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



# CONFIGURATION
HEALING_POT_KEY = 0  # Change accordingly
MANA_POT_KEY = 9  # Change accordingly
HEAL_PARTY_MEMBER_KEY = 2  # Change accordingly
start_time=0

# Available pages -> F1, F2, F3, F4, F5, F6, F7
ACTIVE_SKILL_PAGES = {
    #'F4': [1,2,3,4,5]  # Change accordingly
    'F1':[2]
}

# Be careful not to overlap any skills with your HEAL/MANA pot keys

# One skill page with F4 example is below
# ACTIVE_SKILL_PAGES = {
#     'F4': [3, 4, 5, 6]
# }

ENABLE_R_HITS = True  # Change it to True for basic attacks

# Do not change anything below this line
SELF_HP_X = 195
SELF_HP_Y = 46

SELF_MP_X = 180
SELF_MP_Y = 66

MONSTER_HP_X=960-30
MONSTER_HP_y=46

FIRST_PARTY_MEMBER_X = 1799
FIRST_PARTY_MEMBER_Y = 258
CURRENT_PARTY = []
PARTY_VALID_R = 159
PARTY_VALID_G = 57
PARTY_VALID_B = 39
PARTY_MEMBER_OFFSET_Y = 145

repeat_always = False
is_r_used=False

SELECTED_RUNTIME_CONFIGURATION = 0  # None
TIME_DELAY_BETWEEN_SKILLS = 0.1  # in seconds

HP_R = 0
HP_G = 0
HP_B = 0
MP_R = 0
MP_G = 0
MP_B = 0

# END CONFIGURATION

# IMAGE PROCESSING

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

def extractMobName():
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    debug_image_path = "first_debug_screenshot.png"
    screenshot.save(debug_image_path)
    extracted_text = process_and_extract_text(screenshot, save_path_prefix)
    return extracted_text

# END IMAGE PROCESSING



# INITIALIZATION
def readPixel(x, y):
    if x >= 1920:
        x = 1919
    if y >= 1080:
        y = 1079
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    return r, g, b

def checkMonsterHealtLow():
    global HP_R
    x, y = MONSTER_HP_X, MONSTER_HP_y
    r, g, b = readPixel(x, y)
    if(r+10<HP_R):
        return True
    else:
        return False

def checkMana():
    global SELF_MP_R, SELF_MP_G, SELF_MP_B, SELF_MP_X, SELF_MP_Y
    x, y = SELF_MP_X, SELF_MP_Y
    r, g, b = readPixel(x, y)
    # print("Checking mana with RGB: {}, {}, {} against {}, {}, {}".format(r, g, b, MP_R, MP_G, MP_B))
    if r == SELF_MP_R and g == SELF_MP_G and b == SELF_MP_B:
         return False
     #   print("MP is above 35%")
    else:
    #    print("Using MP with KEY {}".format(MANA_POT_KEY))
        return True


def checkHealth():
    global SELF_HP_R, SELF_HP_G, SELF_HP_B, SELF_HP_X, SELF_HP_Y
    x, y = SELF_HP_X, SELF_HP_Y
    r, g, b = readPixel(x, y)
    #print("Checking health with RGB: {}, {}, {} against {}, {}, {}".format( r, g, b, HP_R, HP_G, HP_B))
    if r == SELF_HP_R and g == SELF_HP_G and b == SELF_HP_B:
        return False
         #print("\n")
       # print("HP is above 40%")
    else:
      #  print("Using HP with KEY {}".format(HEALING_POT_KEY))
        return True

def checkRepair():
    global SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B, SELF_ITEM_X, SELF_ITEM_Y
    x, y = SELF_ITEM_X, SELF_ITEM_Y
    r, g, b = readPixel(x, y)
    #print("Checking health with RGB: {}, {}, {} against {}, {}, {}".format( r, g, b, HP_R, HP_G, HP_B))
    if r < 200:
        return False
         #print("\n")
       # print("HP is above 40%")
    else:
      #  print("Using HP with KEY {}".format(HEALING_POT_KEY))
        return True


def checkPartyMemberHealth(x, y):
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    if r < 75:
        print("Party member [{},{}] is at RGB: {}, {}, {}".format(
            x, y, r, g, b))

def rgbint2rgbtuple(RGBint):
    red = RGBint & 255
    green = (RGBint >> 8) & 255
    blue = (RGBint >> 16) & 255
    return (red, green, blue)

def recordColorOfCursorPos():
    for i in range(5,0,-1):
        print("Recording color in {} seconds".format(i))
        time.sleep(1)
    x, y = win32api.GetCursorPos()
    r,g,b = readPixel(x,y)
    print("Recored r,g,b = {}, {}, {} at x,y = [{}, {}]".format(r,g,b,x,y))
    return x,y,r,g,b

print("Can nereye gelince pot basılsın? (mouse'u üzerinde beklet)")
SELF_HP_X, SELF_HP_Y, SELF_HP_R, SELF_HP_G, SELF_HP_B = recordColorOfCursorPos()

print("Mana nereye gelince pot basılsın? (mouse'u üzerinde beklet)")
SELF_MP_X, SELF_MP_Y, SELF_MP_R, SELF_MP_G, SELF_MP_B = recordColorOfCursorPos()

print("Hangi item kırılınca repair basılsın? (mouse'u üzerinde beklet ve inventory kapatma)")
SELF_ITEM_X, SELF_ITEM_Y, SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B = recordColorOfCursorPos()
SELF_ITEM_X = 2103
SELF_ITEM_Y = 663
SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B = readPixel(SELF_ITEM_X, SELF_ITEM_Y)
print("item rgb {} {} {}".format(SELF_ITEM_R, SELF_ITEM_G, SELF_ITEM_B))
# END INITIALIZATION


# The following function is called when you press ESC.
# autohotpy is the instance that controlls the library, you should do everything through it.
def exitAutoHotKey(autohotpy, event):
    """
    exit the program when you press ESC
    """
    print("Stopping with " + event)
    autohotpy.stop()  # makes the program finish successfully. Thisis the right way to stop it


def waitBetweenKeys():
    random_number = random.uniform(0.05, 0.1)
    time.sleep(random_number)

def pressZ(autohotpy):
    autohotpy.Z.press()
    waitBetweenKeys()
    return extractMobName()




def superCombo(autohotpy, event):
    """
    This function is called when you press "A" key.
    It executes the combo: A -> S -> move left -> move up -> A -> S
    """

    r_started = False
    for i in range(0, 1000):
        autohotpy.N3.press()
        waitBetweenKeys()

        autohotpy.N7.press()
        waitBetweenKeys()

        autohotpy.N8.press()
        waitBetweenKeys()

        #mob_name = pressZ(autohotpy)
        autohotpy.Z.press()
        waitBetweenKeys()
        #
        # if len(mob_name) > 2:
        autohotpy.R.press()
        waitBetweenKeys()


        waitBetweenKeys()

        autohotpy.N2.press()
        waitBetweenKeys()

        if checkHealth():
            print("Health needed!")
            autohotpy.N0.press()

        if checkMana():
            print("Mana needed!")
            autohotpy.N9.press()

        if checkRepair():
            print("Repair needed!")
            autohotpy.N6.press()

    # autohotpy.A.press()  # press() method simulates a key press by sending first the key down, and later the key up events
    # autohotpy.S.press()
    # autohotpy.LEFT_ARROW.press()
    # autohotpy.UP_ARROW.press()
    # autohotpy.A.press()
    # autohotpy.S.press()




# THIS IS WERE THE PROGRAM STARTS EXECUTING!!!!!!!!s
if __name__ == "__main__":
    auto = AutoHotPy()  # Initialize the library
    auto.registerExit(auto.ESC,
                      exitAutoHotKey)  # Registering an end key is mandatory to be able to stop the program gracefully
    auto.registerForKeyDown(auto.F10,
                            superCombo)  # This method lets you say: "when I press A in the keyboard, then execute "superCombo"
    auto.start()  # Now that everything is registered we should start runnin the program
