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
                        13: KEY_RETURN,
                        72: KEY_H,
                        85: KEY_U,
                        73: KEY_I,
                        27: KEY_ESCAPE,
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
                        66: KEY_B,
                        67: KEY_C,
                        68: KEY_D,
                        69: KEY_E,
                        70: KEY_F,
                        71: KEY_G,
                        72: KEY_H,
                        73: KEY_I,
                        74: KEY_J,
                        75: KEY_K,
                        76: KEY_L,
                        77: KEY_M,
                        78: KEY_N,
                        79: KEY_O,
                        80: KEY_P,
                        81: KEY_Q,
                        82: KEY_R,
                        83: KEY_S,
                        84: KEY_T,
                        85: KEY_U,
                        86: KEY_V,
                        87: KEY_W,
                        88: KEY_X,
                        89: KEY_Y,
                        90: KEY_Z,
                        32: KEY_SPACE
                        }

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


# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html


def useSkill(keyCode):
    PressKey(keyCode)
    time.sleep(0.05)
    ReleaseKey(keyCode)
    time.sleep(0.05)

class IOWriter:
    def writeText(self, text):
        for letter in text.upper():
            print(ord(letter))
            keyCode = ord(letter)
            KEY = KEYBOARD_DIRECTX_MAP.get(keyCode)
            if KEY is not None:
                useSkill(KEY)

    def useSkill(self, keyCode):
        PressKey(keyCode)
        time.sleep(0.05)
        ReleaseKey(keyCode)
        time.sleep(0.05)

    def click(self, x, y):
        win32api.SetCursorPos((x, y))
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.3)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)