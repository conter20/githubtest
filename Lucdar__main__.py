import sys
import PyQt5
from PyQt5.QtWidgets import *
from Lucdar__def__ import MyApp
# from Lucdar__background__ import detect_key
import atexit
import win32com.client, time
from pynput.keyboard import Listener, Key



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

aseUrl = 'https://dict.naver.com/search.dict?dicQuery={}&query={}&target=dic&ie=utf8&query_utf=&isOnlyViewEE='