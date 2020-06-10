# Настройки главного окна
def main_win_settings():
    width = 800
    height = 600
    resize_x = True
    resize_y = True
    min_size_flag = False
    title = "Experiment viewer"
    color = 'white'
    title_icon_dir = 'Icons/title_icon.png'
    zoomed = False

    return [width, height,
            resize_x, resize_y,
            min_size_flag,
            title,
            color,
            title_icon_dir,
            zoomed]


# Настройки выпадающих меню (Combobox)
def comboboxes_settings():
    width = 10
    height = 11
    padx = 1
    pady = 1
    font = 'Consolas 10'

    return [width, height,
            padx, pady,
            font]


# Настройки рамок(Frames)
def frames_settings():
    padx = 2
    pady = 2
    color = 'gray'
    border_color = 'silver'
    border_thick = 1

    return [padx, pady,
            color,
            border_color, border_thick]


# Настройки надписей(Frames)
def labels_settings():
    font = 'Consolas 10'
    bg = 'black'
    return [font, bg]


# Настройки кнопок(Buttons)
def buttons_settings():
    bg_color = 'gray'
    active_color = 'white'
    text_normal_color = 'black'
    text_active_color = 'green'
    text_font = 'Consolas 10'
    relief = "raised"
    overelief = "ridge"
    select_relief = 'groove'
    padx = 0
    pady = 0

    return [bg_color, active_color,
            text_normal_color, text_active_color, text_font,
            relief, overelief, select_relief,
            padx, pady]
