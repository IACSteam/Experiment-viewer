from tkinter import *


class rev_fr_cls():
    def __init__(self):
        self.__parent = self.root

        self.review_frame = Frame(self.__parent, bg=self.frames_color, width=150,
                                  highlightcolor=self.frames_border_color,
                                  highlightbackground=self.frames_border_color,
                                  highlightthickness=self.frames_border_thick)

        self.rev_fr_pack()


    def rev_fr_pack(self):
        self.review_frame.pack(side=LEFT, padx=0, pady=0, fill=BOTH, expand=TRUE)
