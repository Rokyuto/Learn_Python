from pynput import keyboard
import subprocess

HOTKEYS_COMBINATIONS = [
        { keyboard.Key.shift , keyboard.KeyCode(char='f') },
        { keyboard.Key.shift , keyboard.KeyCode(char='F') }
    ]

current = set()

# On Correct Hotkey Combination (Shift + f / Shift + F)
def macro():
    # Create GUI Program to Create File
    GUI_CreateFile = 'python FileCreatorMacro\\GUI_CreateFile.py'
    openGUI_CreateFile = subprocess.Popen(GUI_CreateFile)
    out, err = openGUI_CreateFile.communicate()

# On Keyboard Button Pressed
def on_press(key):
    if any([key in COMBO for COMBO in HOTKEYS_COMBINATIONS]):
        current.add(key)
        # If Combination is CORRECT, then call Macro Func
        if any(all(k in current for k in COMBO) for COMBO in HOTKEYS_COMBINATIONS):
            macro()

# On Keyboard Button Released Remove Listener and stop tracking events
def on_release(key):
    if any([key in COMBO for COMBO in HOTKEYS_COMBINATIONS]):
        current.remove(key)
     
# Listener for Keyboard Button Press
with keyboard.Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()