from pynput.keyboard import Controller as KeyboardController, Key, Listener
from pynput.mouse import Controller as MouseController, Button
import time
import threading

# Initialize controllers
keyboard = KeyboardController()
mouse = MouseController()

# Ensure user is ready
print("Starting in 5 seconds.")
time.sleep(5)

# Helper to press keys
def press_key(key, duration=0.1):
    keyboard.press(key)
    time.sleep(duration)
    keyboard.release(key)

# Helper to move mouse and click
def click_at(x, y, button=Button.left):
    mouse.position = (x, y)
    time.sleep(0.1)
    mouse.click(button)

# Function to eat a golden apple
def eat_gapple():
    print("Eating golden apple...")
    press_key('6')  # Assuming golden apple is in hotbar slot 6
    time.sleep(0.2)
    mouse.press(Button.right)  # Start eating
    time.sleep(1.8)  # Adjust duration based on Minecraft eating animation
    mouse.release(Button.right)
    print("Golden apple eaten!")

# Main sequence
def minecraft_sequence():
    # Go to hotbar 9
    press_key('9')
    press_key('s', 0.2)

    # Place chest
    mouse.click(Button.right)
    time.sleep(0.3)

    # Open chest
    mouse.click(Button.right)
    time.sleep(0.5)

    # Move to "dump" button and click
    click_at(897, 349)

    # Close chest
    time.sleep(0.2)
    press_key('e', 0.3)

    # Walk forward
    press_key('w', 0.3)

    # Go to hotbar 8 and place Crystal
    press_key('8')
    time.sleep(0.2)
    mouse.click(Button.right)
    time.sleep(0.2)

    # Go to hotbar 7 and press 'n'
    press_key('7')
    time.sleep(0.7)
    press_key('n', 0.5)

# Flag to control the loop
running = True
sequence_count = 0  # Counter for sequence runs

# Keyboard listener callback to stop the loop
def on_press(key):
    global running
    if key == Key.esc:
        print("ESC pressed. Stopping script...")
        running = False
        return False  # Stop the listener

# Function to run the sequence
def run_sequence():
    global running, sequence_count

    while running:
        minecraft_sequence()
        sequence_count += 1  # Increment counter

        # Check if 5 sequences have been completed
        if sequence_count % 5 == 0:
            eat_gapple()  # Call eat_gapple()

        time.sleep(0.5)  # Delay before next sequence

# Start the keyboard listener in a separate thread
listener = Listener(on_press=on_press)
listener.start()

# Run the Minecraft sequence
run_sequence()

# Wait for the listener thread to finish
listener.join()
