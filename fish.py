import cv2
import numpy as np
import mss
from PIL import Image
import keyboard

# Load symbol images you want to find
symbol_templates = {
    'symbol1': cv2.imread('arrowDown.png', cv2.IMREAD_GRAYSCALE),
    'symbol2': cv2.imread('arrowLeft.png', cv2.IMREAD_GRAYSCALE),
    'symbol3': cv2.imread('arrowRight.png', cv2.IMREAD_GRAYSCALE),
    'symbol4': cv2.imread('arrowUp.png', cv2.IMREAD_GRAYSCALE),
    'symbol5': cv2.imread('space.png', cv2.IMREAD_GRAYSCALE)
    # Add more symbols here...
}

def find_symbol(screen_img, template):
    # Convert the screen image to grayscale
    gray_screen = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Define a threshold for matching
    threshold = 0.8

    if max_val >= threshold:
        return max_loc  # Return the top-left corner of the matched region
    else:
        return None  # Symbol not found

def main():
    # Define the region of the screen to capture
    screen_capture_region = {'top': 500, 'left': 600, 'width': 400, 'height': 200}

    with mss.mss() as sct:
        cv2.namedWindow('Detected Symbols', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Detected Symbols', 1024, 768)  # Set the initial window size
        
        while True:
            # Capture the screen region
            screen_img = np.array(sct.grab(screen_capture_region))
            
            # Initialize dictionary to store symbol locations
            symbol_locations = {}

            # Find all symbols within the captured screen region
            for symbol_name, symbol_template in symbol_templates.items():
                symbol_location = find_symbol(screen_img, symbol_template)
                if symbol_location is not None:
                    symbol_locations[symbol_name] = symbol_location
                    if symbol_name == 'symbol1':
                        keyboard.press('s')
                        keyboard.release('s')
                    elif symbol_name == 'symbol2':
                        keyboard.press('a')
                        keyboard.release('a')
                    elif symbol_name == 'symbol3':
                        keyboard.press('d')
                        keyboard.release('d')
                    elif symbol_name == 'symbol4':
                        keyboard.press('w')
                        keyboard.release('w')
                    elif symbol_name == 'symbol5':
                        keyboard.press('space')
                        keyboard.release('space')

            # Display the captured screen region with rectangles around the detected symbols
            screen_img_with_overlay = screen_img.copy()
            for symbol_location in symbol_locations.values():
                h, w = symbol_template.shape
                cv2.rectangle(screen_img_with_overlay, symbol_location, (symbol_location[0] + w, symbol_location[1] + h), (0, 255, 0), 2)

            cv2.imshow('Detected Symbols', screen_img_with_overlay)
            
            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyWindow('Detected Symbols')

if __name__ == '__main__':
    main()