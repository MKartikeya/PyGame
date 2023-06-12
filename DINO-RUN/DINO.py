import pyautogui
from PIL import ImageGrab,Image
import time
from numpy import asarray
def hit(key):
    pyautogui.keyDown(key)


def takescreensshot():
    image=ImageGrab.grab().convert('L')
    return image

def iscollide(data):
    for i in range(470,480):
             for j in range(600,660):
                if  data[i, j] < 100:
                    return True
    return False


if __name__== '__main__':
    time.sleep(3)
    while True:
        image=takescreensshot()   
        data=image.load()
        if iscollide(data):
            hit("up")
    # print(asarray(image))
        for i in range(470,480):
             for j in range(600,660):
                  data[i, j] = 0
        # break
    # image.show()

    