import requests

def istek_gonder(url):
    try:
        statu=requests.get(url)
        if(statu.status_code==200):
            return True
        else:
            return False
    except:
        return False

def url_kontrol(ip,obje):
    print("deneniyor")
    host = f"http://{ip}:5000/"
    try:
        sonuc = requests.get(host)
        if(sonuc.status_code==200):
            print("başarılı")
            obje.host=host
            obje.kamera_acik=True
            obje.popupWindow.dismiss()

    except:
        obje.show.ids.label_deneme.text="İp adresi geçerli değil"
 