from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import numpy as np
# from kivy.core.window import Window


class MainWindow(Screen):
    pass


class PopupWindow(Screen):
    @staticmethod
    def pop_btn():
        pop_up()


class PopupWindowEnd(Screen):
    @staticmethod
    def pop_btn_end():
        pop_up2()

    def score_show(self):
        self.ids.score_display_1.text = f"{SecondWindow.names_list[0]}: {MainGameWindow2.score_print[-2]}           " +\
                                        f"{ SecondWindow.names_list[1]}: {MainGameWindow2.score_print[-1]}"


class PopupWindowEnd2(Screen):
    @staticmethod
    def pop_btn_end2():
        pop_up3()

    def score_show(self):
        self.ids.score_display_1.text = (f'{ThirdWindow.names_list[0]}: {MainGameWindow3.score_print[0]}        ' +
                                         f'{ThirdWindow.names_list[1]}: {MainGameWindow3.score_print[1]}        ' +
                                         f'{ThirdWindow.names_list[2]}: {MainGameWindow3.score_print[2]}')


class SecondWindow(Screen):
    name_1 = ObjectProperty(None)
    name_2 = ObjectProperty(None)
    starting_score_1 = ObjectProperty(None)
    starting_score_2 = ObjectProperty(None)
    names_list = []
    starting_score_list = []

    def clear_window(self):
        self.names_list.append(self.name_1.text)
        self.names_list.append(self.name_2.text)
        while True:
            try:
                self.starting_score_list.append(int(self.starting_score_1.text))
                self.starting_score_list.append(int(self.starting_score_2.text))
                break

            except ValueError:
                self.starting_score_list.append(0)
                self.starting_score_list.append(0)
                break

        self.starting_score_1.text = ""
        self.starting_score_2.text = ""


class ThirdWindow(Screen):
    names_list = []
    scores_list = []

    def collect_names(self):
        self.names_list.append(self.ids.name_3_1.text)
        self.names_list.append(self.ids.name_3_2.text)
        self.names_list.append(self.ids.name_3_3.text)

    def collect_scores(self):
        try:
            self.scores_list.append(int(self.ids.score_3_1.text))
            self.scores_list.append(int(self.ids.score_3_2.text))
            self.scores_list.append(int(self.ids.score_3_3.text))
        except ValueError:
            self.scores_list.append(0)
            self.scores_list.append(0)
            self.scores_list.append(0)


class MainGameWindow2(Screen):

    score_print = []
    points_dict = {}
    hand_number = 0
    hand_royalties_list = []
    hand_points_list = []
    show_list = [0, 0]

    def name_import(self):
        self.ids.name_label_1.text = SecondWindow.names_list[0]
        self.ids.name_label_2.text = SecondWindow.names_list[1]
        self.ids.score_id.text = f"{SecondWindow.names_list[0]}: {SecondWindow.starting_score_list[0]}           " + \
                                 f"{ SecondWindow.names_list[1]}: {SecondWindow.starting_score_list[1]}"
        self.ids.hand_n.text = f"Hand Number: {MainGameWindow2.hand_number + 1}"
        self.points_dict[0] = SecondWindow.starting_score_list

    def collect_data(self):
        try:
            MainGameWindow2.hand_royalties_list.append(int(self.ids.points_1.text))
            MainGameWindow2.hand_royalties_list.append(int(self.ids.points_2.text))
            MainGameWindow2.hand_royalties_list.append(int(self.ids.row_points.text))
            self.ids.points_1.text = "Conf."
            self.ids.points_2.text = "Conf."
            self.ids.row_points.text = "Conf."

        except ValueError:
            self.ids.points_1.text = ""
            self.ids.points_2.text = ""
            self.ids.row_points.text = ""

    def do_math(self):
        try:
            hand_points_list = []
            h_p_1 = (self.hand_royalties_list[0] - self.hand_royalties_list[1]) + self.hand_royalties_list[2]
            h_p_2 = - h_p_1
            hand_points_list.append(h_p_1)
            hand_points_list.append(h_p_2)
            self.points_dict[self.hand_number + 1] = hand_points_list
            self.ids.score_id.text = f"{SecondWindow.names_list[0]}: {hand_points_list[0]}           { SecondWindow.names_list[1]}: {hand_points_list[1]}"

        except IndexError:
            pass

    def score_f(self):
        try:
            for_zip = self.points_dict.values()
            self.show_list = sum(map(np.array, for_zip))
            self.ids.score_show.text = f"Score: {self.show_list[0]} / {self.show_list[1]}"
            self.hand_royalties_list.clear()
            MainGameWindow2.hand_number += 1
            self.ids.hand_n.text = f"Hand Number: {MainGameWindow2.hand_number + 1}"
            self.ids.points_1.text = ""
            self.ids.points_2.text = ""
            self.ids.row_points.text = ""
            self.score_print.append(self.show_list[0])
            self.score_print.append(self.show_list[1])

        except TypeError:
            pass

    @staticmethod
    def pop_btn():
        pop_up()

    @staticmethod
    def pop_btn_end():
        pop_up2()

    def del_hand(self):
        self.points_dict[self.hand_number ] = [0, 0]


class MainGameWindow3(Screen):
    start_score_1 = 0
    start_score_2 = 0
    start_score_3 = 0
    hand_number = 0
    points_dict = {}
    show_list = []
    score_print = []

    @staticmethod
    def pop_btn():
        pop_up()

    @staticmethod
    def pop_btn_end2():
        pop_up3()

    def start_fnc(self):
        self.ids.name_1.text = ThirdWindow.names_list[0]
        self.ids.name_2.text = ThirdWindow.names_list[1]
        self.ids.name_3.text = ThirdWindow.names_list[2]
        self.start_score_1 = ThirdWindow.scores_list[0]
        self.start_score_2 = ThirdWindow.scores_list[1]
        self.start_score_3 = ThirdWindow.scores_list[2]
        self.ids.hand_label.text = f'Hand No: {self.hand_number + 1} '
        self.ids.hand_score.text = (f'{ThirdWindow.names_list[0]}: {ThirdWindow.scores_list[0]}        ' +
                                    f'{ThirdWindow.names_list[1]}: {ThirdWindow.scores_list[1]}        ' +
                                    f'{ThirdWindow.names_list[2]}: {ThirdWindow.scores_list[2]}')
        self.points_dict[self.hand_number] = [self.start_score_1, self.start_score_2, self.start_score_3]

    def collect_score(self):
        hand_points_list = []
        hand_royalties_list = []
        hand_row_points = []
        try:
            r_r_1 = int(self.ids.row_1.text)
            hand_row_points.append(int(self.ids.row_1.text))
            r_r_2 = int(self.ids.row_2.text)
            hand_row_points.append(int(self.ids.row_2.text))
            r_r_3 = int(self.ids.row_3.text)
            hand_row_points.append(int(self.ids.row_3.text))

            h_r_1 = int(self.ids.points_1.text)
            hand_royalties_list.append(int(self.ids.points_1.text))
            h_r_2 = int(self.ids.points_2.text)
            hand_royalties_list.append(int(self.ids.points_1.text))
            h_r_3 = int(self.ids.points_3.text)
            hand_royalties_list.append(int(self.ids.points_1.text))

            points_list1 = (h_r_1 - h_r_2) + (h_r_1 - h_r_3) + r_r_1 + r_r_3
            hand_points_list.append(points_list1)
            points_list2 = (h_r_2 - h_r_1) + (h_r_2 - h_r_3) - r_r_1 + r_r_2
            hand_points_list.append(points_list2)
            points_list3 =  (h_r_3 - h_r_1) + (h_r_3 - h_r_2) - r_r_2 + r_r_3
            hand_points_list.append(points_list3)
            self.points_dict[self.hand_number + 1] = hand_points_list

        except ValueError:
                pass

    def score_calc(self):
        try:
            hand_points_list2 = self.points_dict[self.hand_number +1]
            self.ids.hand_score.text = (f'{ThirdWindow.names_list[0]}: {hand_points_list2[0]}        ' +
                                        f'{ThirdWindow.names_list[1]}: {hand_points_list2[1]}        ' +
                                        f'{ThirdWindow.names_list[2]}: {hand_points_list2[2]}')
            for_zip = self.points_dict.values()
            self.show_list = sum(map(np.array, for_zip))
            self.ids.score_label.text = f"Score: {self.show_list[0]} / {self.show_list[1]} / {self.show_list[2]}"
            self.ids.row_1.text = ''
            self.ids.row_2.text = ''
            self.ids.row_3.text = ''
            self.ids.points_1.text = ''
            self.ids.points_2.text = ''
            self.ids.points_3.text = ''
            self.hand_number += 1
            self.ids.hand_label.text = f"Hand No: {self.hand_number + 1}"
            self.score_print.append(self.show_list[0])
            self.score_print.append(self.show_list[1])
            self.score_print.append(self.show_list[2])
        except KeyError:
            pass

    def del_hand(self):
        self.points_dict[self.hand_number] = [0, 0, 0]


class WindowManager(ScreenManager):
    pass


def pop_up():
    show = PopupWindow()
    popupWindow = Popup(title="Royalties Table", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow.open()


def pop_up2():
    show = PopupWindowEnd()
    popupWindow2 = Popup(title="", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow2.open()


def pop_up3():
    show = PopupWindowEnd2()
    popupWindow3 = Popup(title="", content=show, size_hint=(None, None), size=(400, 400))
    popupWindow3.open()


kv = Builder.load_file('my.kv')


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
