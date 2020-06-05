from tkinter import *
import tkinter.ttk as ttk


class exp_fr_cls():
    def __init__(self):
        self.__parent = self.root

        self.experiment_frame = Frame(self.__parent, bg=self.frames_color, width=150,
                                      highlightcolor=self.frames_border_color,
                                      highlightbackground=self.frames_border_color,
                                      highlightthickness=self.frames_border_thick)


        self.exp_treeview = ttk.Treeview(self.experiment_frame, selectmode="browse")

        self.exp_treeview.column("#0", width=260, minwidth=260, stretch=NO)
        self.exp_treeview.heading("#0", text="Эксперимент", anchor=W)

        self.exp_fr_pack()

    def exp_fr_pack(self):
        self.experiment_frame.pack(side=LEFT, padx=0, pady=0, fill=BOTH)

        self.exp_treeview.pack(side=TOP, fill=BOTH, expand=True)
