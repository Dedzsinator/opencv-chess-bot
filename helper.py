import pyautogui
import time

try:
    while True:
        # Get and print the current mouse coordinates
        mouse_x, mouse_y = pyautogui.position()
        print(f"Mouse coordinates: x={mouse_x}, y={mouse_y}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")
