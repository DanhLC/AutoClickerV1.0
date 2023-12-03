import pyautogui
import threading
import keyboard

# Đặt thời gian trễ giữa các lần click thành 0.001 giây (1ms)
pyautogui.PAUSE = 0.001

def click():
    while True:
        if stop_clicking:
            break
        pyautogui.click()

def start_auto_click():
    global stop_clicking
    stop_clicking = False
    threading.Thread(target=click).start()

def stop_auto_click():
    global stop_clicking
    stop_clicking = True

keyboard.add_hotkey('f3', start_auto_click)
keyboard.add_hotkey('f4', stop_auto_click)

# Khởi tạo biến để dừng auto-click
stop_clicking = True

# Bắt đầu vòng lặp chính để duy trì việc chạy mã
while True:
    pass
