import kivy
kivy.require("1.9.0")
from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'multisamples', '0')

from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.popup import Popup

from windows.win1 import pencere1
from windows.win3 import pencere3
from windows.win4 import pencere4
from windows.win_otonom import pencereotonom
from windows.win_main import Anaui
from windows.popups import Popups

from utils.usefull_funcs import *
from utils.drive_car import carDriving

adres="http://adres.com/"

class mainApp(App,carDriving):
    
    def secim_yap_manuel(self,secim):
        self.surus=secim
        print("secim:",secim)
        self.pen.remove_widget(self.pen3)
        if(secim=="otonom"):
            self.pen.add_widget(self.pen_oto)
            url=f"{self.host}setotonom"
            print("otonom baslatılıyor")
            sonuc = istek_gonder(url)
            if(sonuc):
                print("baslatıldı---")
            else:
                print("baslatılamadı!")
        else:
            self.popup_ac()
            Clock.schedule_interval(self.kamera_kontrol,0.07)
            self.pen.add_widget(self.pen4)
      
    def popup_ac(self):
        self.show = Popups()
        self.popupWindow = Popup(title="Robotun ip adresini giriniz",content=self.show,size_hint=(0.8,0.3),auto_dismiss=False)#size=(200,200)
        self.popupWindow.open()
    
    def pen_degis(self):
        self.pen.remove_widget(self.pen1)
        self.pen.add_widget(self.pen3)
        
    def build(self):
        Window.size = (414, 716)
        self.pen = Anaui()
        self.pen1 = pencere1()
        self.pen3 = pencere3()
        self.pen4 = pencere4()
        self.pen_oto = pencereotonom()
        self.pen.add_widget(self.pen1)
        Clock.schedule_once(lambda dt: self.pen_degis(), 6)

        return self.pen

if __name__ =="__main__":
    kv = mainApp()
    kv.run()
