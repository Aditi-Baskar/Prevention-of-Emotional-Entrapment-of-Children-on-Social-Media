# Final report portal screen linked to home screen with navigation drawer
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
import helpers
import re

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
                                    
                                IconLeftWidget:
                                    icon: "chat-processing"
                                        
                            OneLineIconListItem:
                                text: "Stats"
                                IconLeftWidget:
                                    icon: "chart-line"
                            
                            OneLineIconListItem:
                                text: "Report Portal"
                                IconLeftWidget:
                                    icon: "notebook-outline"
                                
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


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


sm = ScreenManager()


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Teal"  # "BlueGray"
        self.theme_cls.primary_hue = "800"  # "700"
        self.theme_cls.theme_style = "Dark"

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
        return sm

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


DemoApp().run()
