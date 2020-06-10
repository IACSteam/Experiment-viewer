from tkinter import *

import BackEnd.general as gen_funs

import copy


class experiment_treeview_funs():
    def __init__(self):
        # Иницилизация иконок
        self.__group_icon = None
        self.__subgroup_icon = None

        self.__group_icon = gen_funs.image_add(image_dir="icons/group_icon.png")
        self.__subgroup_icon = gen_funs.image_add(image_dir="icons/subgroup_icon.png")

    # Создать группу (Treeview)
    def exp_tree_create_group(self, group_name='Группа 1', selection_set=True):
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
                arr[-1] = self.exp_groups_and_subgroups[-1][0][:-(i - 1)] + str(num)
            setarr = set(copy.deepcopy(arr))

            self.exp_groups_and_subgroups[-1][0] = arr[-1]

        gr_name = self.exp_groups_and_subgroups[-1][0]
        tag = 'GrId_' + gr_name
        self.exp_treeview.insert('', "end", tag, text=gr_name, image=self.__group_icon)

        # Выделить вставленную грппу
        if selection_set:
            self.exp_treeview.selection_clear()
            self.exp_treeview.selection_set(tag)

        print(self.exp_groups_and_subgroups)

    # Создать подгруппу в указанной группе (Treeview)
    def exp_tree_create_subgroup(self, group_name="Группа 1", subgroup_name="Подгруппа 1", selection_set=True):
        # Проверка на существование группы
        check = self.exp_group_exist_check(group_name)
        if check[0]:
            group_index = check[1]
        else:
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
                num = int(self.exp_groups_and_subgroups[group_index][1][-1][-(i - 1):]) + 1
                self.exp_groups_and_subgroups[group_index][1][-1] = \
                    self.exp_groups_and_subgroups[group_index][1][-1][:-(i - 1)] + str(num)

            setarr = set(copy.deepcopy(self.exp_groups_and_subgroups[group_index][1]))

        subgr_name = self.exp_groups_and_subgroups[group_index][1][-1]
        subgr_tag = 'SubGrId_' + group_name.strip() + '_' + subgr_name
        gr_tag = 'GrId_' + group_name.strip()
        try:
            self.exp_treeview.insert('GrId_' + group_name.strip(), "end", iid=subgr_tag, text=subgr_name,
                                     image=self.__subgroup_icon)
        except:
            pass

        if selection_set:
            self.exp_treeview.item(gr_tag, open=True)
            self.exp_treeview.selection_clear()
            self.exp_treeview.selection_set(subgr_tag)

        print(self.exp_groups_and_subgroups)

    # Удалить группу
    def exp_tree_delete_group(self, group_name='Группа 1'):
        # Проверка на существование группы
        check = self.exp_group_exist_check(group_name)
        if check[0]:
            group_index = check[1]
        else:
            return
        del self.exp_groups_and_subgroups[group_index]
        gr_tag = 'GrId_' + group_name.strip()
        self.exp_treeview.delete(gr_tag)

        print(self.exp_groups_and_subgroups)

    # Удалить подгруппу
    def exp_tree_delete_subgroup(self, subgroup_tag):
        # Определяем имя группы и подгруппы по тэгу
        names = self.exp_gr_and_subgr_names_from_tag(subgroup_tag)
        group_name = names[0]
        sub_group_name = names[1]
        # Проверка на существование группы
        check1 = self.exp_group_exist_check(group_name)
        if check1[0]:
            group_index = check1[1]
        else:
            return
        # Проверка на существование подгруппы
        check2 = self.exp_subgroup_exist_check(group_index, sub_group_name)
        if check2[0]:
            subgroup_index = check2[1]
        else:
            return
        del self.exp_groups_and_subgroups[group_index][1][subgroup_index]
        self.exp_treeview.delete(subgroup_tag)

        print(self.exp_groups_and_subgroups)

    # Проверка на существование группы
    def exp_group_exist_check(self, group_name):
        i = 0
        group_index = None
        exist = False
        while i < len(self.exp_groups_and_subgroups):
            if group_name.strip() == self.exp_groups_and_subgroups[i][0]:
                exist = True
                group_index = i
                break
            i += 1
        else:
            if group_index == None:
                exist = False

        return [exist, group_index]

    # Проверка на существование подгруппы в группе с индексом (group_index)
    def exp_subgroup_exist_check(self, group_index, subgroup_name):
        i = 0
        subgroup_index = None
        exist = False
        while i < len(self.exp_groups_and_subgroups[group_index][1]):
            if subgroup_name.strip() == self.exp_groups_and_subgroups[group_index][1][i]:
                exist = True
                subgroup_index = i
                break
            i += 1
        else:
            if group_index == None:
                exist = False

        return [exist, subgroup_index]

    # Определение имя группы и подгруппы из тэга элемента
    def exp_gr_and_subgr_names_from_tag(self, tag):
        group_name = None
        subgroup_name = None
        if tag[:5] == 'GrId_':
            group_name = tag[5:]
            subgroup_name = None
        elif tag[:8] == 'SubGrId_':
            i = 0
            indexes = []
            while i < len(tag):
                if tag[i] == '_':
                    indexes.append(i)
                i += 1
            group_name = tag[indexes[0] + 1:indexes[1]]
            subgroup_name = tag[indexes[1] + 1:]

        return [group_name, subgroup_name]
