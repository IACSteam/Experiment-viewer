from enum import Enum

class keys(Enum):
    Escape = 27

class k_b_cls():
    def __init__(self):
        self.__parent = self.root

        self.bind_keyboard()

    # Клавиша зажата
    def __key_pressed(self, event):
        but = event.keycode
        print(but)

        if but == keys.Escape.value:
            self.close_main_win()

    # Клавиша отжата
    def __key_released(self, event):
        but = event.keycode

    #  Включить бинд клавиш
    def bind_keyboard(self, event=None):
        self.__parent.bind('<KeyPress>', self.__key_pressed)
        self.__parent.bind('<KeyRelease>', self.__key_released)

    #  Выключить бинд клавиш
    def unbind_keyboard(self, event=None):
        self.__parent.unbind('<KeyPress>')
        self.__parent.unbind('<KeyRelease>')
