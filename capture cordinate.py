import pyautogui
import time

# Wait for 5 seconds
time.sleep(5)

# Get the current mouse position
x, y = pyautogui.position()

# Print the coordinates
print(f"Mouse pointer is at: ({x}, {y})")
