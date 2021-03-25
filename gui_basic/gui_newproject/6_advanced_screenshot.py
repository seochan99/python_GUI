import time
import keyboard
from PIL import ImageGrab


def screenshot():
    #2021 ~ 
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9",screenshot)

keyboard.wait("esc") #사용자가esc 누를 때 가지 

#안된당 ㅋㅋ 
