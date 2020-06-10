from tkinter import *

from FrontEnd.top_drop_down_menus import t_d_d_m_cls as t_d_d_m
from FrontEnd.experiment_frame import exp_fr_cls as exp_fr
from FrontEnd.view_frame import view_fr_cls as view_fr

from BackEnd.keyboard_binds import k_b_cls as k_b
from BackEnd.view_frame_back import view_frame_graphs as graphs
from BackEnd.experiment_frame_back import experiment_treeview_funs as exp_tree


class main_win_cls(t_d_d_m,
                   k_b,
                   exp_fr, exp_tree,
                   view_fr, graphs):
    def __init__(self, main_win_settings, comboboxes_settings, frames_settings, labels_settings, buttons_settings):

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
        self.info_fr_test_but1 = None
        self.info_fr_test_but2 = None
        self.info_fr_test_but3 = None
        self.info_fr_test_but4 = None

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

        # ... надписей (Label)
        self.labels_font = labels_settings[0]
        self.labels_text_color = labels_settings[1]

        # ... кнопок (Buttons)
        self.buttons_bg_color = buttons_settings[0]
        self.buttons_active_color = buttons_settings[1]
        self.buttons_text_normal_color = buttons_settings[2]
        self.buttons_text_active_color = buttons_settings[3]
        self.buttons_text_font = buttons_settings[4]
        self.buttons_relief = buttons_settings[5]
        self.buttons_overelief = buttons_settings[6]
        self.buttons_select_relief = buttons_settings[7]
        self.buttons_padx = buttons_settings[8]
        self.buttons_pady = buttons_settings[9]

        # ... внутренние переменные
        self.__title_icon_main_win = None  # Иконка гл. окна
        self.__title_icon_main_win_dir = main_win_settings[7]  # Дирректория иконки гл. окна
        self.exp_groups_and_subgroups = []  # Список всех групп и их подгрупп эксперимента

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
        # ... дерево (Treeview)
        exp_tree.__init__(self)

        # Иницилизация рамки анализа
        view_fr.__init__(self)
        # ... графики
        graphs.__init__(self)

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
        main_x = screen_width / 2 - self.main_win_width / 2
        main_y = screen_height / 2 - self.main_win_height / 2
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

        self.info_frame_label = Label(self.info_frame,
                                      text="Надпись описания некторых виджетов программы",
                                      font=self.labels_font,
                                      bg=self.frames_color,
                                      fg=self.labels_text_color)

        # Кнопки для отладки !!!
        self.info_fr_test_but1 = Button(self.info_frame,
                                        image=None,
                                        text="Очистить оси",
                                        activebackground=self.buttons_active_color,
                                        relief=self.buttons_relief,
                                        overrelief=self.buttons_overelief,
                                        bg=self.buttons_bg_color,
                                        fg=self.buttons_text_normal_color,
                                        activeforeground=self.buttons_text_active_color,
                                        font=self.buttons_text_font,
                                        command=self.clear_axes
                                        )
        self.info_fr_test_but2 = Button(self.info_frame,
                                        image=None,
                                        text="Построить",
                                        activebackground=self.buttons_active_color,
                                        relief=self.buttons_relief,
                                        overrelief=self.buttons_overelief,
                                        bg=self.buttons_bg_color,
                                        fg=self.buttons_text_normal_color,
                                        activeforeground=self.buttons_text_active_color,
                                        font=self.buttons_text_font,
                                        command=self.build_plot
                                        )
        self.info_fr_test_but3 = Button(self.info_frame,
                                        image=None,
                                        text="Генер.",
                                        activebackground=self.buttons_active_color,
                                        relief=self.buttons_relief,
                                        overrelief=self.buttons_overelief,
                                        bg=self.buttons_bg_color,
                                        fg=self.buttons_text_normal_color,
                                        activeforeground=self.buttons_text_active_color,
                                        font=self.buttons_text_font,
                                        command=self.rand_axes_x_y
                                        )

        self.info_fr_test_but4 = Button(self.info_frame,
                                        image=None,
                                        text="Отладка 4",
                                        activebackground=self.buttons_active_color,
                                        relief=self.buttons_relief,
                                        overrelief=self.buttons_overelief,
                                        bg=self.buttons_bg_color,
                                        fg=self.buttons_text_normal_color,
                                        activeforeground=self.buttons_text_active_color,
                                        font=self.buttons_text_font,
                                        command=None
                                        )

        self.info_frame.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH)
        self.info_frame_label.pack(side=LEFT)
        self.info_fr_test_but4.pack(side=RIGHT)
        self.info_fr_test_but3.pack(side=RIGHT)
        self.info_fr_test_but2.pack(side=RIGHT)
        self.info_fr_test_but1.pack(side=RIGHT)

    # Функция вызываемая при закрытии главного окна
    def close_main_win(self, event=None):
        self.root.destroy()
