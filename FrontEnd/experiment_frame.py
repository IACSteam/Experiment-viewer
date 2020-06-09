from tkinter import *
import tkinter.ttk as ttk

import copy


class exp_fr_cls():
    def __init__(self):
        self.__parent = self.root
        self.__treeview_exp_groups = []

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
        j = 1
        group_name = "Группа "
        subgroup_name = "Подгруппа "
        while j <= 2:
            self.exp_fr_create_group(group_name=group_name+str(j))
            i = 1
            while i <= 25:
                self.exp_fr_create_subgroup(group_name=group_name+str(j), subgroup_name=subgroup_name+str(i))
                i += 1
            j += 1

    def exp_treeview_RB_handler(self, event=None):
        tag = self.exp_treeview.identify_row(event.y)
        print(tag)
        self.__exp_treeview_menu.delete(0, 'end')
        if tag == '':
            self.__exp_treeview_menu.add_command(label='Добавить группу', command=self.exp_fr_create_group)
        elif tag[:5] == 'GrId_':
            self.exp_treeview.selection_set(tag)
            self.__exp_treeview_menu.add_command(label='Добавить подгруппу',
                                                 command=lambda: self.exp_fr_create_subgroup(group_name=tag[5:]))
            self.__exp_treeview_menu.add_command(label='Переименовать группу', command=None)
            self.__exp_treeview_menu.add_command(label='Удалить группу', command=None)
        elif tag[:8] == 'SubGrId_':
            self.exp_treeview.selection_set(tag)
            self.__exp_treeview_menu.add_command(label='Переименовать подгруппу', command=None)
            self.__exp_treeview_menu.add_command(label='Удалить подгруппу', command=None)

        self.__exp_treeview_menu.post(event.x_root, event.y_root)

    def exp_treeview_selection_handler(self, event=None):
        tag = self.exp_treeview.selection()[0]
        print(tag)
        pass

    # Создать группу (Treeview)
    def exp_fr_create_group(self, group_name='Группа 1'):
        self.exp_groups_and_subgroups.append([group_name.strip(), []])

        # Создание массива названий групп и множества групп для проверки уникальности
        i = 0
        arr = []
        while i < len(self.exp_groups_and_subgroups):
            arr.append(self.exp_groups_and_subgroups[i][0])
            i += 1
        setarr = set(copy.deepcopy(arr))

        while len(arr) != len(setarr):
            i = 1
            while True:
                try:
                    print(self.exp_groups_and_subgroups[-1][0])
                    int(self.exp_groups_and_subgroups[-1][0][-i])
                    pass
                except:
                    break
                i += 1

            if i == 1:
                num = 1
                arr[-1] = self.exp_groups_and_subgroups[-1][0] + str(num)
            else:
                num = int(self.exp_groups_and_subgroups[-1][0][-i:]) + 1
                arr[-1] = self.exp_groups_and_subgroups[-1][0][:-(i-1)] + str(num)
            setarr = set(copy.deepcopy(arr))

            self.exp_groups_and_subgroups[-1][0] = arr[-1]

        print(self.exp_groups_and_subgroups[-1][0])
        gr_name = self.exp_groups_and_subgroups[-1][0]
        self.__treeview_exp_groups.append(self.exp_treeview.insert('', "end", 'GrId_'+gr_name, text=gr_name))

    # Создать подгруппу в указанной группе (Treeview)
    def exp_fr_create_subgroup(self, group_name="Группа 1", subgroup_name="Подгруппа 1"):
        # Проверка на существование группы
        i = 0
        group_index = None
        while i < len(self.exp_groups_and_subgroups):
            if group_name.strip() == self.exp_groups_and_subgroups[i][0]:
                group_index = i
                break
            i += 1
        else:
            if group_index == None:
                return

        # Добавляем подгруппу
        self.exp_groups_and_subgroups[group_index][1].append(subgroup_name.strip())
        setarr = set(copy.deepcopy(self.exp_groups_and_subgroups[group_index][1]))
        arr = self.exp_groups_and_subgroups[group_index][1]
        while len(arr) != len(setarr):
            i = 1
            while True:
                try:
                    int(self.exp_groups_and_subgroups[group_index][1][-1][-i])
                except:
                    break
                i += 1

            if i == 1:
                num = 1
                self.exp_groups_and_subgroups[group_index][1][-1] = \
                    self.exp_groups_and_subgroups[group_index][1][-1] + str(num)
            else:
                num = int(self.exp_groups_and_subgroups[group_index][1][-1][-(i-1):]) + 1
                self.exp_groups_and_subgroups[group_index][1][-1] = \
                    self.exp_groups_and_subgroups[group_index][1][-1][:-(i-1)] + str(num)


            setarr = set(copy.deepcopy(self.exp_groups_and_subgroups[group_index][1]))
        subgr_name = self.exp_groups_and_subgroups[group_index][1][-1]
        try:
            self.exp_treeview.insert('GrId_'+group_name.strip(), "end", iid='SubGrId_'+group_name.strip()
                                                                            +'_'+subgr_name,
                                     text=subgr_name)
        except:
            pass

    # Упаковка рамки эксперимента
    def exp_fr_pack(self):
        self.experiment_frame.pack(side=LEFT, padx=0, pady=0, fill=BOTH)

        self.experiment_frame_p1.pack(side=TOP, padx=0, pady=0, fill=BOTH, expand=True)
        self.exp_treeview.pack(side=LEFT, fill=BOTH, expand=True)
        self.__exp_treeview_yscroll.pack(side=RIGHT, fill=Y)

        self.experiment_frame_p2.pack(side=BOTTOM, padx=0, pady=0, fill=BOTH)
        self.experiment_frame_p2_1.pack(side=RIGHT, padx=0, pady=0, fill=BOTH)
        self.__exp_treeview_xscroll.pack(side=LEFT, fill=X, expand=TRUE)
