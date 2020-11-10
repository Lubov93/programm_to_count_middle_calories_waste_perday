from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window


Window.size = (480,853)
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')


def get_callories(m):
    wemanmin= str((9.99*50)+(6.25*m)-(4.92*19)-161)
    wemanmax = str((9.99*60)+(6.25*m)-(4.92*19)-161)
    manmin =str((9.99*70)+(6.25*m)-(4.92*19)-161)
    manmax = str((9.99*80)+(6.25*m)-(4.92*19)-161)
    min_active = str(m*1.2)
    return {'wemanmin': wemanmin, 'wemanmax': wemanmax, 'manmin': manmin , 'manmax': manmax, 'min_active': min_active}



class Container(GridLayout):
    def calculate(self):
        try:
            rost = int(self.text_input.text)

        except:
            rost = 0



        callories = get_callories(rost)

        self.wemanmin.text = callories.get('wemanmin')
        self.wemanmax.text = callories.get('wemanmax')
        self.manmin.text = callories.get('manmin')
        self.manmax.text = callories.get('manmax')
        self.min_active.text = callories.get('min_active')





class MyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    MyApp().run()