@echo off

echo Installing required Python packages...
py -m pip install --upgrade pip
py -m pip install pyautogui
py -m pip install pynput

echo Installation complete!
pause