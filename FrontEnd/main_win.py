from tkinter import *

from FrontEnd.top_drop_down_menus import t_d_d_m_cls as t_d_d_m
from FrontEnd.experiment_frame import exp_fr_cls as exp_fr
from FrontEnd.review_frame import rev_fr_cls as rev_fr

from BackEnd.keyboard_binds import k_b_cls as k_b

class main_win_cls(t_d_d_m,
                   k_b,
                   exp_fr,
                   rev_fr):
    def __init__(self, main_win_settings, comboboxes_settings, frames_settings):

        # Параметры ...
        # ... главного окна
        self.main_win_width = main_win_settings[0]
        self.main_win_height = main_win_settings[1]
        self.main_win_resize_x = main_win_settings[2]
        self.main_win_resize_y = main_win_settings[3]
        self.min_size_flag = main_win_settings[4]
        self.main_win_title = main_win_settings[5]
        self.main_win_color = main_win_settings[6]
        self.main_win_zoom = main_win_settings[8]
        # ... ... рамка информации
        self.info_frame = None

        # ... выпадающих меню
        self.comboboxes_width = comboboxes_settings[0]
        self.comboboxes_height = comboboxes_settings[1]
        self.comboboxes_padx = comboboxes_settings[2]
        self.comboboxes_pady = comboboxes_settings[3]
        self.comboboxes_font = comboboxes_settings[4]

        # ... рамок
        self.frames_padx = frames_settings[0]
        self.frames_pady = frames_settings[1]
        self.frames_color = frames_settings[2]
        self.frames_border_color = frames_settings[3]
        self.frames_border_thick = frames_settings[4]

        # ... внутренние переменные
        self.__title_icon_main_win = None  # Иконка гл. окна
        self.__title_icon_main_win_dir = main_win_settings[7]  # Дирректория иконки гл. окна

        # Объявление главного окна как объект
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close_main_win)

        # Иницилизация рамки информации
        self.info_frame_pack()

        # Иницилизация верхних выпадающих меню (Combobox)
        t_d_d_m.__init__(self)

        # Иницилизация бинда клавиш
        k_b.__init__(self)

        # Иницилизация рамки эксперимента
        exp_fr.__init__(self)

        # Иницилизация рамки анализа
        rev_fr.__init__(self)

        # self.test_height = 260
        # self.root.after(250, self.test)

    def test(self):
        self.experiment_frame.config(width=self.test_height)
        self.test_height += 10
        self.root.after(250, self.test)

    # Упаковка виджетов и открытие главного окна
    def open_main_win(self):
        # Размеры и положение
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        main_x = screen_width/2 - self.main_win_width/2
        main_y = screen_height/2 - self.main_win_height/2
        self.root.geometry("+%d+%d" % (main_x, main_y))
        self.root.geometry(str(self.main_win_width) + 'x' + str(self.main_win_height))
        if self.main_win_resize_y == 'True':
            self.root.minsize(self.main_win_width, self.main_win_height)
        else:
            self.root.minsize(0, 0)
        self.root.resizable(width=self.main_win_resize_x, height=self.main_win_resize_y)

        # ... открыть окно на весь экран
        if self.main_win_zoom:
            self.root.state('zoomed')

        # Наименование и иконка
        self.root.title(self.main_win_title)
        try:
            self.__title_icon_main_win = PhotoImage(file=self.__title_icon_main_win_dir)
            self.root.tk.call('wm', 'iconphoto', self.root, self.__title_icon_main_win)
        except:
            pass

        # Открытие основоного окна
        self.root.mainloop()

    # Рамка с информацией снизу
    def info_frame_pack(self):
        self.info_frame = Frame(self.root, bg=self.frames_color, height=20,
                                highlightcolor=self.frames_border_color)

        self.info_frame.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH)

    # Функция вызываемая при закрытии главного окна
    def close_main_win(self, event=None):
        self.root.destroy()
