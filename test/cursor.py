import pyautogui
import time
import macmouse

while True:
    x, y = pyautogui.position()
    print(f"현재 커서 좌표: ({x}, {y})   ", end="\r")
    time.sleep(0.1)


# while True : 
#     if macmouse.is_pressed("left"):
#         pos = macmouse.get_position()
#         print(pos)
#     time.sleep(0.1)