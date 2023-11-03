# import macro_config as mc
from config import macro_config as mc
import cv2
import numpy as np
import pyautogui
import time
import threading
import random
import keyboard
import os
import webbrowser
import datetime


SEARCH_REGION = mc.SEARCH_REGION  # 좌석 선택 영역
REFRESH_REGION = mc.REFRESH_REGION  # 좌석 새로고침하는 버튼 영역
CLICK_DESTINATION = mc.CLICK_DESTINATION  # 다음단계 버튼 좌표
CLICK_TICKET = mc.CLICK_TICKET  # 티켓 버튼 좌표
CHROME_PATH = "open -a /Applications/Google\ Chrome.app %s"


RECAPTCHA_REGION = (711, 205, 1844-711, 1074-205)  # 리캡챠 감지 영역
CLICK_GROUP = (1245,830) #타겟 그룹 좌표


def find_color_on_screen(color, region=None, tolerance=10):
    screen = pyautogui.screenshot('my_screenshot.png',region=region)
    screen_np = np.array(screen.convert('RGB'))
    lower_bound = np.array([color[0] - tolerance, color[1] - tolerance, color[2] - tolerance])
    upper_bound = np.array([color[0] + tolerance, color[1] + tolerance, color[2] + tolerance])
    mask = cv2.inRange(screen_np, lower_bound, upper_bound)
    result = cv2.findNonZero(mask)

    if result is not None:
        # return np.mean(result, axis=0)[0]
        return np.array(result[1][0])
    else:
        return None
    
def thread_SearchColor(stop_event):
    while not stop_event.is_set():
        target_color = mc.TARGET_COLOR
        print("매크로 실행 중...(q키를 꾹 눌러 종료)",  end="\r")
        time.sleep(1)
        color_position = find_color_on_screen(target_color, region=SEARCH_REGION)
        if color_position is not None:
            stop_event.set()
            pyautogui.moveTo(SEARCH_REGION[0] + color_position[0], SEARCH_REGION[1] + color_position[1]+1)
            pyautogui.click()
            # 2자리 맞추기
            # pyautogui.moveTo(SEARCH_REGION[0] + color_position[0] + 10, SEARCH_REGION[1] + color_position[1]+1)
            # pyautogui.click()
            ############
            # 예매 완료 버튼 클릭
            # pyautogui.moveTo(*CLICK_DESTINATION)
            # pyautogui.click()
        time.sleep(0.001)

def thread_Refresh(stop_event, region):
    while not stop_event.is_set() and not keyboard.is_pressed('q'):
        random_x = random.randint(region[0], region[0] + region[2])
        random_y = random.randint(region[1], region[1] + region[3])
        random_interval = random.uniform(0.500, 0.600)
        pyautogui.moveTo(random_x, random_y)
        pyautogui.click()
        time.sleep(random_interval)
    stop_event.set()

def main():
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(CHROME_PATH))
    stop_event = threading.Event()
    while True:
        pause_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"\n[{pause_time}]매크로가 중지된 상태입니다.\n매크로를 시작하려면 'r'를, 예매 홈페이지에 접속하려면 'e'를 입력하세요. 종료하려면 다른 키워드를 입력하세요.")
        user_input = input()
        print("\n\n\n\n\n")
        if user_input.lower() == 'e':
            webbrowser.get("chrome").open_new_tab(mc.RESERVATION_URL)
            time.sleep(1)
            webbrowser.open(mc.RESERVATION_URL)
            continue
        elif user_input.lower() != 'r' :
            break
        start_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{start_time}] 매크로가 실행되었습니다.")
        
        # 여기부터는 마우스 움직이는 알고리즘 계산하기
        # 좌석 그룹 선택
        # pyautogui.moveTo(*CLICK_TICKET)
        # pyautogui.click()
        #1루 내야일반석 선택
        # pyautogui.scroll(-10)
        # pyautogui.moveTo(CLICK_TICKET[0],CLICK_TICKET[1]+20)
        ################
        # pyautogui.click()
        # 다음 단계 버튼 클릭
        pyautogui.moveTo(*CLICK_DESTINATION)
        pyautogui.click()
        
        ##################################
        ####좌석 클릭후 좌석선택완료 버튼 누르고 나면 이선좌통과####
        stop_event = threading.Event()
        search_thread = threading.Thread(target=thread_SearchColor, args=(stop_event,))
        refresh_thread = threading.Thread(target=thread_Refresh, args=(stop_event, REFRESH_REGION))
        search_thread.start()
        # refresh_thread.start()
        search_thread.join()
        # refresh_thread.join()

    terminate_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{terminate_time}]프로그램이 종료됩니다.")



if __name__ == "__main__":
    main()



# 알고리즘
# 1. 좌석그룹을 누른다
# 2. 좌석선택을 누른다
# 3. 좌석을 연달아 두개를 누른다 (테이블석은 한번만 누르면됨, 일반석은 두개 눌러야됨)
# 4. 좌석선택완료를 누른다 (여기서 넘어가면 이선좌는 통과)
# 5. 이선좌가 뜨면 확인 버튼을 누른다 (새로고침이 알아서 됨)
# 6. 3번 ~ 5번 반복한다


#https://puzizig.com/posts/368/