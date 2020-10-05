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
newsscraping = """
Screen:
    id: home
    name: 'home'
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
                            id: button
                            icon: "plus"
                            pos: 10, 10
                            on_release: app.tap_target_start1()
                    DrawerList:
                        id: features
                        MDList:
                            OneLineIconListItem:
                                text: "Iraq urged to investigate attacks on women human rights defenders"
                                on_release: root.manager.current = 'sent'
                                IconLeftWidget:
                                    icon: "square"
                                    on_release: root.manager.current = 'sent'
                            OneLineIconListItem:
                                text: "Thailand: More than 100 companies pledge to strengthen women’s economic empowerment"
                                on_release: root.manager.current = 'emo'
                                IconLeftWidget:
                                    icon: "square"
                                    on_release: root.manager.current = 'emo'
                            OneLineIconListItem:
                                text: "Most countries failing to protect women from COVID-19 economic and social fallout"
                                on_release: root.manager.current = 'aspect'
                                IconLeftWidget:
                                    icon: "square"
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
                    text: "ARTICLES ON WOMEN"
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
                on_action_button: root.manager.current = 'home'
"""
screen_helper2 = """
Screen:
    id: emo
    name: 'emo'
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
                on_action_button: root.manager.current = 'home'
"""

screen_helper3 = """
Screen:
    id: aspect
    name: 'aspect'
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
                on_action_button: root.manager.current = 'home'
"""


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


sm = ScreenManager()


class news_scrape(MDApp):

    def build(self):
        screen = Builder.load_string(newsscraping)
        self.tap_target_view = MDTapTargetView(widget=screen.ids.button, title_text="Teens having \nat least 1 social \nmedia profile",
                                               description_text="   75%                  ",

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
            text='2nd October, 2020\nHuman Rights',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info2(self):
        self.dialog = MDDialog(
            text='30th September, 2020\nWomen Empowerment',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info3(self):
        self.dialog = MDDialog(
            text='28th September, 2020\nWomen Safety',
            size_hint=(0.9, 0.5), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def info4(self):
        self.dialog = MDDialog(
            text='This section shows the latest articles on child and women empowerment, abuse, welfare and such obtained from the UN Women Updates.',
            size_hint=(1, 0), radius=[20, 7, 20, 7],
            buttons=[MDFlatButton(text='Close', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def callback(self, instance):
        print("Button is pressed")
        print('The button % s state is <%s>' % (instance, instance.state))


root = news_scrape()
root.run()