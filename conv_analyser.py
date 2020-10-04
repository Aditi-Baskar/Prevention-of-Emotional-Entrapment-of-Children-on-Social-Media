from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.list import MDList
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDTextButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.taptargetview import MDTapTargetView
Window.size = (300, 500)
conv_anal = """
Screen:
    id: home
    name: 'home'
    NavigationLayout:
        ScreenManager:
            Screen:
                
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'CONV. ANALYSER'
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
                on_action_button: root.manager.current = 'home'


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
                on_action_button: root.manager.current = 'home'


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
                on_action_button: root.manager.current = 'home'


"""


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass

sm=ScreenManager()


class conversation_analyser(MDApp):

    def build(self):
        screen = Builder.load_string(conv_anal)
        self.tap_target_view = MDTapTargetView(widget=screen.ids.button,title_text="USER 1      USER 2",description_text="   118                  154 \nMESSAGES    MESSAGES",widget_position="center",title_position="right_top",title_text_size="20sp",outer_radius=250,)
        #self.tap_target_view = MDTapTargetView(widget=screen.ids.button,title_text="USER 2",description_text="154 MESSAGES",widget_position="right", outer_radius=100,)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper1)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper2)
        sm.add_widget(screen)
        screen = Builder.load_string(screen_helper3)
        sm.add_widget(screen)
        return sm

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

    def close_dialog(self, obj):
        self.dialog.dismiss()
        # do stuff after closing the dialog

    def info1(self):
        self.dialog = MDDialog(
            text='Sentimental Analysis displays the polarity ie. positive, negative and neutral polarity values of the whole conversation', size_hint=(0.9, 0.5),radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info2(self):
        self.dialog = MDDialog(
            text='Emotional Analysis displays the various emotions and their value of the whole conversation', size_hint=(0.9, 0.5),radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info3(self):
        self.dialog = MDDialog(
            text='Aspect Based Analysis displays the most talked category of the whole conversation', size_hint=(0.9, 0.5),radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()
    def info4(self):
        self.dialog = MDDialog(
            text='Analysis on emotions and tones of conversations and visualise the results in the form of graphs.', size_hint=(1, 0),radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def callback(self, instance):
        print("Button is pressed")
        print('The button % s state is <%s>' % (instance, instance.state))

root = conversation_analyser()
root.run()
