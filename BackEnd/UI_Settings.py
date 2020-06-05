# Настройки главного окна
def main_win_settings():
    width = 800                             # 0
    height = 600                            # 1
    resize_x = True                         # 2
    resize_y = True                         # 3
    min_size_flag = False                            # 4
    title = "Experiment Reviewer"           # 5
    color = 'white'                         # 6
    title_icon_dir = 'Icons/title_icon.png'  # 7
    zoomed = False     # 8

    return [width, height,
            resize_x, resize_y,
            min_size_flag,
            title,
            color,
            title_icon_dir,
            zoomed]

# Настройка выпадающих меню (Combobox)
def comboboxes_settings():
    width = 10
    height = 11
    padx = 1
    pady = 1
    font = 'Consolas 10'

    return [width, height,
            padx, pady,
            font]

# Настройка рамок(Frames)
def frames_settings():
    padx = 2
    pady = 2
    color = 'gray'
    border_color = 'silver'
    border_thick = 1

    return [padx, pady,
            color,
            border_color, border_thick]


