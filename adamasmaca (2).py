import random
harfler=['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z', 'a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
kelimeler=["FAALİYET","PROBLEM", "MEDYA","MERKEZ", "DAVRANIŞ", "KURTULMAK", "TOPLANMAK","ULUSLARARASI", "DÜŞÜNCE", "TELEFON","TÜRK KAHVESİ","DENİZ","YÜKSELMEK","SENDROM", "MİMAR", "BAYKUŞ","KAĞIT", "BATAKLIK", "KAYIP", "ZAMAN", "BAŞ AĞRISI","SAĞLIKLI", "TEHDİTKAR", "FAVORİ", "CANAVAR","KİMLİK","HASTANE", "GÖRÜNMEZ","HEMŞİRE" ,"DOKTOR", "TREN","DİPLOMATİK", "GÜLÜMSEMEK", "NOKTA", "ÜNLÜ","ERKEK", "KADIN", "PİLOT","BEKLENMEDİK","SAAT","SAYAÇ", "SEÇENEK", "DUVAR SAATİ", "DOĞU","BATI","KUZEY","GÜNEY","KALP","YAYIN", "İLGİSİZ","KALDIRAÇ", "MAĞARA","BUGÜN","ANNE","BABA",  "AMCA","BAYRAMLAŞMAK","SÖYLEMEK","BEKLEMEK", "UZUN ADAM", "DÜNYA", "AZ", "GÖRKEMLİ","SINIF","ÖĞRETMEN", "ŞEKİLSİZ", "GÖZ ATMAK", "SU","BAŞKA", "ALT","ÜST","HAYAT","ZOR","KOLAY"]

genelliste=[]
for kelime in kelimeler:
    analiste=[]
    for harf in kelime:
        icliste=["_{}_".format(harf)]
        analiste.append(icliste)
    genelliste.append(analiste)
yanlis=0
randkelime=random.choice(kelimeler)
first=[]
for char in randkelime:
    last=["_{}_".format("?")]
    first.append(last)
print(f"KELIME {len(randkelime)} KAREKTER: ")
def daragaci(yanlis):
    if yanlis == 0:
        print("o--------\n"
              "|        \n"
              "|        \n"
              "|        \n"
              "|        \n")



    elif yanlis == 1:
        print("o--------\n"
              "|       O\n"
              "|        \n"
              "|        \n"
              "|        \n")
    elif yanlis == 2:
        print("o--------\n"
              "|       O\n"
              "|       |\n"
              "|        \n"
              "|        \n")
    elif yanlis == 3:
        print("o--------\n"
              "|       O\n"
              "|       |\n"
              "|       |\n"
              "|        \n")
    elif yanlis == 4:
        print("o--------\n"
              "|       O\n"
              "|      /|\ \n"
              "|       | \n"
              "|         \n")
    elif yanlis == 5:
        print("o--------\n"
              "|       O\n"
              "|      /|\ \n"
              "|       |\n"
              "|      / \ \n")
        print("randomKelime: {}".format(randkelime))
        exit()
hak=5
while(True):
    for i in first:
        for j in i:
            print(j,end="  ")
    sec=input("Harf tahmini icin 1 kelime icin 2 gir (KALAN HAK SAYISI= {}) ".format(hak))
    
    if sec=="1":
    #for i in first:
        #for j in i:
            #print(j,end="   ")
        index=kelimeler.index(randkelime)
        tahmin=input("Harf gir: ")
        tahmin=tahmin.upper()
        for i in range(len(randkelime)):
            if tahmin==kelimeler[index][i]:
                first[i]=["_{}_".format(tahmin)]
            else:
                hak-=1
                yanlis+=1
                daragaci(yanlis)
                break
    elif sec=="2":
        Ttahmin=input("Kelimeni gir: ")
        Ttahmin=Ttahmin.upper()
        if Ttahmin==randkelime:
            first=genelliste[index]
            yanlis=5
        else:
            hak-=1
            yanlis+=1



