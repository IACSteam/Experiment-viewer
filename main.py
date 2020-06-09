# from Excel_Functions.test import xl_test_class

from FrontEnd.main_win import main_win_cls as m_w

import BackEnd.UI_Settings as UI_Sts

if __name__ == '__main__':
    # arr = ["Подгруппа 1", "Подгруппа 2"]
    # setarr = set(arr)
    # if len(arr) == len(setarr):
    #     print("Все элементы уникальны")
    # else:
    #     print("Есть одинаковые")
    # raise SystemExit(0)
    main_window = m_w(UI_Sts.main_win_settings(),
                      UI_Sts.comboboxes_settings(),
                      UI_Sts.frames_settings(),
                      UI_Sts.labels_settings(),
                      UI_Sts.buttons_settings())

    main_window.open_main_win()

    raise SystemExit(0)
