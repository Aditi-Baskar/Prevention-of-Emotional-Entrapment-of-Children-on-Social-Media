from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os
from kivymd.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDTextButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
from kivymd.uix.taptargetview import MDTapTargetView

Window.size = (300, 500)
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            s = "YOUR FILE HAS BEEN UPLOADED"
            print(type(s))
            self.text_input.text = stream.read()
            #print(self.text_input.text)
            print(os.path.join(path, filename[0]))
            file = open('C:\\Users\\HP\\Desktop\\exconvo.txt', 'w')
            file.write(self.text_input.text)

        self.dismiss_popup()

class Editor(App):
    def build(self):
        pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()