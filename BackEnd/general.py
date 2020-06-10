from tkinter import *


#   Добавление картинки и проверка на её существование
def image_add(image_dir):
    try:
        img = PhotoImage(file=image_dir)
    except:
        img = None
    return img
