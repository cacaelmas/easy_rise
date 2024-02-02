# Gets cursor pos and r,g,b color on that exact pixel
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
