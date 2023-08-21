from mss import mss
import cv2
from PIL import Image
import numpy as np
import pyautogui

mon = {'top': 188, 'left':337, 'width':1280, 'height':720}

sct = mss()

# Mouse coordinates: 1126, 693


while 1:
    mouse_x, mouse_y = pyautogui.position()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('test', np.array(img_bgr))
    print(f'Mouse: ({mouse_x}, {mouse_y})')
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break