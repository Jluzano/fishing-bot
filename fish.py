import os.path
import keyboard
import mss
import mss.tools
import time
import pyautogui
import json
import os

with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # (1120, 710)
    x = 55
    y = 47

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 665,  # 100px from the top
        "left": mon["left"] + 1073,  # 100px from the left
        "width": 1280,
        "height": 720,
        "mon": monitor_number,
    }

    #print("Starting in 5...")
    #time.sleep(5)
    
    while True:
        start_time = time.time()
        sct_img = sct.grab(monitor)
        pixel_color = sct_img.pixel(x, y)  # Get the color value at (1120, 710)

        # Check if the RGB values match black (0, 0, 0)
        if pixel_color == (245, 197, 67): # Arrow left
            print("LEFT")
        elif pixel_color == (52, 145, 247): # Arrow down
            print("DOWN")
        elif pixel_color == (226, 50, 50): # Arrow down
            print("UP")
        elif pixel_color == (45, 236, 43): # Arrow down
            print("RIGHT")
        elif pixel_color == (174, 49, 209): # Arrow down
            print("SPACE")
        else:
            print("NONE")
        
        if keyboard.is_pressed('q'):
            break
        print("FPS: ", 1.0 / (time.time() - start_time))