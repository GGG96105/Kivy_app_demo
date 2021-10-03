from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import numpy as np


class MainWindow(Screen):
    pass


class PopupWindow(Screen):
    @staticmethod
    def pop_btn(self):
        pop_up()


class PopupWindowEnd(Screen):
    @staticmethod
    def pop_btn_end():
        pop_up2()

    def score_show(self):
        self.ids.score_display_1.text = f"{SecondWindow.names_list[0]}: {MainGameWindow2.score_print[-2]}           { SecondWindow.names_list[1]}: {MainGameWindow2.score_print[-1]}"
        print(MainGameWindow2.score_print[-1])
        print(MainGameWindow2.score_print[-2])


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

    def print_names(self):
        for name in self.names_list:
            print(name)
        for number in self.starting_score_list:
            print(number)


class ThirdWindow(Screen):
    pass


class MainGameWindow2(Screen):

    score_print=[]
    points_dict = {}
    hand_number = 0
    hand_royalties_list = []
    hand_points_list = []
    show_list = [0, 0]

    def name_import(self):
        self.ids.name_label_1.text = SecondWindow.names_list[0]
        self.ids.name_label_2.text = SecondWindow.names_list[1]
        self.ids.score_id.text = f"{SecondWindow.names_list[0]}: {SecondWindow.starting_score_list[0]}           { SecondWindow.names_list[1]}: {SecondWindow.starting_score_list[1]}"
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
            # print(self.points_dict[self.hand_number])
            # MainGameWindow2.hand_number += 1
            # self.ids.hand_n.text = f"Hand Number: {MainGameWindow2.hand_number + 1}"
            self.ids.score_id.text = f"{SecondWindow.names_list[0]}: {hand_points_list[0]}           { SecondWindow.names_list[1]}: {hand_points_list[1]}"
            # self.hand_royalties_list.clear()
            # self.hand_points_list.clear()
            print("*" * 80)
        except IndexError:
            pass

    def score_f(self):
        try:
            for_zip = self.points_dict.values()
            self.show_list = sum(map(np.array, for_zip))
            self.ids.score_show.text = f"Score: {self.show_list[0]} / {self.show_list[1]}"
            self.hand_royalties_list.clear()
            # self.hand_points_list.clear()
            MainGameWindow2.hand_number += 1
            self.ids.hand_n.text = f"Hand Number: {MainGameWindow2.hand_number + 1}"
            self.ids.points_1.text = ""
            self.ids.points_2.text = ""
            self.ids.row_points.text = ""
            print('*'*80)
            print(self.hand_number)
            for item in self.points_dict.values():
                print(item)
            print('*'*80)
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
        self.points_dict[self.hand_number - 1] = [0, 0]


class MainGameWindow3(Screen):

    @staticmethod
    def pop_btn():
        pop_up()


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


kv = Builder.load_file('my.kv')


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
