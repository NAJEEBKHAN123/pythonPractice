import pyautogui
import time
import pyperclip

# Give yourself 5 seconds to click WhatsApp window
print("You have 5 seconds to switch to WhatsApp...")
time.sleep(5)

start_x, start_y = 1176, 207
end_x, end_y = 1675, 916

pyautogui.moveTo(start_x, start_y, duration=0.5)
pyautogui.dragTo(end_x, end_y, duration=1, button='left')

pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

text = pyperclip.paste()
print("Copied text:", text)
