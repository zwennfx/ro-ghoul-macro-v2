import subprocess
import sys
import os
import fnmatch
import keyboard
import time
import threading
import base64
import tkinter as tk

def check_python_installed():
    try:
        subprocess.run(["python", "--version"], check=True, capture_output=True)
        return True
    except:
        return False

def install_python():
    for root, dir, files in os.walk("C:\\"):
        for file in files:
            if fnmatch.fnmatch(file, 'python*.*.exe'):
                file_path = os.path.join(root, file)
                subprocess.run([file_path, "/quiet", "/norestart"])
                sys.exit()

def check_module_installed(module_name):
    try:
        __import__(module_name)
        return True
    except:
        return False

def install_module(module_name):
    subprocess.run([sys.executable, "-m", "pip", "install", module_name])

def check_pip_installed():
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"], check=True, capture_output=True)
        return True
    except:
        return False

def install_pip():
    subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade", "--default-pip"])

def press_key():
    global macro_on, stop
    stop = False
    while macro_on:
        if keyboard.is_pressed('w'):
            keyboard.press('w')
            time.sleep(0.025)
            keyboard.release('w')
        elif keyboard.is_pressed('a'):
            keyboard.press('a')
            time.sleep(0.025)
            keyboard.release('a')
        elif keyboard.is_pressed('s'):
            keyboard.press('s')
            time.sleep(0.025)
            keyboard.release('s')
        elif keyboard.is_pressed('d'):
            keyboard.press('d')
            time.sleep(0.025)
            keyboard.release('d')
        if stop:
            break


def start_macro():
    global macro_on, press_key_thread, stop
    if not macro_on:
        macro_on = True
        stop = False
        start_button.config(state="disable")
        stop_button.config(state="normal")
        press_key_thread = threading.Thread(target=press_key)
        press_key_thread.start()


def stop_macro():
    global macro_on, stop
    if macro_on:
        stop = True
        macro_on = False
        start_button.config(state="normal")
        stop_button.config(state="disable")
        press_key_thread.join()

if check_python_installed() == False:
    install_python()
else:
    print("Python is already installed.")

keyboard.add_hotkey('f2', start_macro, args=())
keyboard.add_hotkey('f4', stop_macro, args=())
root = tk.Tk()
root.geometry("400x200")
root.title("Zwenn's Macro V2 [RG]")

macro_on = False
start_button = tk.start_button = tk.Button(root, text="Start Macro (F2)", command=start_macro)
start_button.pack()
stop_button = tk.Button(root, text="Stop Macro (F4)", state="disable", command=stop_macro)
stop_button.pack()

root.protocol("WM_DELETE_WINDOW", lambda : stop_macro() or root.destroy())
root.mainloop()