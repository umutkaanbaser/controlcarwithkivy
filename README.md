# kivy ile araba kontrolu | control car with kivy
Python kivy kullanarak geliştirdiğimiz ara yüzde aynı ağda bulundunan ve içinde 'gorev_bilgisayari' klasöründe bulunan kod çalışan arabayı uzaktan kontrolunu sağladık. Bu kontrol için araba içindeki bilgisayarda bir flask server ve onu yönettiği bir sqlite veri tabanı kurduk. Telefonda çalışacak olan kontrol programında ise kivynin etiket sistemiyle  bir .kv dosyası oluşturarak ara yüz geliştirdik ardından ara yüzü python'a dahil ederek fonksiyonlarını yazdık. Ara yüzde araça ip adresi ile bağlanıp ondan görüntü aldık ve butonlar ile kontrolunu sağlıyoruz.
   
In the interface we developed using python kivy, we provided remote control of the car, which is on the same network and running the code in the 'gorev_bilgisayari' folder. For this control, we set up a flask server on the computer in the car and an sqlite database that it manages. In the control program that will run on the phone, we developed an interface by creating a .kv file with kivy's tag system, then we included the interface in python and wrote its functions. In the interface, we connect to the vehicle with the ip address, get an image from it and control it with the buttons.

# Kullanım | Usage
not: unutulmamalıdır ki suan kamera görüntüsü 'webcam_Stream' klasöründe bulunun 'sunucu.py' dosyasından alınmaktadır. Kullanılacak araça ve kameraya göre o kod düzenlenmeli ve 'gorev_bilgisayari' klasorundeki 'sunucu.py' dosyasına eklenmelidir.

note: it should be noted that the current camera image is taken from the 'server.py' file in the 'webcam_Stream' folder. According to the tool and camera to be used, that code should be edited and added to the 'server.py' file in the 'task_computer' folder.

<div style="display:flex;width:100%;">
   <img src="https://github.com/umutkaanbaser/controlcarwithkivy/blob/main/github_images/ekle1.png" width="200" style="margin:auto;"/>
</div>
 şeklinde açılış sayfası sizi karşılar, bu sayfa 3 saniye kadar şirket logosunu ve açıklamayı gösterip gidecektir.
 
 The landing page will greet you, this page will show the company logo and description for about 3 seconds and go.
 
 <div style="display:flex;width:100%;">
   <img src="https://github.com/umutkaanbaser/controlcarwithkivy/blob/main/github_images/ekle2.png" width="200" style="margin:auto;"/>
</div>

ardından size bu soru sorulur ve cevabınıza göre aşağıda ki 2 sayfadan birisi açılır. Otonom'u seçerseniz iptal butonu bulanan bir sayfa açlılır ve araça otonom gitmesini söyler.
Eğer Manuel'ı seçersiniz araçı kamera görüntüsü ile kullanabileceğiniz ekran gelir ve araça bağlanmak için sizden ip adresi bekler.

then you will be asked this question and one of the following 2 pages will open according to your answer. If you choose Autonomous, a page with a cancel button opens and tells the vehicle to drive autonomously.

 <div style="float:left;width:100%;">
   <img src="https://github.com/umutkaanbaser/controlcarwithkivy/blob/main/github_images/ekle3.png" width="200" heigth="100" style="margin:auto;"/>
   <img src="https://github.com/umutkaanbaser/controlcarwithkivy/blob/main/github_images/ekle4.png" width="200" style="margin:auto;"/>
</div>

# Kurulum | installation
 ```
 pip3 install requests  # ==2.28.1
 pip3 install flask # ==2.1.2
 pip3 install opencv-python  #==4.6.0
 
 # kivy kurulum | installation kivy : https://kivy.org/doc/stable-1.10.1/installation/installation-windows.html
 python -m pip install --upgrade pip wheel setuptools
 python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
 python -m pip install kivy.deps.gstreamer
 python -m pip install kivy.deps.angle
 python -m pip install kivy
 ```
 # koşturmak | run 
 ```
 python main.py # apk yada exe haline getirilebilir, you can make apk or exe
 ```
 
