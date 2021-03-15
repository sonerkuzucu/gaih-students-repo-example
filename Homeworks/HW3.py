n = int(input("Kaç Öğrenci Girmek istiyorsunuz :"))
i = 0
passingGrade = 0.0
Notlar ={}
while i < n:
  i += 1
  adi = str(input("Adı Soyadı : "))
  midterm = float(input("Vize Notu : "))
  project = float(input("Proje Notu : "))
  final = float(input("Final Notu : "))
  passingGrade = midterm*0.3 + project*0.3 + final*0.4
  Not = [midterm, project, final, passingGrade]
  Notlar[adi] = Not
isimler = {}
for x, y in Notlar.items():
    isimler[x] = y[-1]

grades = []
for g in isimler.values():
    grades.append(g)
grades.sort(reverse=True)
for r, t in isimler.items():
    print(r.ljust(22, ' '), ": ", "{0:.1f}".format(t))

print("")
print ("Mezuniyet Notları Sıralaması")
for g in grades:
    print("{0:.1f}".format(g))
