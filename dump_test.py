import psutil
import win32con
import win32gui
import win32security


def dump_process_info(pid, output_file):
    try:
        process = psutil.Process(pid)
        process_info = f"Process ID: {pid}\n"
        process_info += f"Name: {process.name()}\n"
        process_info += f"Status: {process.status()}\n"
        process_info += f"CPU Usage: {process.cpu_percent()}%\n"
        process_info += f"Memory Usage: {process.memory_info().rss / 1024 / 1024} MB\n"
        process_info += f"Command Line: {process.cmdline()}\n"

        with open(output_file, 'w') as file:
            file.write(process_info)

        print(f"Process information dumped successfully to '{output_file}'.")
    except psutil.NoSuchProcess:
        print(f"No process with PID {pid} exists.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")



import win32gui
import win32process

# Find the window handle (HWND) based on the window title
hwnd = win32gui.FindWindow(None, "Rise Online Client")
pid = None
if hwnd != 0:
    # Get the process ID (PID) associated with the window
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    print(f"Window HWND: {hwnd}")
    print(f"Process PID: {pid}")
else:
    print("Window not found.")
import win32process
import win32gui
import win32api
import ctypes
import win32process
import win32api
import win32con


if pid:
    import ctypes

    # Constants
    PROCESS_PID = pid  # Replace with the actual PID of the target process
    from ReadWriteMemory import ReadWriteMemory

    rwm = ReadWriteMemory()
    rwm = ReadWriteMemory()

    processes_ids = rwm.enumerate_processes()
    process = rwm.get_process_by_id(pid)
    print(process.__dict__)
