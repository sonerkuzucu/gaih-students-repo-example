#Nested Dictinary kullanarak 5 adet cv kaydını tek bir Dictinary'de topladım.
#Daha sonra içiçe 2 for döngüsü ile biraz da print format kullanarak düzgün bir görsel ile ekrana bastırdım.

#Homework 2

CV = {
  1 : {"Adi": "Ahmet", "Soyadi": "YILMAZ", "Dogum Tarihi": "12.05.1992", "Departman": "Satis", "Pozisyon": "Satis Oncesi", "Yabancı Dil ve Seviye": "ingilizce orta", "Askerli": "Tamamladi"},
  2 : {"Adi": "Ayse", "Soyadi": "TOPAC", "Dogum Tarihi": "02.07.1997", "Departman": "Satis", "Pozisyon": "Satis Temsilcisi", "Yabancı Dil ve Seviye": "ingilizce iyi", "Askerli": "Muaf"},
  3 : {"Adi": "Batu", "Soyadi": "TEKIN", "Dogum Tarihi": "18.11.1989", "Departman": "Teknik", "Pozisyon": "Elektrik Muhendisi", "Yabancı Dil ve Seviye": "Almanca İyi", "Askerli": "Tamamladi"},
  4 : {"Adi": "Tayfun", "Soyadi": "GIDERAYAK", "Dogum Tarihi": "25.08.1991", "Departman": "Teknik", "Pozisyon": "Teknisyen", "Yabancı Dil ve Seviye": "ingilizce az", "Askerli": "2 yıl tecilli"},
  5 : {"Adi": "Ahmet", "Soyadi": "YILMAZ", "Dogum Tarihi": "12.05.1992", "Departman": "Satis", "Pozisyon": "Satis Oncesi", "Yabancı Dil ve Seviye": "ingilizce orta", "Askerli": "Tamamladi"}
    }
for x, y in CV.items():
  print("=".ljust(49, '='))
  print("CV ", x)
  print("_".ljust(49, '_'))
  for k, v in y.items():
    print(k.ljust(22, ' '), ": ", v)

    
   
