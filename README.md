# kivy ile araba kontrolu | control car with kivy
Python kivy kullanarak geliştirdiğimiz ara yüzde aynı ağda bulundunan ve içinde 'gorev_bilgisayari' klasöründe bulunan kod çalışan arabayı uzaktan kontrolunu sağladık. Bu kontrol için araba içindeki bilgisayarda bir flask server ve onu yönettiği bir sqlite veri tabanı kurduk. Telefonda çalışacak olan kontrol programında ise kivynin etiket sistemiyle  bir .kv dosyası oluşturarak ara yüz geliştirdik ardından ara yüzü python'a dahil ederek fonksiyonlarını yazdık. Ara yüzde araça ip adresi ile bağlanıp ondan görüntü aldık ve butonlar ile kontrolunu sağlıyoruz.
   
In the interface we developed using python kivy, we provided remote control of the car, which is on the same network and running the code in the 'gorev_bilgisayari' folder. For this control, we set up a flask server on the computer in the car and an sqlite database that it manages. In the control program that will run on the phone, we developed an interface by creating a .kv file with kivy's tag system, then we included the interface in python and wrote its functions. In the interface, we connect to the vehicle with the ip address, get an image from it and control it with the buttons.
