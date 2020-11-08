# Final report portal screen linked to home screen with navigation drawer
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.toast import toast
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
from kivymd.uix.taptargetview import MDTapTargetView
import helpers
import os
import re
finalpath=""
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

Window.size = (300, 500)

navigation_helper = """
Screen:
    id: home
    name: 'home'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "HOME"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:
                    DrawerList:
                        id: features
                        MDList:
                            OneLineIconListItem:
                                text: "Conversational Analyser"
                                on_release: root.manager.current = 'conv_upload'
                                IconLeftWidget:
                                    icon: "chat-processing"
                                    on_release: root.manager.current = 'conv_upload'

                            OneLineIconListItem:
                                text: "Stats"
                                on_release: root.manager.current = 'news_home'
                                IconLeftWidget:
                                    icon: "chart-line"
                                    on_release: root.manager.current = 'news_home'

                            OneLineIconListItem:
                                text: "Report Portal"
                                on_release: root.manager.current = 'portal'
                                IconLeftWidget:
                                    icon: "notebook-outline"
                                    on_release: root.manager.current = 'portal'

                    ScrollView:
                    MDBottomNavigation:
                        MDBottomNavigationItem:
                            name: 'contact'
                            icon: 'phone'
                        MDBottomNavigationItem:
                            name: 'query'
                            icon: 'comment-question'
                        MDBottomNavigationItem:
                            name: 'account'
                            icon: 'account'
                        MDBottomNavigationItem:
                            name: 'settings'
                            icon: 'settings'
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                MDLabel:
                    text: "CHAT ANALYSER"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    DrawerList:
                        id: md_list
                        MDList:
                            OneLineIconListItem:
                                text: "How to use"
                                IconLeftWidget:
                                    icon: "help"
                            OneLineIconListItem:
                                text: "FAQ"
                                IconLeftWidget:
                                    icon: "frequently-asked-questions"
                            OneLineIconListItem:
                                text: "About this app"
                                IconLeftWidget:
                                    icon: "application"
                            OneLineIconListItem:
                                text: "Privacy policy"
                                IconLeftWidget:
                                    icon: "security"
                            OneLineIconListItem:
                                text: "Logout"
                                IconLeftWidget:
                                    icon: "login"
"""

conv_upload = """
Screen:
    id: conv_upload
    name: 'conv_upload'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Upload File'
            left_action_items: [["alert-circle-outline", lambda x: app.info()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"        
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: app.file_manager_open()
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDRaisedButton:
            text: "NEXT"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .5}
            on_release: root.manager.current = 'conv_home'
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'home'
"""

screen_helper = """
Screen:
    id: portal
    name: 'portal'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Report Portal'
            left_action_items: [["alert-circle-outline", lambda x: app.info()]]
            elevation:10
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'home'
"""

login_helper = """
Screen:
    id: login
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Login'
            elevation:10
        Widget:
        MDTextButton:
            text: 'Click here to sign up'
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            on_press: root.manager.current = 'signup'
        MDBottomAppBar:
            MDToolbar:
                icon: 'kodi'
                type: 'bottom'
"""

signup_helper = """
Screen:
    id: signup
    name: 'signup'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Signup'
            elevation:10
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'kodi'
                type: 'bottom'
"""

newsscraping = """
Screen:
    id: news_home
    name: 'news_home'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'TRENDING ARTICLES ON WOMEN'
                        left_action_items: [['alert-circle-outline', lambda x: app.info4()]]
                        elevation:2
                    MDLabel:
                        text: ""
                        font_style:"H6"
                        halign: "center"
                    MDLabel:
                        text: "Active Social Media Users"
                        halign: "center"
                    MDLabel:
                        text: "3.80"
                        font_style:"H3"
                        halign: "center"
                    MDLabel:
                        text: "BILLION"
                        halign: "center"
                    BoxLayout:
                        orientation: 'horizontal'
                        MDFloatingActionButton:
                            id: button1
                            icon: "plus"
                            pos: 10, 10
                            on_release: app.tap_target_start1()
                    DrawerList:
                        id: features1
                        MDList:
                            OneLineIconListItem:
                                text: "Iraq urged to investigate attacks on women human rights defenders"
                                on_release: root.manager.current = 'news_1'
                                IconLeftWidget:
                                    icon: "square"
                                    on_release: root.manager.current = 'news_1'
                            OneLineIconListItem:
                                text: "Thailand: More than 100 companies pledge to strengthen women’s economic empowerment"
                                on_release: root.manager.current = 'news_2'
                                IconLeftWidget:
                                    icon: "square"
                                    on_release: root.manager.current = 'news_2'
                            OneLineIconListItem:
                                text: "Most countries failing to protect women from COVID-19 economic and social fallout"
                                on_release: root.manager.current = 'news_3'
                                IconLeftWidget:
                                    icon: "square"
                                    on_release: root.manager.current = 'news_3'
                    ScrollView:
                    MDBottomNavigation:
                        MDBottomNavigationItem:
                            name: 'query'
                            icon: 'comment-question'
                        MDBottomNavigationItem:
                            name: 'home'
                            icon: 'home'
                            on_tab_release: root.manager.current = 'home'
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                MDLabel:
                    text: "ARTICLES ON WOMEN"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]
"""

screen_helper4 = """
Screen:
    id: news_1
    name: 'news_1'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Iraq urged to investigate attacks on women human rights defenders'
            left_action_items: [["alert-circle-outline", lambda x: app.info1()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDLabel:
            text: "UN-appointed independent rights experts have urged the Iraqi authorities to investigate the murder of a female human rights defender, and the attempted killing of another, targeted “simply because they are women”."
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"

        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'news_home'
"""
screen_helper5 = """
Screen:
    id: news_2
    name: 'news_2'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Thailand: More than 100 companies pledge to strengthen women’s economic empowerment'
            left_action_items: [["alert-circle-outline", lambda x: app.info2()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDLabel:
            text: "Chief executives of 110 companies in Thailand on Wednesday, have signed up to a new set of UN principles on women’s economic empowerment, pledging to improve gender equality in the boardroom, equal pay for equal work, and safer and more inclusive workplaces."
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"

        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'news_home'
"""

screen_helper6 = """
Screen:
    id: news_3
    name: 'news_3'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Most countries failing to protect women from COVID-19 economic and social fallout'
            left_action_items: [["alert-circle-outline", lambda x: app.info3()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDLabel:       
	        text: "The COVID-19 pandemic is “hitting women hard”, but most nations are failing to provide sufficient social and economic protection for them, the head of the UN gender empowerment agency said on Monday."
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'news_home'
"""

conv_anal = """
Screen:
    id: conv_home
    name: 'conv_home'
    NavigationLayout:
        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'CONVO-LYSER'
                        left_action_items: [['alert-circle-outline', lambda x: app.info4()]]
                        elevation:2
                    MDLabel:
                        text: ""
                        font_style:"H6"
                        halign: "center"

                    MDLabel:
                        text: "272"
                        font_style:"H1"
                        halign: "center"
                    MDLabel:
                        text: "MESSAGES IN TOTAL"
                        halign: "center"
                    BoxLayout:
                        orientation: 'horizontal'
                        MDFloatingActionButton:
                            id: button
                            icon: "plus"
                            pos: 10, 10
                            on_release: app.tap_target_start1()
                    DrawerList:
                        id: features
                        MDList:
                            OneLineIconListItem:
                                text: "SENTIMENT ANALYSIS"
                                on_release: root.manager.current = 'sent'
                                IconLeftWidget:
                                    icon: "chart-pie"
                                    on_release: root.manager.current = 'sent'

                            OneLineIconListItem:
                                text: "EMOTIONAL ANALYSIS"
                                on_release: root.manager.current = 'emo'
                                IconLeftWidget:
                                    icon: "chart-line"
                                    on_release: root.manager.current = 'emo'

                            OneLineIconListItem:
                                text: "ASPECT BASED ANALYSIS"
                                on_release: root.manager.current = 'aspect'
                                IconLeftWidget:
                                    icon: "chart-bar"
                                    on_release: root.manager.current = 'aspect'

                    ScrollView:
                    MDBottomNavigation:

                        MDBottomNavigationItem:
                            name: 'query'
                            icon: 'comment-question'

                        MDBottomNavigationItem:
                            name: 'home'
                            icon: 'home'
                            on_tab_release: root.manager.current = 'home'


        MDNavigationDrawer:
            id: nav_drawer


            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                MDLabel:
                    text: "CONVO-LYSER"


                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "H6"
                    size_hint_y: None
                    height: self.texture_size[1]


"""

screen_helper1 = """
Screen:
    id: sent
    name: 'sent'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'SENTIMENTAL ANALYSIS'
            left_action_items: [["alert-circle-outline", lambda x: app.info1()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"

        MDLabel:
            text: "POSITIVE: 9.98%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "NEGATIVE: 65.3%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "NEUTRAL: 24.7%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'conv_home'


"""
screen_helper2 = """
Screen:
    id: emo
    name: 'emo'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'EMOTIONAL ANALYSIS'
            left_action_items: [["alert-circle-outline", lambda x: app.info2()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDLabel:
            text: "SADNESS: 29%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "JOY: 20%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "FEAR: 10%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "DISGUST: 26%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        MDLabel:
            text: "ANGER: 15%"
            halign: "center"
            font_style: "H5"
            theme_text_color: "Custom"
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'conv_home'


"""

screen_helper3 = """
Screen:
    id: aspect
    name: 'aspect'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'ASPECT BASED ANALYSIS'
            left_action_items: [["alert-circle-outline", lambda x: app.info3()]]
            elevation:10
        MDLabel:
            text: ""
            font_style:"H6"
            halign: "center"
        MDLabel:       
            text: "ART & ENTERTAINMENT"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "HEALTH AND FITNESS"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "SOCIETY"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "EDUCATION"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "HOBBIES & INTERESTS"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "SPORTS"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        MDLabel:
            text: "STYLE & FASHION"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
        Widget:
        MDBottomAppBar:
            MDToolbar:
                icon: 'home'
                type: 'bottom'
                on_action_button: root.manager.current = 'conv_home'


"""


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


sm = ScreenManager()


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"  # "BlueGray"
        self.theme_cls.primary_hue = "500"  # "700"
        self.theme_cls.theme_style = "Light"

        screen = Builder.load_string(login_helper)
        self.lusername = Builder.load_string(helpers.lusername_input)
        self.lpassword = Builder.load_string(helpers.lpassword_input)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.log_show_data
                                       )
        screen.add_widget(self.lusername)
        screen.add_widget(self.lpassword)
        screen.add_widget(button)
        sm.add_widget(screen)

        screen = Builder.load_string(signup_helper)
        self.username = Builder.load_string(helpers.username_input)
        self.mycontact = Builder.load_string(helpers.mycontact_input)
        self.email = Builder.load_string(helpers.email_input)
        self.password = Builder.load_string(helpers.password_input)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.sign_show_data
                                       )

        screen.add_widget(self.username)
        screen.add_widget(self.mycontact)
        screen.add_widget(self.email)
        screen.add_widget(self.password)
        screen.add_widget(button)
        sm.add_widget(screen)

        screen = Builder.load_string(navigation_helper)
        sm.add_widget(screen)

        screen = Builder.load_string(screen_helper)
        self.abusername = Builder.load_string(helpers.abusername_input)
        self.contact = Builder.load_string(helpers.contact_input)
        self.reason = Builder.load_string(helpers.reason_input)
        button = MDRectangleFlatButton(text='Submit',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3},
                                       on_release=self.show_data)
        screen.add_widget(self.abusername)
        screen.add_widget(self.contact)
        screen.add_widget(self.reason)
        screen.add_widget(button)
        sm.add_widget(screen)
        screen = Builder.load_string(newsscraping)
        self.tap_target_view = MDTapTargetView(widget=screen.ids.button1,
                                               title_text="Teens having \nat least 1 social \nmedia profile",
                                               description_text="   75%                  ",

                                               widget_position="center", title_position="right_top",
                                               title_text_size="20sp", outer_radius=250, )
        # self.tap_target_view = MDTapTargetView(widget=screen.ids.button,title_text="USER 2",description_text="154 MESSAGES",widget_position="right", outer_radius=100,)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper1)
        sm.add_widget(screen)
        screen = Builder.load_string(conv_upload)
        sm.add_widget(screen)
        screen = Builder.load_string(conv_anal)
        self.tap_target_view = MDTapTargetView(widget=screen.ids.button, title_text="USER 1      USER 2",
                                               description_text="   118                  154 \nMESSAGES    MESSAGES",
                                               widget_position="center", title_position="right_top",
                                               title_text_size="20sp", outer_radius=250, )
        # self.tap_target_view = MDTapTargetView(widget=screen.ids.button,title_text="USER 2",description_text="154 MESSAGES",widget_position="right", outer_radius=100,)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper1)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper2)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper3)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper4)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper5)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper6)
        sm.add_widget(screen)

        return sm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".txt",".py", "kv"],
        )
    def show_data(self, obj):

        if self.contact.text != "" and self.reason.text != "":
            if len(self.contact.text) == 10 and self.contact.text.isdigit():
                print("ABUSER NAME- " + self.abusername.text)
                print("CONTACT NUMBER- " + self.contact.text)
                print("REASON- " + self.reason.text)
                # self.reason.text, self.contact.text, self.username.text = ""
                self.abusername.text = ""
                self.contact.text = ""
                self.reason.text = ""
                user_error = "Your response has been noted. The immediate responders will contact you soon."
            else:
                user_error = "Please enter a valid contact number."
        else:
            user_error = "Please enter the required fields"
        self.dialog = MDDialog(
            text=user_error, size_hint=(0.8, 1),
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog

    def info(self):
        self.dialog = MDDialog(
            text='The information entered below will be forwarded to the respective authorities.', size_hint=(0.8, 1),
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def log_show_data(self, obj):
        if self.lusername.text != "" and self.lpassword.text != "":
            if len(self.lpassword.text) >= 8:
                sm.switch_to(Builder.load_string(navigation_helper))
            else:
                user_error = "Incorrect password. Please try again"
                self.dialog = MDDialog(
                    text=user_error, size_hint=(0.8, 1),
                    buttons=[MDFlatButton(text='Close', on_release=self.close_dialog), ]
                )

                self.dialog.open()



        else:
            user_error = "Please enter the required details"
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.8, 1),
                buttons=[MDFlatButton(text='Close', on_release=self.close_dialog), ]
            )

            self.dialog.open()

    def close_dialog1(self, obj):
        self.dialog.dismiss()

        # do stuff after closing the dialog

    def sign_show_data(self, obj):

        if self.username.text != "" and self.mycontact.text != "" and self.email.text != "" and self.password.text != "":
            if len(self.mycontact.text) == 10 and self.mycontact.text.isdigit():
                if re.search(regex, self.email.text):
                    if len(self.password.text) >= 8:

                        print("USERNAME- " + self.username.text)
                        print("CONTACT NUMBER- " + self.mycontact.text)
                        print("EMAIL- " + self.email.text)
                        print("PASSWORD- " + self.password.text)
                        # self.reason.text, self.contact.text, self.username.text = ""
                        self.username.text = ""
                        self.mycontact.text = ""
                        self.email.text = ""
                        user_error = ""
                    else:
                        user_error = "Please enter a valid password"
                else:
                    user_error = "Please enter a valid email id"
            else:
                user_error = "Please enter a valid contact number."


        else:
            user_error = "Please enter the required fields"
        if user_error == "":
            sm.switch_to(Builder.load_string(navigation_helper))
        else:
            self.dialog = MDDialog(
                text=user_error, size_hint=(0.8, 1),
                buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
            )
            self.dialog.open()

    def tap_target_start1(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

    def tap_target_start2(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

    def info1(self):
        self.dialog = MDDialog(
            text='Sentimental Analysis displays the polarity ie. positive, negative and neutral polarity values of the whole conversation',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info2(self):
        self.dialog = MDDialog(
            text='Emotional Analysis displays the various emotions and their value of the whole conversation',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info3(self):
        self.dialog = MDDialog(
            text='Aspect Based Analysis displays the most talked category of the whole conversation',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info4(self):
        self.dialog = MDDialog(
            text='Analysis on emotions and tones of conversations and visualise the results in the form of graphs.',
            size_hint=(1, 0), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def callback(self, instance):
        print("Button is pressed")
        print('The button % s state is <%s>' % (instance, instance.state))

    def file_manager_open(self):
        self.file_manager.show('/')  # output manager to the screen
        self.file_manager.use_access = True
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        self.exit_manager()

       global finalpath
        punc = '''/~$%^'''
        #remove '/' from the path
        for ele in path:
            if ele in punc:
                path1 = path.replace(ele, "")
        #path1 -> '/' symbol removed filepath  /Users\HP\Desktop\exconvo.txt to Users\HP\Desktop\exconvo.txt

        tmplist = path1.split(os.sep)
        #splits the path and is put in the list tmplist
        #Users\HP\Desktop\exconvo.txt to ['Users','HP','Desktop','exconvo.txt']

        #print(tmplist)
        finalpath=""
        for wrd in tmplist:
            finalpath = finalpath+r"\\"+wrd
        finalpath="C:"+finalpath
        #print(finalpath)   #C:\\Users\HP\Desktop\exconvo.txt
        with open(finalpath, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            lines = (line.split(",") for line in stripped if line)

            with open('C:\\Users\\HP\\Desktop\\convo.csv', 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                writer.writerow(('name', 'msg'))
                writer.writerows(lines)

        toast(finalpath)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


DemoApp().run()
