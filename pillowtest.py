import os
import time
from PIL import ImageGrab
from datetime import datetime

# Create a folder for saving screenshots
folder_name = "Screenshots"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Continuously take screenshots every 5 seconds
try:
    while True:
        # Capture the screenshot
        screenshot = ImageGrab.grab()

        # Generate a unique filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(folder_name, f"screenshot_{timestamp}.png")

        # Save the screenshot to the folder
        screenshot.save(file_path)

        # Close the screenshot to free up resources
        screenshot.close()

        # Wait for 5 seconds before taking the next screenshot
        time.sleep(5)

except KeyboardInterrupt:
    print("Screenshot capture stopped.")
