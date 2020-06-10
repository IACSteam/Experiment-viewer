from tkinter import *
import tkinter.ttk as ttk

import copy


class exp_fr_cls():
    def __init__(self):
        self.__parent = self.root

        # Рамка эксперимента
        self.experiment_frame = Frame(self.__parent, bg=self.frames_color,
                                      highlightcolor=self.frames_border_color,
                                      highlightbackground=self.frames_border_color,
                                      highlightthickness=self.frames_border_thick)
        self.experiment_frame_p1 = Frame(self.experiment_frame, bg=self.frames_color,
                                         highlightcolor=self.frames_border_color,
                                         highlightbackground=self.frames_border_color,
                                         highlightthickness=self.frames_border_thick)
        self.experiment_frame_p2 = Frame(self.experiment_frame, bg=self.frames_color,
                                         highlightcolor=self.frames_border_color,
                                         highlightbackground=self.frames_border_color,
                                         highlightthickness=self.frames_border_thick)
        self.experiment_frame_p2_1 = Frame(self.experiment_frame_p2, bg=self.frames_border_color, width=17)

        # Дерево
        self.exp_treeview = ttk.Treeview(self.experiment_frame_p1, selectmode="browse", padding=10)

        self.exp_treeview.column("#0", width=260, minwidth=260, stretch=YES)
        self.exp_treeview.heading("#0", text="Эксперимент", anchor=W)
        # ... скрол(ScrollBar) по y
        self.__exp_treeview_yscroll = Scrollbar(self.experiment_frame_p1, orient="vertical")
        self.__exp_treeview_yscroll.config(command=self.exp_treeview.yview)
        self.exp_treeview.config(yscrollcommand=self.__exp_treeview_yscroll.set)
        # ... скрол(ScrollBar) по x
        self.__exp_treeview_xscroll = Scrollbar(self.experiment_frame_p2, orient=HORIZONTAL)
        self.__exp_treeview_xscroll.config(command=self.exp_treeview.xview)
        self.exp_treeview.config(xscrollcommand=self.__exp_treeview_xscroll.set)
        # ... конекстное меню(Menu)
        self.__exp_treeview_menu = Menu(tearoff=0)
        # ... бинды дерева
        self.exp_treeview.bind('<<TreeviewSelect>>', self.exp_treeview_selection_handler)
        self.exp_treeview.bind("<Button-3>", self.exp_treeview_RB_handler)

        # self.__animation_pan_list_scroll = Scrollbar(self.__animation_pan_p2_2, orient="vertical")
        # self.__animation_pan_list_scroll.config(command=self.animation_pan_list_frames.yview)
        # self.animation_pan_list_frames.config(yscrollcommand=self.__animation_pan_list_scroll.set)

        # Упаковка рамки эксперимента
        self.exp_fr_pack()

        # Вставка групп и подгрупп(тест)
        # j = 1
        # group_name = "Группа "
        # subgroup_name = "Подгруппа "
        # while j <= 2:
        #     self.exp_tree_create_group(group_name=group_name + str(j))
        #     i = 1
        #     while i <= 25:
        #         self.exp_tree_create_subgroup(group_name=group_name + str(j), subgroup_name=subgroup_name + str(i))
        #         i += 1
        #     j += 1

    # Обработчик ПКМ по Treeview
    def exp_treeview_RB_handler(self, event=None):
        tag = self.exp_treeview.identify_row(event.y)
        # print(tag)
        self.__exp_treeview_menu.delete(0, 'end')
        if tag == '':
            self.__exp_treeview_menu.add_command(label='Добавить группу', command=self.exp_tree_create_group)
        elif tag[:5] == 'GrId_':
            self.exp_treeview.selection_set(tag)
            self.__exp_treeview_menu.add_command(label='Добавить подгруппу',
                                                 command=lambda: self.exp_tree_create_subgroup(group_name=tag[5:]))
            self.__exp_treeview_menu.add_command(label='Переименовать группу', command=None)
            self.__exp_treeview_menu.add_command(label='Удалить группу',
                                                 command=lambda: self.exp_tree_delete_group(group_name=tag[5:]))
        elif tag[:8] == 'SubGrId_':
            self.exp_treeview.selection_set(tag)
            self.__exp_treeview_menu.add_command(label='Переименовать подгруппу', command=None)
            self.__exp_treeview_menu.add_command(label='Удалить подгруппу',
                                                 command=lambda: self.exp_tree_delete_subgroup(subgroup_tag=tag))

        # Открыть контекстное меню
        self.__exp_treeview_menu.post(event.x_root, event.y_root)

    # Обработчик выделения строки дерева
    def exp_treeview_selection_handler(self, event=None):
        tag = self.exp_treeview.selection()[0]
        names = self.exp_gr_and_subgr_names_from_tag(tag)
        print(names)

    # Упаковка рамки эксперимента
    def exp_fr_pack(self):
        self.experiment_frame.pack(side=LEFT, padx=0, pady=0, fill=BOTH)

        self.experiment_frame_p1.pack(side=TOP, padx=0, pady=0, fill=BOTH, expand=True)
        self.exp_treeview.pack(side=LEFT, fill=BOTH, expand=True)
        self.__exp_treeview_yscroll.pack(side=RIGHT, fill=Y)

        self.experiment_frame_p2.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH)
        self.experiment_frame_p2_1.pack(side=RIGHT, padx=0, pady=0, fill=BOTH)
        self.__exp_treeview_xscroll.pack(side=LEFT, fill=X, expand=TRUE)
