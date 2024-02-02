# coding=utf-8
# DEPENDENCIES
# pywin32-220.win32-py2.7
# to use win32gui and win32api
# pyHook-1.5.1.win32-py2.7
# for 64 bit systems: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook
# pyHook‑1.5.1‑cp27‑cp27m‑win_amd64.whl
# to use pyhook
# win32 libs http://www.lfd.uci.edu/~gohlke/pythonlibs
import ctypes
import datetime
import os

import math
import sched
import threading
import time
import win32api
import win32gui

import numpy as np
import win32con
import pythoncom
import pyHook
# from ScreenChatFeeder import ScreenChatFeeder
# from defpack.FTNoticeClicker import FTNoticeClicker
# from defpack.FirebaseHandler import FirebaseHandler
# from defpack.ImageComparator import ImageComparator
# from defpack.PMHandler import PMHandler, NewPMListener
# from defpack.kobjects.MouseColorListener import MouseColorListener
#from defpack import IOWriter
#from defpack.MouseColorListener import MouseColorListener


#import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'


s = sched.scheduler(time.time, time.sleep)
# definitions
# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
import ctypes
import time
# definitions
# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# Listed are keyboard scan code constants, taken from dinput.h
import win32api

import win32con

KEY_ESCAPE = 0x01
KEY_1 = 0x02
KEY_2 = 0x03
KEY_3 = 0x04
KEY_4 = 0x05
KEY_5 = 0x06
KEY_6 = 0x07
KEY_7 = 0x08
KEY_8 = 0x09
KEY_9 = 0x0A
KEY_0 = 0x0B
KEY_MINUS = 0x0C  # - on main keyboard */
KEY_EQUALS = 0x0D
KEY_BACK = 0x0E  # backspace */
KEY_TAB = 0x0F
KEY_Q = 0x10
KEY_W = 0x11
KEY_E = 0x12
KEY_R = 0x13
KEY_T = 0x14
KEY_Y = 0x15
KEY_U = 0x16
KEY_I = 0x17
KEY_O = 0x18
KEY_P = 0x19
KEY_LBRACKET = 0x1A
KEY_RBRACKET = 0x1B
KEY_RETURN = 0x1C  # Enter on main keyboard */
KEY_LCONTROL = 0x1D
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20
KEY_F = 0x21
KEY_G = 0x22
KEY_H = 0x23
KEY_J = 0x24
KEY_K = 0x25
KEY_L = 0x26
KEY_SEMICOLON = 0x27
KEY_APOSTROPHE = 0x28
KEY_GRAVE = 0x29  # accent grave */
KEY_LSHIFT = 0x2A
KEY_BACKSLASH = 0x2B
KEY_Z = 0x2C
KEY_X = 0x2D
KEY_C = 0x2E
KEY_V = 0x2F
KEY_B = 0x30
KEY_N = 0x31
KEY_M = 0x32
KEY_COMMA = 0x33
KEY_PERIOD = 0x34  # . on main keyboard */
KEY_SLASH = 0x35  # / on main keyboard */
KEY_RSHIFT = 0x36
KEY_MULTIPLY = 0x37  # * on numeric keypad */
KEY_LMENU = 0x38  # left Alt */
KEY_SPACE = 0x39
KEY_CAPITAL = 0x3A
KEY_F1 = 0x3B
KEY_F2 = 0x3C
KEY_F3 = 0x3D
KEY_F4 = 0x3E
KEY_F5 = 0x3F
KEY_F6 = 0x40
KEY_F7 = 0x41
KEY_F8 = 0x42
KEY_F9 = 0x43
KEY_F10 = 0x44
KEY_NUMLOCK = 0x45
KEY_SCROLL = 0x46  # Scroll Lock */
KEY_NUMPAD7 = 0x47
KEY_NUMPAD8 = 0x48
KEY_NUMPAD9 = 0x49
KEY_SUBTRACT = 0x4A  # - on numeric keypad */
KEY_NUMPAD4 = 0x4B
KEY_NUMPAD5 = 0x4C
KEY_NUMPAD6 = 0x4D
KEY_ADD = 0x4E  # + on numeric keypad */
KEY_NUMPAD1 = 0x4F
KEY_NUMPAD2 = 0x50
KEY_NUMPAD3 = 0x51
KEY_NUMPAD0 = 0x52
KEY_DECIMAL = 0x53  # . on numeric keypad */
KEY_F11 = 0x57
KEY_F12 = 0x58

KEY_F13 = 0x64  # (NEC PC98) */
KEY_F14 = 0x65  # (NEC PC98) */
KEY_F15 = 0x66  # (NEC PC98) */

KEY_KANA = 0x70  # (Japanese keyboard)            */
KEY_CONVERT = 0x79  # (Japanese keyboard)            */
KEY_NOCONVERT = 0x7B  # (Japanese keyboard)            */
KEY_YEN = 0x7D  # (Japanese keyboard)            */
KEY_NUMPADEQUALS = 0x8D  # = on numeric keypad (NEC PC98) */
KEY_CIRCUMFLEX = 0x90  # (Japanese keyboard)            */
KEY_AT = 0x91  # (NEC PC98) */
KEY_COLON = 0x92  # (NEC PC98) */
KEY_UNDERLINE = 0x93  # (NEC PC98) */
KEY_KANJI = 0x94  # (Japanese keyboard)            */
KEY_STOP = 0x95  # (NEC PC98) */
KEY_AX = 0x96  # (Japan AX) */
KEY_UNLABELED = 0x97  # (J3100) */
KEY_NUMPADENTER = 0x9C  # Enter on numeric keypad */
KEY_RCONTROL = 0x9D
KEY_NUMPADCOMMA = 0xB3  # , on numeric keypad (NEC PC98) */
KEY_DIVIDE = 0xB5  # / on numeric keypad */
KEY_SYSRQ = 0xB7
KEY_RMENU = 0xB8  # right Alt */
KEY_HOME = 0xC7  # Home on arrow keypad */
KEY_UP = 0xC8  # UpArrow on arrow keypad */
KEY_PRIOR = 0xC9  # PgUp on arrow keypad */
KEY_LEFT = 0xCB  # LeftArrow on arrow keypad */
KEY_RIGHT = 0xCD  # RightArrow on arrow keypad */
KEY_END = 0xCF  # End on arrow keypad */
KEY_DOWN = 0xD0  # DownArrow on arrow keypad */
KEY_NEXT = 0xD1  # PgDn on arrow keypad */
KEY_INSERT = 0xD2  # Insert on arrow keypad */
KEY_DELETE = 0xD3  # Delete on arrow keypad */
KEY_LWIN = 0xDB  # Left Windows key */
KEY_RWIN = 0xDC  # Right Windows key */
KEY_APPS = 0xDD  # AppMenu key */

#  Alternate names for keys, to facilitate transition from DOS.
KEY_BACKSPACE = KEY_BACK  # backspace */
KEY_NUMPADSTAR = KEY_MULTIPLY  # * on numeric keypad */
KEY_LALT = KEY_LMENU  # left Alt */
KEY_CAPSLOCK = KEY_CAPITAL  # CapsLock */
KEY_NUMPADMINUS = KEY_SUBTRACT  # - on numeric keypad */
KEY_NUMPADPLUS = KEY_ADD  # + on numeric keypad */
KEY_NUMPADPERIOD = KEY_DECIMAL  # . on numeric keypad */
KEY_NUMPADSLASH = KEY_DIVIDE  # / on numeric keypad */
KEY_RALT = KEY_RMENU  # right Alt */
KEY_UPARROW = KEY_UP  # UpArrow on arrow keypad */
KEY_PGUP = KEY_PRIOR  # PgUp on arrow keypad */
KEY_LEFTARROW = KEY_LEFT  # LeftArrow on arrow keypad */
KEY_RIGHTARROW = KEY_RIGHT  # RightArrow on arrow keypad */
KEY_DOWNARROW = KEY_DOWN  # DownArrow on arrow keypad */
KEY_PGDN = KEY_NEXT  # PgDn on arrow keypad */
KEY_TAB = 0x0F
KEY_ENTER = 0x1C
KEY_R = 0x13
KEY_B = 0x30

ARROW_UP = 0xC8
ARROW_RIGHT = 0xCD
ARROW_DOWN = 0xD0
ARROW_LEFT = 0xCB

KEY_Z = 0x5A
KEY_ESCAPE = 0x01
KEY_1 = 0x02
KEY_2 = 0x03
KEY_3 = 0x04
KEY_4 = 0x05
KEY_5 = 0x06
KEY_6 = 0x07
KEY_7 = 0x08
KEY_8 = 0x09
KEY_9 = 0x0A
KEY_0 = 0x0B
KEY_W = 0x11
KEY_R = 0x13
KEY_A = 0x1E
KEY_S = 0x1F
KEY_D = 0x20
KEY_TAB = 0x0F
KEY_ENTER = 0x1C
KEY_H = 0x23
KEY_U = 0x16
KEY_I = 0x17
KEY_ESC = 0x01
KEY_F1 = 0x3B
KEY_F2 = 0x3C
KEY_F3 = 0x3D
KEY_F4 = 0x3E
KEY_F5 = 0x3F
KEY_F6 = 0x40
KEY_F7 = 0x41
KEY_F8 = 0x42
KEY_F9 = 0x43
KEY_F10 = 0X44
KEY_F11 = 0x57
KEY_F12 = 0x58
KEY_LCONTROL = 0x1D
KEYBOARD_DIRECTX_MAP = {49: KEY_1,
                        50: KEY_2,
                        51: KEY_3,
                        52: KEY_4,
                        53: KEY_5,
                        54: KEY_6,
                        55: KEY_7,
                        56: KEY_8,
                        57: KEY_9,
                        48: KEY_0,
                        87: KEY_W,
                        82: KEY_R,
                        65: KEY_A,
                        83: KEY_S,
                        68: KEY_D,
                        9: KEY_TAB,
                        13: KEY_ENTER,
                        72: KEY_H,
                        85: KEY_U,
                        73: KEY_I,
                        27: KEY_ESC,
                        112: KEY_F1,
                        113: KEY_F2,
                        114: KEY_F3,
                        115: KEY_F4,
                        116: KEY_F5,
                        117: KEY_F6,
                        118: KEY_F7,
                        119: KEY_F8,
                        120: KEY_F9,
                        121: KEY_F10,
                        122: KEY_F11,
                        123: KEY_F12,
                        66: KEY_B
                        }

print("Width =", win32api.GetSystemMetrics(0))
print("Height =", win32api.GetSystemMetrics(1))


class sharedObject:
    def __init__(self, key, posX, posY, action):
        self.key = key
        self.posX = posX
        self.posY = posY
        self.action = action


hp0x = 28
mp0x = 28

hpfirstHalfX = 96
hpsecondHalfX = 148

hp100x = 215
mp100x = 215

hpY = 42
mpY = 57

mobx1 = 856
moby1 = 10

mobx2 = 1046
moby2 = 30

HP_X = 150
HP_Y = 44
MP_X = 91
MP_Y = 59

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def rightClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def clickAndDrag(startX, startY, destinationX, destinationY):
    win32api.SetCursorPos((startX, startY))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, startX, startY, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((destinationX, destinationY))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, destinationX, destinationY, 0, 0)


def rgbint2rgbtuple(RGBint):
    red = RGBint & 255
    green = (RGBint >> 8) & 255
    blue = (RGBint >> 16) & 255
    return (red, green, blue)


def continousRightClick(x, y):
    time.sleep(2)
    while True:
        rightClick(x, y)
        time.sleep(0.1)

import pyHook
import pythoncom

# Assuming you have a flag variable defined somewhere in your script
# For example: flag = False
def getColorOfPixel(x, y):
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    return r, g, b


TIDAL_WAVE_ACTIVE = False
RIPTIDE_ACTIVE = True
PRIMORDIAL_WAVE_ACTIVE = True

def updatePrimordialWaveStatus():
    # print("TIDAL_WAVE_ACTIVE = {}".format(TIDAL_WAVE_ACTIVE))
    # print("RIPTIDE_ACTIVE = {}".format(RIPTIDE_ACTIVE))
    # print("PRIMORDIAL_WAVE_ACTIVE = {}".format(PRIMORDIAL_WAVE_ACTIVE))


    global PRIMORDIAL_WAVE_ACTIVE
    r, g, b = getColorOfPixel(666, 850)
    #print("Primordial= {}, {}, {}".format(r,g,b))
    if g > 60:
        PRIMORDIAL_WAVE_ACTIVE = True

    else:
        PRIMORDIAL_WAVE_ACTIVE = False

    twThread = threading.Thread(target=updatePrimordialWaveStatus)
    twThread.daemon = True
    twThread.start()
twThread = threading.Thread(target=updatePrimordialWaveStatus)
twThread.daemon = True
twThread.start()


def updateRiptideStatus():
    global RIPTIDE_ACTIVE
    r, g, b = getColorOfPixel(666, 920)
    #print("Riptide= {}, {}, {}".format(r,g,b))

    if g > 60:
        RIPTIDE_ACTIVE = True

    else:
        RIPTIDE_ACTIVE = False

    twThread = threading.Thread(target=updateRiptideStatus)
    twThread.daemon = True
    twThread.start()
twThread = threading.Thread(target=updateRiptideStatus)
twThread.daemon = True
twThread.start()

def updateTidalWaveStatus():
    global TIDAL_WAVE_ACTIVE
    r, g, b = getColorOfPixel(667, 981)
    #print("TidalWave= {}, {}, {}".format(r,g,b))

    if g > 60:
        TIDAL_WAVE_ACTIVE = True

    else:
        TIDAL_WAVE_ACTIVE = False

    twThread = threading.Thread(target=updateTidalWaveStatus)
    twThread.daemon = True
    twThread.start()
twThread = threading.Thread(target=updateTidalWaveStatus)
twThread.daemon = True
twThread.start()

VK_MENU = 0x12  # Alt key

def is_alt_pressed():
    """Check if Alt key is currently pressed."""
    return win32api.GetAsyncKeyState(VK_MENU) < 0

def OnKeyboardEvent(event):
    # Check if '3' is pressed
    if event.Ascii == 51:  # 51 is the ASCII code for '3'
        if is_alt_pressed():
            return True
        global TIDAL_WAVE_ACTIVE
        global RIPTIDE_ACTIVE
        global PRIMORDIAL_WAVE_ACTIVE

        if TIDAL_WAVE_ACTIVE:
            # Simulate 'E' key press if the flag is True
            print("pressing 3 -> CAST Chain Heal, Tidal Wave Active")
            return True
        else:
            # Do nothing if the flag is False, allowing the '3' key press to proceed
            print(datetime.datetime.now().strftime("%H:%M:%S"))

            if RIPTIDE_ACTIVE:
                # CAST Riptide
                print("pressing E -> CAST Riptide, Activating Tidal Wave")
                PressKey(KEY_E)  # 0x12 is the hex code for 'E'
                ReleaseKey(KEY_E)
                return False
            else:
                # CAST Primodial Wave
                if PRIMORDIAL_WAVE_ACTIVE:
                    print("pressing T -> CAST Primordial Wave, Activating Tidal Wave")
                    PressKey(KEY_T)  # 0x12 is the hex code for 'E'
                    ReleaseKey(KEY_T)
                    return False
                else:
                    # CAST Natures Swiftness Then Chain Heal
                    print("pressing 2 -> CAST Healing Wave, Consuming Primordial Wave")
                    PressKey(KEY_2)
                    ReleaseKey(KEY_2)
                    return False
            return False
    return True

# Create a hook manager
hm = pyHook.HookManager()
# Watch for all keyboard events
hm.KeyDown = OnKeyboardEvent
# Set the hook
hm.HookKeyboard()

# Enter into a perpetual loop to keep the script running
pythoncom.PumpMessages()







# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
def useSkill(keyCode):
    PressKey(keyCode)
    time.sleep(0.05)
    ReleaseKey(keyCode)
    time.sleep(0.05)


def calculateHPxy(percentage):
    x = 1.87 * percentage
    y = hpY
    if x > hpfirstHalfX and x < hpsecondHalfX:
        x = hpfirstHalfX
    flr = math.floor(x)
    return int(flr), y


def calculateMPxy(percentage):
    x = 1.87 * percentage
    y = mpY
    if x > hpfirstHalfX and x < hpsecondHalfX:
        x = hpfirstHalfX
    flr = math.floor(x)
    return int(flr), y


def checkMana(keyCode):
    x, y = calculateMPxy(80)
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    if b < 50:
        time.sleep(0.3)
        useSkill(keyCode)


def checkHealth(keyCode):
    x, y = calculateHPxy(80)
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    r, g, b = rgbint2rgbtuple(color)
    if r < 50:
        time.sleep(0.3)
        useSkill(keyCode)


def useTS(keyCode):
    time.sleep(0.5)
    useSkill(KEY_5)
    time.sleep(0.5)
    for x in range(0, 5):
        useSkill(ARROW_DOWN)
        time.sleep(0.1)
    useSkill(KEY_TAB)
    time.sleep(0.2)
    useSkill(ARROW_DOWN)
    time.sleep(0.2)
    useSkill(KEY_ENTER)
    useSkill(KEY_ENTER)
    threading.Timer(3600, useTS, (KEY_5,)).start()


def printer(keyCode):
    print("time", time.time(), keyCode)
    threading.Timer(5, printer, (KEY_0,)).start()


def useFlash(keyCode):
    for x in range(0, 10):
        useSkill(keyCode)
        time.sleep(0.1)
    threading.Timer(900, useFlash, (keyCode,)).start()


def provok():
    useSkill(KEY_5)
    click(675, 434)
    time.sleep(2)


def mage():
    useSkill(KEY_9)
    useSkill(KEY_3)
    click(675, 434)
    time.sleep(5)
    useSkill(KEY_4)
    click(659, 280)
    time.sleep(5)
    useSkill(KEY_5)
    click(659, 280)
    time.sleep(5)
    useSkill(KEY_6)
    click(659, 280)
    time.sleep(5)


def Z2():
    mage()




def image_compare(image_1, image_2):
    arr1 = np.array(image_1)
    arr2 = np.array(image_2)
    if arr1.shape != arr2.shape:
        return False
    maxdiff = np.max(np.abs(arr1 - arr2))
    return maxdiff


def pil_frombytes(im):
    """ Efficient Pillow version. """
    return Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX').tobytes()


global knightOnlineTitle
knightOnlineTitle = "Rise Online Client"
global anyOtpTitle
anyOtpTitle = "AnyOTP"



MAGE_WAIT_TRIGGERED = False



def OnKeyboardEvent(event):
    # if event.WindowName != "Rise Online Client":
    #     return True
    # print 'MessageName:', event.MessageName
    # print 'Message:', event.Message
    # print 'WindowName:', event.WindowName
    # print 'KEY_ID:', event.KeyID
    ctrl_pressed = GetKeyState(HookConstants.VKeyToID('VK_CONTROL'))
    shift_pressed = GetKeyState(HookConstants.VKeyToID('VK_LSHIFT'))
    if ctrl_pressed > 0 and event.KeyID == 74 and event.Message == 257 :  # 74 is J
        MAGE_WAIT_TRIGGERED = True
        wait_for_mage_attack()
    return True


def screenOnClickListenThread():
    hm = pyHook.HookManager()
    # hm.SubscribeMouseAllButtonsDown(onclick)
    hm.SubscribeKeyAll(OnKeyboardEvent)
    # hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    # hm.UnhookMouse()
    hm.UnhookKeyboard()


def displaySelectionMenu():
    print("1. Asas\n2. Warrior\n3. Mage\n4. Forgotten\n5. Juraid")
    return input("Select program to run method: ")


def asasAttack():
    while True:
        if True:
            print("press z")
            useSkill(KEY_Z)
            useSkill(KEY_2)
            time.sleep(0.3)
            checkHealth(KEY_0)
            checkMana(KEY_9)
        else:
            time.sleep(2)


def warriorAttack():
    while True:
        if isWindowKnightOnline():
            useSkill(KEY_Z)
            useSkill(KEY_3)
            time.sleep(0.2)
            useSkill(KEY_9)
            checkHealth(KEY_6)
            checkMana(KEY_0)
        else:
            time.sleep(2)


def mageAttack():
    while True:
        if isWindowKnightOnline():
            useSkill(KEY_Z)
            useSkill(KEY_1)
            time.sleep(0.3)
            useSkill(KEY_Z)
            useSkill(KEY_2)
            time.sleep(0.3)
            useSkill(KEY_Z)
            useSkill(KEY_3)
            time.sleep(0.3)
            useSkill(KEY_Z)
            useSkill(KEY_4)
            time.sleep(0.3)
            useSkill(KEY_Z)
            useSkill(KEY_6)
            time.sleep(0.3)
            useSkill(KEY_Z)
            useSkill(KEY_7)
            time.sleep(0.3)
            checkHealth(KEY_5)
            checkMana(KEY_0)
        else:
            time.sleep(2)


def isWindowKnightOnline():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Rise Online Client"


def ftClick():
    print("Record click x,y")
    time.sleep(5)
    x, y = win32api.GetCursorPos()
    print("Record color x,y")
    time.sleep(5)
    checkX, checkY = win32api.GetCursorPos()

    print("Record 2nd color x,y")
    time.sleep(5)
    checkX2, checkY2 = win32api.GetCursorPos()
    print("starting in 5...")
    time.sleep(5)

    print(x)
    print(y)
    x2 = 1083
    y2 = 587
    commandListenerThread = threading.Thread(target=screenOnClickListenThread)
    commandListenerThread.daemon = True
    commandListenerThread.start()

    forgottenX = 1073
    forgottenY = 587

    confirmX = 1071
    confirmY = 587

    while True:
        activeWindow = win32gui.GetDC(win32gui.GetActiveWindow())
        print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Rise Online Client":
            # color = win32gui.GetPixel(activeWindow, x, y)
            # r, g, b = rgbint2rgbtuple(color)
            greenCounter = 0
            for index in range(6):
                color = win32gui.GetPixel(activeWindow, checkX + index, checkY)
                g = (color >> 8) & 255
                if g > 100:
                    greenCounter = greenCounter + 1

            for index in range(6):
                color = win32gui.GetPixel(activeWindow, checkX2 + index, checkY2)
                g = (color >> 8) & 255
                if g > 100:
                    greenCounter = greenCounter + 1

            print("GreenCounter: ", greenCounter)
            if greenCounter > 4:
                print("CLICK")
                click(x, y)
                rightClick(x, y)
            else:
                print("RIGHT")
                useSkill(KEY_B)
                time.sleep(0.05)
                rightClick(x, y)
        else:
            time.sleep(2)


def jrClick():
    useSkill(KEY_Z)


def getScreenShot(x1, y1, x2, y2, filename):
    w = x2 - x1
    h = y2 - y1
    hwnd = win32gui.GetActiveWindow()
    hwnd = win32gui.FindWindow(None, "Rise Online Client")
    # hwnd = win32gui.FindWindow(None, anyOtpTitle)
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (x1, y1), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, filename + ".png")
    # Data version of png file
    # signedIntsArray = dataBitMap.GetBitmapBits(True)
    # img = np.fromstring(signedIntsArray, dtype='uint8')
    # cv2.imshow(img)
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


global pmHeight
global pmGapHeight
pmHeight = 20  # in px
pmGapHeight = 14  # in px

global distanceToSecondPm
distanceToSecondPm = 34  # in px

global hpPercentage
global mpPercentage

global yDistanceFor1stPm
yDistanceFor1stPm = 294

global xDistanceFor1stPm
xDistanceFor1stPm = 110

global pmIdWidth
pmIdWidth = 125

global pmIdHeight
pmIdHeight = 15


def onPmArrived(object):
    print(object)


def get_string_from_image(image_path):
    # Simple image to string
    # img = cv2.imread('mobName.png')
    # img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #
    # # Apply dilation and erosion to remove some noise
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)
    # img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # img = cv2.medianBlur(img, 3)
    # cv2.imwrite('processedMobName.png', img)
    #
    # pimg = Image.open('processedMobName.png')
    # print(pytesseract.image_to_string(pimg))

    img = cv2.imread(image_path)
    originalImg = cv2.resize(img, None, fx=5.5, fy=5.5)
    img = cv2.cvtColor(originalImg, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    cv2.imwrite('processed.png', img)

    pimg = Image.open('processed.png')
    text = pytesseract.image_to_string(pimg)
    print(text)
    return text


from uuid import getnode as get_mac

print("Knight Online must be running in full screen")
SCREEN_WIDTH = win32api.GetSystemMetrics(0)
SCREEN_HEIGHT = win32api.GetSystemMetrics(1)

chatx1 = 201
chaty1 = 959
chatx2 = 801
chaty2 = 979

pmClickX = 242
pmClickY = 795

pmColorX = 250
pmColorY = 786

pmSSX = 105
pmSSY = 785
pmSSX2 = 229
pmSSY2 = 803

chatSSX = 108
chatSSY = 787
chatSSX2 = 334
chatSSY2 = 910

clickBoxImageX = 234
clickBoxImageY = 754
clickBoxImageX2 = 251
clickBoxImageY2 = 769

dropDownNoticeX = 1105
dropDownNoticeY = 26

noticeRGB = 40, 44, 36
KEY_V = 0x2F


def rgbint2rgbtuple(RGBint):
    red = RGBint & 255
    green = (RGBint >> 8) & 255
    blue = (RGBint >> 16) & 255
    return (red, green, blue)




FT_MAP_FOLDER = "C:/Users/CagdasSensgreen/PycharmProjects/MacroFull/defpack/ftmap"


def onMobFound():
    print("MOB FOUND")


class MobFounder():
    def __init__(self, mobFoundListener):
        self.mobFoundListener = mobFoundListener

    def mobFound(self):
        self.mobFoundListener()


FT_MAP_X1 = 54
FT_MAP_Y1 = 130
FT_MAP_X2 = 168
FT_MAP_Y2 = 255

REFColorOffsets = [0,10,12,16,20]
import threading
import win32api
import win32gui
import time


class MouseColorListener:
    t1 = None
    STOP_THREAD = True

    def startStream(self):
        self.STOP_THREAD = False
        self.t1 = threading.Thread(target=self.colorPrinter)
        self.t1.daemon = True
        self.t1.start()

    def stopStream(self):
        self.STOP_THREAD = True
        self.t1.join()

    def colorPrinter(self):
        time.sleep(2)
        while True and self.STOP_THREAD is False:
            hwnd = win32gui.GetActiveWindow()
            activeWindow = win32gui.GetDC(hwnd)
            x, y = win32api.GetCursorPos()
            color = win32gui.GetPixel(activeWindow, x, y)
            r, g, b = self.rgbint2rgbtuple(color)
            state = "[X: {}, Y: {}] -> Color: {} -> RGB : ({}, {}, {})".format(x, y, color, r, g, b)
            print(state)
            time.sleep(0.1)
            win32gui.ReleaseDC(hwnd, activeWindow)


    def rgbint2rgbtuple(self, RGBint):
        red = RGBint & 255
        green = (RGBint >> 8) & 255
        blue = (RGBint >> 16) & 255
        return (red, green, blue)


def pressForAWhile(keyCode, startTime):
    if datetime.datetime.utcnow() >= startTime:
        return
    while True:
        now = datetime.datetime.utcnow()
        if now >= startTime:
            useSkill(keyCode)
            return

def releaseForAWhile(keyCode):
    pass


def main():
    hpPercentage = int(input("Enter HP percentage %[ x<52 & x>79 ]: "))
    mpPercentage = int(input("Enter MP percentage %[ x<52 & x>79 ]: "))
    if hpPercentage > 52 and hpPercentage < 79:
        hpPercentage = 52
    if mpPercentage > 52 and mpPercentage < 79:
        mpPercentage = 52
    if hpPercentage > 100:
        hpPercentage = 99
    if mpPercentage > 100:
        mpPercentage = 99
    if hpPercentage < 1:
        hpPercentage = 2
    if mpPercentage < 1:
        mpPercentage = 2

    selection = int(displaySelectionMenu())
    print("Switch to knight online for k0zp to start")
    if selection == 1:
        asasAttack()
    elif selection == 2:
        warriorAttack()
    elif selection == 3:
        mageAttack()
    elif selection == 4:
        ftClick()
    elif selection == 5:
        jrClick()
    else:
        print("Wrong input")
    input("Enter a key to exit: ")

    # Bu neydi acaba amk
    while(True):
        useSkill(KEY_2)
        time.sleep(0.122222)
    exit(0)
    # koxper öldürtmece22222
    for i in range (0, 10):
        click(750, 750)
        time.sleep(0.1)
        click(750,750)
        time.sleep(0.5)
    exit(0)
    # ZELDAKE
    time.sleep(5)
    for i in range(0,10000):
        if i % 100 == 0:
            print ("Adjusting lateral position")
            PressKey(KEY_D)
            time.sleep(0.22)
            ReleaseKey(KEY_D)
            time.sleep(0.15)
            useSkill(KEY_W)
            time.sleep(0.1)
        PressKey(KEY_W)
        time.sleep(0.066)
        useSkill(KEY_NUMPAD8)
        useSkill(KEY_NUMPAD8)
        useSkill(KEY_NUMPAD8)
        ReleaseKey(KEY_W)
        time.sleep(0.25)
        useSkill(KEY_NUMPAD9)

        # PressKey(KEY_Q)
        # time.sleep(0.16)
        # useSkill(KEY_NUMPAD8)
        # useSkill(KEY_NUMPAD6)
        # time.sleep(0.176)
        # useSkill(KEY_NUMPAD9)
        # ReleaseKey(KEY_Q)
        time.sleep(0.766)  # inventory screen

        useSkill(KEY_NUMPAD6)
        time.sleep(0.308) # let ui render
        useSkill(KEY_S)
        time.sleep(0.11) # let ui render
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)

        time.sleep(0.4)  # holding items now9

        startTime = datetime.datetime.utcnow() + datetime.timedelta(seconds=0.6)
        t1 = threading.Thread(target=pressForAWhile, args=(KEY_NUMPAD4, startTime, ))
        t2 = threading.Thread(target=pressForAWhile, args=(KEY_NUMPAD2, startTime, ))
        t1.daemon = True
        t2.daemon = True
        t1.start()
        t2.start()

        t1.join()
        t2.join()
        #4224
        # PressKey(KEY_NUMPAD2)
        # PressKey(KEY_NUMPAD4)
        # time.sleep(0.05)
        # PressKey(KEY_NUMPAD4)
        # ReleaseKey(KEY_NUMPAD2)


        time.sleep(1.25)  # duplication done by sorting and closing

        for skIndex in range(0, 3):
            PressKey(KEY_W)
            useSkill(KEY_NUMPAD6)
            time.sleep(0.01)
            ReleaseKey(KEY_W)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_S)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)
        useSkill(KEY_NUMPAD6)

        for skIndex in range(0,6):
            PressKey(KEY_S)
            useSkill(KEY_NUMPAD6)
            time.sleep(0.082524)
            ReleaseKey(KEY_S)

        time.sleep(0.1)
        PressKey(KEY_W)
        time.sleep(0.07)
        ReleaseKey(KEY_W)
        time.sleep(0.7)  # collected everything
    exit(1);
    # time.sleep(3)
    # x, y = win32api.GetCursorPos()
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    # time.sleep(0.01)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    # exit(0)
    # threading.Thread(target=screenOnClickListenThread).start()
    # finder = MobFounder(onMobFound)
    # finder.mobFound()
    # exit(0)
    # getScreenShot(0, 0, 100, 1000, "100xscreensht")
    # exit(0)
    # print("sa")
    #
    # while True:
    #     screenWidth = win32api.GetSystemMetrics(0)
    #     screenHeight = win32api.GetSystemMetrics(1)
    #     FT_HP_REF_X = screenWidth / 2 - 50
    #     FT_HP_REF_Y = 45
    #     for offset in REFColorOffsets:
    #         hwnd = win32gui.FindWindow(None, "Rise Online Client")
    #         activeWindow = win32gui.GetDC(hwnd)
    #         color = win32gui.GetPixel(activeWindow, FT_HP_REF_X + offset, FT_HP_REF_Y)
    #         r, g, b = rgbint2rgbtuple(color)
    #         state = "[X: {}, Y: {}] -> Color: {} -> RGB : ({}, {}, {})".format(FT_HP_REF_X, FT_HP_REF_Y, color, r, g, b)
    #         print(state)
    #     time.sleep(2)
    #     print("------------------------------------------------------------")
    #     win32gui.ReleaseDC(hwnd, activeWindow)
    #
    #
    # exit(0)11
    #LOL REGION#
    # timeNow = datetime.datetime.utcnow()
    # stopTime = timeNow + datetime.timedelta(seconds=13)
    # clickedFlag = False
    # while True:
    #     (firstParam, cursorInfo, (moeX,moeY)) = win32gui.GetCursorInfo()
    #     if cursorInfo == 65541 and clickedFlag is False:
    #         clickedFlag = True
    #         print("Cursor is active")
    #         for i in range(10):
    #             click(606, 775)
    #             PressKey(IOWriter.KEY_LCONTROL)
    #             PressKey(IOWriter.KEY_V)
    #             ReleaseKey(IOWriter.KEY_LCONTROL)
    #             ReleaseKey(IOWriter.KEY_V)
    #             PressKey(IOWriter.KEY_RETURN)
    #             ReleaseKey(IOWriter.KEY_RETURN)
    #         exit(0)
    #
    #     else:
    #         click(606, 775)
    #         print("Cursor is disabled")
    #         PressKey(IOWriter.KEY_LCONTROL)
    #         PressKey(IOWriter.KEY_V)
    #         ReleaseKey(IOWriter.KEY_LCONTROL)
    #         ReleaseKey(IOWriter.KEY_V)
    #         PressKey(IOWriter.KEY_RETURN)
    #         ReleaseKey(IOWriter.KEY_RETURN)
    #
    #     click(606, 775)
    #     PressKey(IOWriter.KEY_LCONTROL)
    #     PressKey(IOWriter.KEY_V)
    #     ReleaseKey(IOWriter.KEY_LCONTROL)
    #     ReleaseKey(IOWriter.KEY_V)
    #     PressKey(IOWriter.KEY_RETURN)
    #     ReleaseKey(IOWriter.KEY_RETURN)
    #     now = datetime.datetime.utcnow()
    #     if now > stopTime:
    #         exit(0)
    #
    # print("hello")
    time.sleep(2)

    # PressKey(KEY_W)
    # while True:
    #     useSkill(IOWriter.KEY_SPACE)
    #     time.sleep(50)
    # exit(0)
    #LOL REGION END#
    # ms = MouseColorListener() # 606 775
    # ms.startStream()

    # kekX, kekY = win32api.GetCursorPos()
    # while True:
    #     click(kekX, kekY)
    # exit(input("enter to exit"))
    # # first red dots appear in file_3871.png
    # for i in range(3870, 3900):  # loop to read one image at a time
    #     imgpath = os.path.join(FT_MAP_FOLDER, "{}/file_{}.png".format(FT_MAP_FOLDER, i))
    #
    #     im = Image.open(imgpath)
    #     pixels = list(im.getdata())
    #     frame = cv2.imread(imgpath, 1)
    #     print("Displaying image {}".format(imgpath))
    #     cv2.imshow('Window', frame)
    #
    #     img = cv2.imread(imgpath)
    #     lower_red = np.array([-1, -1, 127])
    #     upper_red = np.array([1, 1, 129])
    #     mask0 = cv2.inRange(img, lower_red, upper_red)
    #     # cv2.imshow("Mask0", mask0)
    #     # height, width, channels = img.shape
    #     # blank_image = np.zeros((height, width, channels), np.uint8)
    #     # resultImage = cv2.bitwise_and(blank_image, mask0)
    #     # cv2.imwrite("MASK0_file_{}.png".format(i), resultImage)
    #     # mask0 = cv2.imread("MASK0_file_{}.png".format(i))
    #     nonBlackCount = 0
    #     for pixel in mask0:
    #         if all(i < 1 for i in pixel):
    #             pass  # all values are black
    #         else:
    #             nonBlackCount = nonBlackCount + 1
    #     if nonBlackCount > 20:
    #         print("White pixel found in: file_{}.png ! COUNT : {}".format(i, nonBlackCount))
    #
    # input("enter")
    # exit(0)
    # # for i in range(0, 5000):
    # #     getScreenShot(54,130,168,255,"file_{}".format(i))


    x = 1799
    y = 258

    # for y in range(257,1080):
    #     color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
    #     r, g, b = rgbint2rgbtuple(color)
    #     print("y: {} -> r: {} g: {} b: {}".format(y,r,g,b))
    asasAttack()
    #ms = MouseColorListener()
    #ms.startStream()
    exit(input("exit: "))
    # input("lel")
    # autoLoot = AutoLoot()
    # while True:
    #     hwnd = win32gui.GetActiveWindow()
    #     activeWindow = win32gui.GetDC(hwnd)
    #     x, y = win32api.GetCursorPos()
    #     autoLoot.checkForLoots(x,y)
    # exit(0)
    # input("Ener")
    # recorder = ScreenRecorder()
    # recorder.startRecord("filename")
    # exit(0)
    # pmHandler = NewPMListener(pmColorX, pmColorY, pmClickX, pmColorY)
    # pmHandler.startStream()
    # # noticeListener = NoticeListener()
    # # noticeListener.startStream()
    # exit(0)
    pmHandler = NewPMListener(pmColorX, pmColorY, pmClickX, pmClickY)
    pmHandler.startStream()
    input("eben")
    #
    # getScreenShot(clickBoxImageX, clickBoxImageY -(distanceToSecondPm*2), clickBoxImageX2, clickBoxImageY2-(distanceToSecondPm*2), "clickBoxImage3")
    # imageComparator = ImageComparator("clickBoxImage.png","clickBoxImage3.png", True)
    # imageComparator.compare_images()
    # screenReader = ScreenChatFeeder(chatx1, chaty1, chatx2, chaty2, "generalChat")
    # screenReader.startStream()
    # while True:
    #     getScreenShot(863,7,1044,30,"activeMobName")
    #     get_string_from_image("activeMobName.png")
    # print (get_mac())
    # listener = MouseColorListener()
    # listener.startStream()
    #
    # listener.startStream()
    # loggedChar = KChar()
    #
    # raw_input("exit")
    #
    # #ioWriter = IOWriter()
    # #ioWriter.writeText("makina napiyosun\r")
    # pmHandler.startStream()
    # pmHandler.startStream()
    # pmHandler.getPmScreenShot(1)
    # exit(1)
    # x = -1619
    # y = 358
    #
    # # for i in range(y, y+150):
    # #     hwnd = win32gui.GetActiveWindow()
    # #     activeWindow = win32gui.GetDC(hwnd)
    # #     color = win32gui.GetPixel(activeWindow, x,i)
    # #     r, g, b = rgbint2rgbtuple(color)
    # #     print(x, i)
    # #     print(r, g, b)
    # #     time.sleep(0.1)
    # #
    # # exit(0)
    # hwnd = win32gui.FindWindow(None, "Rise Online Client")
    # rect = win32gui.GetWindowRect(hwnd)
    # x = rect[0]
    # y = rect[1]
    # w = rect[2] - x
    # h = rect[3] - y
    # print("Ko is running on settings: ", x, y, w, h)
    # ssX, ssY, ssW, ssH = 0 + xDistanceFor1stPm, h - yDistanceFor1stPm, 0 + xDistanceFor1stPm + pmIdWidth, h - yDistanceFor1stPm + pmIdHeight
    # print("ScreenShot settings: ", ssX, ssY, ssW, ssH)
    # filename = "_KO_x" + str(ssX) + "_y" + str(ssY) + "_w" + str(ssW) + "_h" + str(ssH)
    # #getScreenShot(ssX, ssY, ssW, ssH, "pm")
    # im = cv2.imread('pm.png')
    # im[np.where((im < [60, 60, 60]).all(axis=2))] = [0, 0, 255]
    # cv2.imwrite('output.png', im)
    # print(pytesseract.image_to_string(Image.open('output.png')))
    # print(pytesseract.image_to_string(Image.open('chatbox.png')))
    # while True:
    #     hwnd = win32gui.FindWindow(None, "Rise Online Client")
    #     hwnd = win32gui.GetActiveWindow()
    #     activeWindow = win32gui.GetDC(hwnd)
    #     # print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    #     if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Rise Online Client" or 1:
    #         x, y = win32api.GetCursorPos()
    #         color = win32gui.GetPixel(activeWindow, x, y)
    #         r, g, b = rgbint2rgbtuple(color)
    #         print(x, y)
    #         print(r, g, b)
    #         time.sleep(0.1)

    hpPercentage = input("Enter HP percentage %[ x<52 & x>79 ]: ")
    mpPercentage = input("Enter MP percentage %[ x<52 & x>79 ]: ")
    if hpPercentage > 52 and hpPercentage < 79:
        hpPercentage = 52
    if mpPercentage > 52 and mpPercentage < 79:
        mpPercentage = 52
    if hpPercentage > 100:
        hpPercentage = 99
    if mpPercentage > 100:
        mpPercentage = 99
    if hpPercentage < 1:
        hpPercentage = 2
    if mpPercentage < 1:
        mpPercentage = 2

    selection = displaySelectionMenu()
    print("Switch to knight online for k0zp to start")
    if selection == 1:
        asasAttack()
    elif selection == 2:
        warriorAttack()
    elif selection == 3:
        mageAttack()
    elif selection == 4:
        ftClick()
    elif selection == 5:
        jrClick()
    else:
        print("Wrong input")
    input("Enter a key to exit: ")


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(10)
        else:
            break
