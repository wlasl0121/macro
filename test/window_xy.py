import math
# import pyautogui
import time
import macmouse

def get_window_range() :

    while True :
        if macmouse.is_pressed("left") :
            x, y = macmouse.get_position()
            print(f"\n\nSEARCH_REGION_x = {math.trunc(x)}\nSEARCH_REGION_y = {math.trunc(y)}\n", end="\r")
        
        time.sleep(0.1)
    
    
    

def main() :
    print("필요한 위치를 클릭해주세요.")

    get_window_range()


if __name__ == "__main__" :
    main()