# from Excel_Functions.test import xl_test_class

from FrontEnd.main_win import main_win_cls as m_w

import BackEnd.UI_Settings as UI_Sts

if __name__ == '__main__':
    main_window = m_w(UI_Sts.main_win_settings(),
                      UI_Sts.comboboxes_settings(),
                      UI_Sts.frames_settings(),
                      UI_Sts.labels_settings(),
                      UI_Sts.buttons_settings())

    main_window.open_main_win()

    raise SystemExit(0)
