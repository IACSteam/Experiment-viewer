from tkinter import *
from tkinter import ttk

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class view_fr_cls():
    def __init__(self):
        self.__parent = self.root

        self.review_frame = Frame(self.__parent, bg=self.frames_color, width=150,
                                  highlightcolor=self.frames_border_color,
                                  highlightbackground=self.frames_border_color,
                                  highlightthickness=self.frames_border_thick)

        # Объявление Notebook
        self.rev_notebook = ttk.Notebook(self.review_frame)

        # Вкладка настроек
        self.rev_nb_settings_frame = Frame(self.rev_notebook, bg=self.frames_color,
                                           highlightcolor=self.frames_border_color,
                                           highlightbackground=self.frames_border_color,
                                           highlightthickness=self.frames_border_thick)

        # Вкладка значений(таблицы)
        self.rev_nb_values_frame = Frame(self.rev_notebook, bg=self.frames_color,
                                         highlightcolor=self.frames_border_color,
                                         highlightbackground=self.frames_border_color,
                                         highlightthickness=self.frames_border_thick)

        # Вкладка отображения графиков(Graphs)
        self.rev_nb_graphs_frame = Frame(self.rev_notebook, bg=self.frames_color,
                                         highlightcolor=self.frames_border_color,
                                         highlightbackground=self.frames_border_color,
                                         highlightthickness=self.frames_border_thick)

        # ... иницилизация виджета графика
        self.rev_figure = None
        self.rev_subplot = None
        self.rev_canva = None
        self.rev_toolbar = None
        self.rev_graph_setup()

        # Упаковка рамки обзора
        self.view_fr_pack()

        # Выбрать вкладку отображаемую при включении программы
        self.rev_notebook.select(self.rev_nb_graphs_frame)

    def rev_graph_setup(self):
        self.rev_figure = Figure()
        self.rev_subplot = self.rev_figure.add_subplot(111)
        # self.rev_subplot.plot([1, 2, 3, 4], [1, 8, 3, 12])

        self.rev_canva = FigureCanvasTkAgg(self.rev_figure, self.rev_nb_graphs_frame)

        # Добавление тулбара
        self.rev_toolbar = NavigationToolbar2Tk(self.rev_canva, self.rev_nb_graphs_frame)
        self.rev_toolbar.update()

    # Упковка рамки обзора эксперимента
    def view_fr_pack(self):
        self.review_frame.pack(side=LEFT, padx=0, pady=0, fill=BOTH, expand=TRUE)
        # NoteBook
        self.rev_notebook.pack(fill=BOTH, expand=TRUE)
        self.rev_nb_settings_frame.pack(padx=0, pady=0, fill=BOTH, expand=TRUE)
        self.rev_notebook.add(self.rev_nb_settings_frame, text="Настройки")
        self.rev_nb_values_frame.pack(padx=0, pady=0, fill=BOTH, expand=TRUE)
        self.rev_notebook.add(self.rev_nb_values_frame, text="Значения")

        # Вкладка графика
        self.rev_nb_graphs_frame.pack(padx=0, pady=0, fill=BOTH, expand=TRUE)
        self.rev_notebook.add(self.rev_nb_graphs_frame, text="График")
        self.rev_canva.get_tk_widget().pack(fill=BOTH, expand=TRUE)
        self.rev_canva._tkcanvas.pack()
