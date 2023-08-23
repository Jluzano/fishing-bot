import keyboard
import mss
import time

# Color values for arrow keys
ARROW_COLORS = {
    (245, 197, 67): "LEFT",
    (52, 145, 247): "DOWN",
    (226, 50, 50): "UP",
    (45, 236, 43): "RIGHT",
    (174, 49, 209): "SPACE"
}

def main():
    with mss.mss() as sct:
        monitor_number = 1
        mon = sct.monitors[monitor_number]

        x = 55
        y = 47

        monitor = {
            "top": mon["top"] + 665,
            "left": mon["left"] + 1073,
            "width": 1280,
            "height": 720,
            "mon": monitor_number,
        }

        start_time = time.time()
        fps_counter = 0

        while True:
            sct_img = sct.grab(monitor)
            pixel_color = sct_img.pixel(x, y)

            arrow_key = ARROW_COLORS.get(pixel_color, "NONE")
            print(arrow_key)

            if keyboard.is_pressed('q'):
                break
            
            fps_counter += 1
            if time.time() - start_time >= 1:
                print("FPS:", fps_counter)
                start_time = time.time()
                fps_counter = 0

if __name__ == "__main__":
    main()
