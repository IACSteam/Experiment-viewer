from tkinter import *


class t_d_d_m_cls():
    def __init__(self):
        # Присвоение переменных классу
        self.__parent = self.root

        self.tdd_menu = Menu(self.__parent)
        self.__parent.config(menu=self.tdd_menu)

        self.file_menu = Menu(self.tdd_menu, tearoff=0)
        self.file_menu.add_command(label="Открыть файл Excel(.xlsx)...", command=None)
        self.file_menu.add_command(label="Открыть файл TDMS...", command=None)
        self.file_menu.add_command(label="Импорт из базы данных...", command=None)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Закрыть программу", command=self.close_main_win)

        self.tdd_menu.add_cascade(label="Файл", menu=self.file_menu)
