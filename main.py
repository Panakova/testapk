import kivy
kivy.require('1.11.1')

import datetime
from kivymd.app import MDApp

from helpers import screen_helper
from result import BehaviorModel1, BehaviorModel2, BehaviorModel3, BehaviorModel4

from functools import partial
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDIconButton,MDRaisedButton, MDFillRoundFlatButton,MDFloatingActionButton, MDRectangleFlatButton, MDFloatingActionButtonSpeedDial, MDFlatButton, MDRoundFlatButton
from kivy.uix.image import Image
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout, MDBoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem, ILeftBodyTouch, ThreeLineAvatarListItem
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import MDList, CheckboxLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.uix.gridlayout import GridLayout
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.bottomsheet import MDListBottomSheet


class ItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, choice):
        choice.active = True
        check_list = choice.get_widgets(choice.group)
        for check in check_list:
            if check != choice:
                check.active = False

class HomeScreen(Screen):
    choose_dialog= None
    choice = None
    help_dialog= None
    M_dialog = None

    def show_motivation_dialog (self):
        ok_button = MDRaisedButton(text="Poďme na to", on_release=self.close_M_dialog)
        self.M_dialog = MDDialog(title="Naučíš sa: ", text="- Lepšie spoznať svoje správanie a vystupovanie\n"
                                                                 "- Oodhaliť svoje osobné prednosti a tendencie\n"
                                                                 "- Využívať svoju energiu tam, kde môžete byť najúspešnejší\n"
                                                                 "- Vytvoriť si prostredie v tíme, ktoré najviac dopomôže k úspechu\n"
                                                                 "- Spoznať oblasti možných konfliktov s inými ľuďmi a zredukovať ich na minimum\n"
                                                                 "- Rozvíjať svoje silné stránky, sebapoznaním\n",
                                    size_hint=[0.8, 0.5], auto_dismiss=False,
                                    buttons=[ok_button])
        self.M_dialog.open()

    def close_M_dialog(self,obj):
        self.M_dialog.dismiss()

    def show_ChooseDialog(self):
        self.choose_dialog = MDDialog(title="Test zameraný pre:", type="confirmation",
                size_hint=[0.9, 0.5], auto_dismiss=False,
                items=[ItemConfirm(text="osobné zlepšenie",on_release= self.next_page_me,
                                   on_press= self.close_choose_dialog,),
                        ItemConfirm(text="prácu v tíme", on_release= self.next_page_team,
                                    on_press= self.close_choose_dialog, ),
                        ItemConfirm(text="osobné vzťahy",on_release= self.next_page_we,
                                    on_press= self.close_choose_dialog,)],)
        self.choose_dialog.open()


    def close_choose_dialog(self, obj):
        self.choose_dialog.dismiss()

    def next_page_me (self,obj):
        self.manager.current = "motivationme"
    def next_page_team (self,obj):
        self.manager.current = "motivationteam"
    def next_page_we (self,obj):
        self.manager.current = "motivationwe"

    def show_HelpDialog(self):
        ok_button = MDRaisedButton(text= "Rozummiem",on_release=self.close_help_dialog)
        self.help_dialog = MDDialog(title="O čo v teste ide?", text="Ak chceme v živote niečo dosiahnuť, potrebujeme vedieť, v čom sme výnimoční. Tento "
                                                                    "test ti ponúka 48 otázok, pre lepšie pochopenie svojjch schopností. Pokiaľ budeš "
                                                                    "odpovedať úprimne, umožnia ti vytvoriť prehľad svojej osobnosti. \n\n"
                                                                    "Poznať sám seba je prvý krok k úspechu.\n"
                                                                    "Ak chceš naozaj naplniť svoje túžby a zistiť, čo môžeš v živote dokázať, "
                                                                    "neváhaj začni už dnes! Zadefinuj si osobné ciele a vytrvaj v ich plnení. "
                                                                    "Časom si z nich vytvoríš návyk, ktorý ti pomôže spraviť seba lepším. \n\n"
                                                                    "Tak neváhaj a otvor sa sám sebe.",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog.open()

    def close_help_dialog(self,obj):
        self.help_dialog.dismiss()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "goals"
        elif button.icon == "notebook":
            self.manager.current = "history"


class MotivationScreenMe(Screen):

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("testy.txt", "a")
        file.write(self.ids.nazov_testu.text)
        file.write("\n")
        user = test(self.ids.nazov_testu.text)

class MotivationScreenTeam(Screen):
    nazov_testu = ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("testy.txt", "a")
        file.write(self.ids.nazov_testu.text)
        file.write("\n")

class MotivationScreenWe(Screen):
    nazov_testu = ObjectProperty(None)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

    def add_test(self):
        file = open("testy.txt", "a")
        file.write(self.ids.nazov_testu.text)
        file.write("\n")

class TestConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, choice):
        choice.active = True
        check_list = choice.get_widgets(choice.group)
        for check in check_list:
            if check != choice:
                check.active = False

class test:

    def __init__(self, testovatel, test_v=[], test_m=[]):
        self.testovatel = testovatel
        self.test_v = test_v
        self.test_m = test_m

    # spocitanie znakov v teste v#
    def pocetvd(self):
        d = self.test_v.count('d')
        return d

    def pocetvi(self):
        i = self.test_v.count('i')
        return i

    def pocetvs(self):
        s = self.test_v.count('s')
        return s

    def pocetvk(self):
        k = self.test_v.count('k')
        return k

    def pocetvn(self):
        n = self.test_v.count('n')
        return n

    def pocetmd(self):
        d = self.test_m.count('d')
        return d

    def pocetmi(self):
        i = self.test_m.count('i')
        return i

    def pocetms(self):
        s = self.test_m.count('s')
        return s

    def pocetmk(self):
        k = self.test_m.count('k')
        return k

    def pocetmn(self):
        n = self.test_m.count('n')
        return n

    # prepocet spolocneho vysledku testv-testm#
    def vyratajd(self):
        return self.pocetvd() - self.pocetmd()

    def vyrataji(self):
        return self.pocetvi() - self.pocetmi()

    def vyratajs(self):
        return self.pocetvs() - self.pocetms()

    def vyratajk(self):
        return self.pocetvk() - self.pocetmk()

    def vyratajn(self):
        return self.pocetvn() - self.pocetmn()

    # ntica testuv#
    def vysledok_v(self):
        return (self.pocetvd(), self.pocetvi(), self.pocetvs(), self.pocetvk(), self.pocetvn())

    # ntica testum#
    def vysledok_m(self):
        return (self.pocetmd(), self.pocetmi(), self.pocetms(), self.pocetmk(), self.pocetmn())

    # ntica vysledna#
    def vysledok_spol(self):
        return (self.vyratajd(), self.vyrataji(), self.vyratajs(), self.vyratajk(), self.vyratajn())

    def vyhodnotenie(self):
        self.d= self.vyratajd()
        self.i= self.vyrataji()
        self.s= self.vyratajs()
        self.k= self.vyratajk()
        self.ukazovatel = ()

        # tri cisla
        if self.d >= 1 and self.i >= 0 and self.s >= -1 and self.k < -2:
            print(123)
            self.ukazovatel = "123"
        elif self.d >= 1 and self.i >= 0 and self.s < -1 and self.k >= -2:
            print (124)
            self.ukazovatel = "124"
        elif self.d >= 1 and self.i < 0 and self.s >= -1 and self.k >= -2:
            print(134)
            self.ukazovatel = "134"
        elif self.d < 1 and self.i >= 0 and self.s >= -1 and self.k >= -2:
            print(234)
            self.ukazovatel = "234"

        # dve cisla s rovnakou poziciou
        elif self.d == 4 and self.i == 1 and self.s < 0 and self.k < -2 or self.d == 5 and self.i == 2 and self.s < 0 and self.k < -2 or self.d == 6 and self.i == 3 and self.s < 0 and self.k < -2 or self.d == 9 and self.i == 5 and self.s < 0 and self.k < -2 or self.d == 10 and self.i == 6 and self.s < 0 and self.k < -2 or self.d == 14 and self.i == 8 and self.s < 0 and self.k < -2 or self.d == 15 and self.i == 9 and self.s < 0 and self.k < -2 or self.d == 16 and self.i == 10 and self.s < 0 and self.k < -2 or self.d == 21 and self.i == 17 and self.s < 0 and self.k < -2:
            print(12)
            self.ukazovatel = "12"

        elif self.d == 4 and self.i < 0 and self.s == 0 and self.k < -2 or self.d == 5 and self.i <0 and self.s == 1 and self.k < -2 or self.d == 6 and self.i <0 and self.s == 2 and self.k < -2 or self.d == 7 and self.i <0 and self.s == 3 and self.k < -2 or self.d == 8 and self.i <0 and self.s == 4 and self.k < -2 or self.d == 9 and self.i <0 and self.s == 5 and self.k < -2 or self.d == 10 and self.i <0 and self.s == 7 and self.k < -2 or self.d == 13 and self.i <0 and self.s == 8 and self.k < -2 or self.d == 14 and self.i <0 and self.s == 9 and self.k < -2 or self.d == 15 and self.i <0 and self.s == 10 and self.k < -2 or self.d == 16 and self.i <0 and self.s == 11 and self.k < -2 or self.d == 21 and self.i <0 and self.s == 19 and self.k < -2 :
            print(13)
            self.ukazovatel = "13"

        elif self.d == 4 and self.i < 0 and self.s < -1 and self.k == -1 or self.d == 5 and self.i < 0 and self.s < -1 and self.k == 0 or self.d == 8 and self.i < 0 and self.s < -1 and self.k == 2 or self.d == 9 and self.i < 0 and self.s < -1 and self.k == 3 or self.d == 13 and self.i < 0 and self.s < -1 and self.k == 5 or self.d == 4 and self.i < 0 and self.s < -1 and self.k == 6 or self.d == 15 and self.i < 0 and self.s < -1 and self.k == 7 or self.d == 16 and self.i < 0 and self.s < -1 and self.k == 8 or self.d == 21 and self.i < 0 and self.s < -1 and self.k == 15:
            print(14)
            self.ukazovatel = "14"

        elif self.d <1 and self.i == 0 and self. s == -1 and self.k < -2 or self.d <1 and self.i == 1 and self. s == 0 and self.k < -2 or self.d <1 and self.i == 2 and self. s == 1 and self.k < -2 or self.d <1 and self.i == 3 and self. s == 2 and self.k < -2 or self.d <1 and self.i == 5 and self. s == 5 and self.k < -2 or self.d <1 and self.i == 6 and self. s == 7 and self.k < -2 or self.d <1 and self.i == 7 and self. s == 8 and self.k < -2 or self.d <1 and self.i == 8 and self. s == 9 and self.k < -2 or self.d <1 and self.i == 9 and self. s == 10 and self.k < -2 or self.d <1 and self.i == 10 and self. s == 11 and self.k < -2 or self.d <1 and self.i == 17 and self. s == 19 and self.k < -2:
            print(23)
            self.ukazovatel = "23"

        elif self.d <1 and self.i == 0 and self. s < -1 and self.k == -2 or self.d <1 and self.i == 1 and self. s < -1 and self.k == -1 or self.d <1 and self.i == 2 and self. s < -1 and self.k == 0 or self.d <1 and self.i == 5 and self. s < -1 and self.k == 3 or self.d <1 and self.i == 8 and self. s < -1 and self.k == 6 or self.d <1 and self.i == 9 and self. s < -1 and self.k == 7 or self.d <1 and self.i == 10 and self. s < -1 and self.k == 8 or self.d <1 and self.i == 17 and self. s < -1 and self.k == 15:
            print(24)
            self.ukazovatel = "24"

        elif self.d <1 and self.i< 0 and self.s == -1 and self.k == -2 or self.d <1 and self.i< 0 and self.s == 0 and self.k == -1 or self.d <1 and self.i< 0 and self.s == 1 and self.k == 0 or self.d <1 and self.i< 0 and self.s == 4 and self.k == 2 or self.d <1 and self.i< 0 and self.s == 5 and self.k == 3 or self.d <1 and self.i< 0 and self.s == 9 and self.k == 6 or self.d <1 and self.i< 0 and self.s == 10 and self.k == 7 or self.d <1 and self.i< 0 and self.s == 11 and self.k == 8 or self.d <1 and self.i< 0 and self.s == 19 and self.k == 15 :
            print(34)
            self.ukazovatel = "34"

        # jedno cislo
        elif self.d >= 1 and self.i < 0 and self.s < -1 and self.k < -2:
            print(1)
            self.ukazovatel = "1"
        elif self.i >= 0 and self.d < 1 and self.s < -1 and self.k < -2:
            print(2)
            self.ukazovatel = "2"
        elif self.s >= -1 and self.i < 0 and self.d < 1 and self.k < -2:
            print(3)
            self.ukazovatel = "3"
        elif self.k >= -2 and self.d < 1 and self.i < 0 and self.s < -1:
            print(4)
            self.ukazovatel = "4"

        #vsetky
        elif self.d >= 1 and self.i >= 0 and self.s >= -1 and self.k >= -2:
            self.ukazovatel = "zle urobeny test"

        #dve cisla
        else:
            self.dve()

    def dve(self):
        if self.d < 1:
            self.d_hodnota = 0
        elif self.d == 1:
            self.d_hodnota = 1
        elif self.d == 2 or self.d == 3:
            self.d_hodnota = 2
        elif self.d == 4:
            self.d_hodnota = 3
        elif self.d == 5:
            self.d_hodnota = 4
        elif self.d == 6:
            self.d_hodnota = 5
        elif self.d == 7:
            self.d_hodnota = 6
        elif self.d == 8:
            self.d_hodnota = 7
        elif self.d == 9:
            self.d_hodnota = 8
        elif self.d == 10:
            self.d_hodnota = 9
        elif self.d == 11 or self.d == 12:
            self.d_hodnota = 10
        elif self.d == 13:
            self.d_hodnota = 11
        elif self.d == 14:
            self.d_hodnota = 12
        elif self.d == 15:
            self.d_hodnota = 13
        elif self.d == 16:
            self.d_hodnota = 14
        elif self.d > 16:
            self.d_hodnota = 15

        # i
        if self.i < 0:
            self.i_hodnota = 0
        elif self.i == 0:
            self.i_hodnota = 1
        elif self.i == 1:
            self.i_hodnota = 3
        elif self.i == 2:
            self.i_hodnota = 4
        elif self.i == 3:
            self.i_hodnota = 5
        elif self.i == 4:
            self.i_hodnota = 7
        elif self.i == 5:
            self.i_hodnota = 8
        elif self.i == 6:
            self.i_hodnota = 9
        elif self.i == 7:
            self.i_hodnota = 11
        elif self.i == 8:
            self.i_hodnota = 12
        elif self.i == 9:
            self.i_hodnota = 13
        elif self.i == 10:
            self.i_hodnota = 14
        elif self.i > 10:
            self.i_hodnota = 15
        # s
        if self.s < -1:
            self.s_hodnota = 0
        elif self.s == -1:
            self.s_hodnota = 1
        elif self.s == 0:
            self.s_hodnota = 3
        elif self.s == 1:
            self.s_hodnota = 4
        elif self.s == 2:
            self.s_hodnota = 5
        elif self.s == 3:
            self.s_hodnota = 6
        elif self.s == 4:
            self.s_hodnota = 7
        elif self.s == 5:
            self.s_hodnota = 8
        elif self.s == 6 or self.s == 7:
            self.s_hodnota = 9
        elif self.s == 8:
            self.s_hodnota = 11
        elif self.s == 9:
            self.s_hodnota = 12
        elif self.s == 10:
            self.s_hodnota = 13
        elif self.s == 11:
            self.s_hodnota = 14
        elif self.s > 11:
            self.s_hodnota = 15

        # k
        if self.k < -2:
            self.k_hodnota = 0
        elif self.k == -2:
            self.k_hodnota = 1
        elif self.k == -1:
            self.k_hodnota = 3
        elif self.k == 0:
            self.k_hodnota = 4
        elif self.k == 1:
            self.k_hodnota = 6
        elif self.k == 2:
            self.k_hodnota = 7
        elif self.k == 3:
            self.k_hodnota = 8
        elif self.k == 4:
            self.k_hodnota = 10
        elif self.k == 5:
            self.k_hodnota = 11
        elif self.k == 6:
            self.k_hodnota = 12
        elif self.k == 7:
            self.k_hodnota = 13
        elif self.k == 8:
            self.k_hodnota = 14
        elif self.k > 8:
            self.k_hodnota = 15

        self.d_dvojica = (self.d_hodnota, self.d)
        self.i_dvojica = (self.i_hodnota, self.i)
        self.s_dvojica = (self.s_hodnota, self.s)
        self.k_dvojica = (self.k_hodnota, self.k)

        print(self.d_dvojica, self.i_dvojica, self.s_dvojica, self.k_dvojica, )

        if self.d_dvojica[0] > self.i_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("12")
            self.ukazovatel = "12"
        elif self.d_dvojica[0] > self.s_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("13")
            self.ukazovatel = "13"
        elif self.d_dvojica[0] > self.k_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("14")
            self.ukazovatel = "14"

        elif self.i_dvojica[0] > self.d_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("21")
            self.ukazovatel = "21"
        elif self.i_dvojica[0] > self.s_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("23")
            self.ukazovatel = "23"
        elif self.i_dvojica[0] > self.k_dvojica[0] != 0 and self.s_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("24")
            self.ukazovatel = "24"

        elif self.s_dvojica[0] > self.d_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("31")
            self.ukazovatel = "31"
        elif self.s_dvojica[0] > self.i_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.k_dvojica[0] == 0:
            print("32")
            self.ukazovatel = "32"
        elif self.s_dvojica[0] > self.k_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("34")
            self.ukazovatel = "34"

        elif self.k_dvojica[0] > self.d_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("41")
            self.ukazovatel = "41"
        elif self.k_dvojica[0] > self.i_dvojica[0] != 0 and self.d_dvojica[0] == 0 and self.s_dvojica[0] == 0:
            print("42")
            self.ukazovatel = "42"
        elif self.k_dvojica[0] > self.s_dvojica[0] != 0 and self.i_dvojica[0] == 0 and self.d_dvojica[0] == 0:
            print("43")
            self.ukazovatel = "43"

    @staticmethod
    def get_date():
        return str(datetime.datetime.now())

    def zapis_test(self):
        with open("testy.txt", "r") as p:
            load = p.read()
        with open("testy.txt", "w") as p:
            p.write(load)
            p.write(self.testovatel +";"+ self.ukazovatel+";"+ self.get_date() )

class TestScreenV(Screen):
    snackbar = None
    help_dialog_m = None
    help_dialog_v = None
    p = 0
    user = test("test1")

    def show_HelpDialogM(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialog)
        self.help_dialog_m = MDDialog(title="Niečo nieje v poriadku", text="Pri odpovediach si vynechal niektorú otázku. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_m.open()

    def show_HelpDialogV(self):
        ok_button = MDRaisedButton(text= "Skontroluj si test",on_release=self.close_help_dialog)
        self.help_dialog_v = MDDialog(title="Niečo nieje v poriadku", text="Pri odpovediach si zaškrtol viac možností ako je potreba. ",
                              size_hint=[0.9, None], auto_dismiss=False,
                              buttons=[ok_button])
        self.help_dialog_v.open()

    def close_help_dialog(self,obj):
        self.help_dialog_m.dismiss()
    def close_help_dialog(self,obj):
        self.help_dialog_v.dismiss()

    def d_plus(self):
        self.user.test_v += ('d',)

    def i_plus(self):
        self.user.test_v += ('i',)

    def s_plus(self):
        self.user.test_v +=('s',)

    def k_plus(self):
        self.user.test_v +=('k',)

    def n_plus(self):
        self.user.test_v +=('n',)

    def d(self):
        self.user.test_m +=('d',)

    def i(self):
        self.user.test_m +=('i',)

    def s(self):
        self.user.test_m +=('s',)

    def k(self):
        self.user.test_m +=('k',)

    def n(self):
        self.user.test_m +=('n',)


    def vyhodnot(self):
        print("Výsledok pre test V  ", self.user.vysledok_v())
        print("list je", self.user.test_v)
        print("Výsledok pre test M  ", self.user.vysledok_m())
        print("list je", self.user.test_m)
        print("Spoločný Výsledok   ", self.user.vysledok_spol())
        print(self.user.vyhodnotenie())

    def show_example_snackbar(self):
        self.snackbar = Snackbar(text="Ukončiť test?",
                                    snackbar_x="10dp",
                                    snackbar_y="10dp",
                                 bg_color= (0.96,0.79,0.09, 1),)
        self.snackbar.size_hint_x = ( Window.width -
                                      (self.snackbar.snackbar_x * 2)) / Window.width
        self.snackbar.buttons = [MDFlatButton(text="Áno",text_color=(1, 1, 1, 1),
                                              on_release=self.evaluate),]
        self.snackbar.open()

    def evaluate (self,obj):
        self.manager.current= "history"
        self.manager.transition.direction = 'left'

    def plus(self):
        self.p = self.p +2.08
        self.ids.progress.value = self.p

class MyGoalsScreen (Screen):

    def on_enter(self):
        file= open("goals.txt" , "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel.text = load_file

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class GoalsScreen(Screen):
    model = ObjectProperty (None)
    ciel1= ObjectProperty(None)
    ciel2 = ObjectProperty(None)
    ciel3 = ObjectProperty(None)
    ciel4 = ObjectProperty(None)
    ciel5 = ObjectProperty(None)
    ciel6 = ObjectProperty(None)
    ciel7 = ObjectProperty(None)
    ciel8 = ObjectProperty(None)
    ciel9 = ObjectProperty(None)
    ciel10 = ObjectProperty(None)
    ciel11 = ObjectProperty(None)

    def add_goals(self):
        if self.ids.model.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Model správania: "+ self.ids.model.text + "\n")

        if self.ids.ciel1.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Kde a ako môžem využiť svoje prednosti: "+ self.ids.ciel1.text +"\n" )

        if self.ids.ciel2.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Rozvíjať sa môžem: "+ self.ids.ciel2.text +"\n" )

        if self.ids.ciel3.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Zistil som o sebe: "+ self.ids.ciel3.text +"\n" )

        if self.ids.ciel4.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako vytvorím pre mňa motivujúce prostredie: "+ self.ids.ciel4.text +"\n" )

        if self.ids.ciel5.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Mojími prednosťami pomôžem tímu: " + self.ids.ciel5.text + "\n")

        if self.ids.ciel6.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako viem zvíšiť efektivitu a postoj k úlohám: " + self.ids.ciel6.text + "\n")

        if self.ids.ciel7.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo zvážiť pri jednaní s inými: " + self.ids.ciel7.text + "\n")

        if self.ids.ciel8.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo je na mne atraktívne: " + self.ids.ciel8.text + "\n")

        if self.ids.ciel9.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Ako viem vytvoriť príjemnejšie prostredie: " + self.ids.ciel9.text + "\n")

        if self.ids.ciel10.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Kroky: " + self.ids.ciel10.text + "\n")

        if self.ids.ciel11.text != "":
            with open("goals.txt", "r") as p:
                load = p.read()
            with open("goals.txt", "w") as p:
                p.write(load)
                p.write("Čo pre to musím urobiť: " + self.ids.ciel11.text + "\n")

    def show_smart(self):
        self.smart_dialog = MDDialog(title="Technika SMART", text="Je jednou z pomôcok pre dobré definovanie cieľa \n"
                                                                "Tvoj cieľ musí byť: \n\n"
                                                                 "S- špecifický, pretože musíme vedieť čo\n"
                                                                 "M- merateľný, aby sme vedeli definovať pokrok\n"
                                                                 "A- akceptovaný, pre istotu, že všetic relevantí vedia a súhlasia\n"
                                                                 "R- realistický, aby bolo jasné, že stojíme nohami na zemi\n"
                                                                 "T- termínovaný, určený do kedy má byť splnený\n"
                                                                 "\n\n"
                                                                 "Mal by zodpovedať tieto otázky:\n\n"
                                                                 "- Čo potrebuje zmenu?\n"
                                                                 "- Aká zmena je potrebná?\n"
                                                                 "- Na koho je zmena zameraná?\n"
                                                                 "- Kde sa zmena uplatní?\n"
                                                                 "- Kedy sa zmena uplatní?\n",
                                   size_hint=[0.8, None], auto_dismiss=True,)
        self.smart_dialog.open()

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"



class HistoryScreen(Screen):
    custom_sheet = None

    def on_enter(self):
        file = open("testy.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
            self.ids.mylabel2.add_widget(
                ThreeLineAvatarListItem(text="Test: " + line[0:5], secondary_text="Ukazovatel: " ,
                                        tertiary_text=" " ))

        file.close()

        file = open("testy.txt", "r")
        load_file = ""
        for line in file:
            load_file = load_file + line
        file.close()
        self.ids.mylabel3.text = load_file

    def show_bottom_sheet(self):
        bs = MDListBottomSheet()
        bs.add_item("Model správania", lambda x: x,icon='account-group-outline')

        for y in 1, 2, 3, 4, 12, 13, 14, 21, 23, 24, 31, 32, 34, 41, 42, 43, 123, 124, 134, 234:
            bs.add_item(f"Ukazovateľ {y} ", partial(self.behavior, y), icon='account-group-outline')
            bs.open()

    def behavior(self, x, instance):
        self.manager.current = str(x)

    def main_navigate(self, button):
        if button.icon == "home":
            self.manager.current = "home"
        elif button.icon == "lightning-bolt":
            self.manager.current = "mygoals"
        elif button.icon == "notebook":
            self.manager.current = "history"

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"

        screen = Builder.load_string(screen_helper)
        return screen

MainApp().run()
