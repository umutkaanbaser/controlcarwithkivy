from utils.usefull_funcs import istek_gonder,url_kontrol
import requests
import base64
from threading import Thread

class carDriving():
    baglanti=""
    surus=""
    host=""
    kamera_acik=False
   
    def kamera_kontrol(self,*args):
        if(self.kamera_acik):
            try:
                istek = requests.get(f"{self.host}video_feed")
                txt = istek.text
                jpg_original = base64.b64decode(txt)
                filename = 'img/yaz.png'

                with open(filename, 'wb') as f:
                    f.write(jpg_original)

                self.pen4.ids.kamera.source=filename
                self.pen4.ids.kamera.reload()
            except Exception as e:
                print("Kamera hatası:",e)
    
    def ip_adres_kontrol(self):
        metin=self.show.ids.ip_text.text
        boy = metin.split(".")
        if(len(boy)>4):
            self.show.ids.label_deneme.text="4 sayi dan fazla girmeyiniz"
        elif(len(boy)<4):
            self.show.ids.label_deneme.text="4 sayi dan az girmeyiniz"
        elif(len(boy)==4):
            self.show.ids.label_deneme.text="İp adresi kontrol ediliyor"
            url_th = Thread(target=url_kontrol,args=(metin,self))
            url_th.start()
            
    def otonom_iptal(self):
        url=f"{self.host}stopotonom"
        print("otonom iptal ediliyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("edildi---")
        else:
            print("edilemedi!")
        self.pen.remove_widget(self.pen_oto)
        self.pen.add_widget(self.pen3)

    def ileri_git(self):
        self.pen4.ids.kamera.reload()
        url=f"{self.host}setileri"
        print("ileri gidiliyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("ileri gidildi")
        else:
            print("ileri gidilemedi")
    
    def geri_git(self):
        url=f"{self.host}setgeri"
        print("geri gidiliyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("geri gidildi")
        else:
            print("geri gidilemedi")
    
    def saga_git(self):
        url=f"{self.host}setsag"
        print("saga gidiliyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("saga gidildi")
        else:
            print("saga gidilemedi")
    
    def sola_git(self):
        url=f"{self.host}setsol"
        print("sola gidiliyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("sola gidildi")
        else:
            print("sola gidilemedi")
    
    def capala(self):
        url=f"{self.host}setcapala"
        print("capalanıyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("capalanıyor---")
        else:
            print("capalanamadı!")
    
    def durdur(self):
        url=f"{self.host}setdurdur"
        print("capalama durduluyor")
        sonuc = istek_gonder(url)
        if(sonuc):
            print("Durdurulurdu")
        else:
            print("Durdurulamadı")
