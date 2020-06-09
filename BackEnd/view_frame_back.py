from tkinter import *

import numpy as np


class view_frame_graphs():
    def __init__(self):
        self.graphs_x = None
        self.graphs_y = None

    # Очистить оси
    def clear_axes(self):
        self.rev_subplot.clear()
        self.rev_canva.draw()

    # Построить график
    def build_plot(self):
        try:
            self.rev_subplot.plot(self.graphs_x, self.graphs_y)
        except:
            pass
        self.rev_canva.draw()

    # Сгенерировать произвольные значения осей
    def rand_axes_x_y(self, length=100):
        self.graphs_y = np.random.randint(0, length, length)
        self.graphs_x = np.arange(0, length)
