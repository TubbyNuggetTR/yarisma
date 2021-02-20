#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!
#Lutfen once oyunu oynayin sonra kaynak kodlara bakin!

import time
#Kodlayan @hevesli.coder & @tubbynugget_tr
print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hayal Et! Kendini hayal dünyasının kollarına bırak ve dünyadan biraz uzaklaş
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
time.sleep(3)
print("\nHayal etmek bir nevi gerçeklikten bir parça uzaklaşmaktır.")
time.sleep(3)
print("\nBu oyunda fikirleriniz, düşünceleriniz ve hareketleriniz kaderinizi etkilemektedir")
time.sleep(3)
print("\nBir sonraki hamleyi hayal ederek ve neler olacağını tahmin ederek oyunda ilerleyebilirsiniz")
time.sleep(3)
print("\nUmarım oynarken eğlenirsiniz. İyi oyunlar!")
time.sleep(3)
print("\nNot: En yüksek kalite için arkaya sevdiğiniz bir müziği açabilirsiniz")
time.sleep(5)
print("""\nKurallar
1- Size verilen seçenekleri kullanın eğer başka bir değer girerseniz oyun biter(Orayı yapamayacağımdan korktum)
2- Eğlenmenize bakın :)
Not: 2 den fazla karakter var""")
#Kodlayan @hevesli.coder & @tubbynugget_tr
time.sleep(7)
print("""

 HIKAYE
""")
time.sleep(3)
print("Arkadaşlarınla gezerken bir mağara gördünüz"
      "\nve merak edip içinde ne var diye girip bakmak istediniz fakat gerekli malzemeleriniz yoktu."
      "\nHerkes evine gitti ve ertesi gün o mağaraya girmek için gerekli malzemeleri toplamaya başladınız.")
time.sleep(7)
print("\n~Ertesi Gün~")
time.sleep(3)
print("Gerekli malzemeleri topladınız.")
time.sleep(3)
print("Malzemeler: Fener, Kraker, Bisküvi, Su, Kek, Bıçak, Şapka")
time.sleep(3)
print("Mağaraya doğru yol aldınız")
time.sleep(3)
print("Mağaranın kapısına geldiniz fakat girişi odunlarla kaplı ne yapacaksın?")

bug = 0

while bug == 0:
    magara = int(input("""
1- Tahtaları kırmaya çalışın
2- Mağaranın başka girişi var mı diye araştırın
Seçimin:"""))

    if(magara == 1):
        time.sleep(2)
        print("\nTahtaları kırmak için malzeme aranıyor.")
        time.sleep(3)
        print("O da ne! Bu uzun kütük işimize yarayabilir")
        bug += 5
    elif(magara == 2):
        time.sleep(2)
        print("\nMağaranın arkasında bir delik var ama çok küçük")
        bug+=2

time.sleep(3)

if(bug==2):
    print("\nBu delik küçük fakat genişletilebilir. Geri mi dönmek istersin devam mı etmek istersin?")
    sec = int(input("\n1- Deliği genişletip buradan gir\n2- Geri Dön\nSeçimin:"))
    if(sec==1):
        bug+=1
    else:
        bug+=3

if (bug == 3):
    print("\nBir taş yardımıyla deliği genişlettiniz"
          " ve içeri doğru ilerliyorsunuz, etraf karanlık olmaya başladı. Feneri açman gerek")
    time.sleep(3)
    print("Fener açılıyor")

if(bug==5):
    print("\nTahtaları kırdınız ve içeri doğru ilerliyorsunuz etraf karanlık olmaya başladı. Feneri açman gerek")
    time.sleep(3)
    print("Fener açılıyor")

time.sleep(3)

print("Oh be önümüz aydınlandı")
time.sleep(3)
print("Yavaş yavaş ilerliyorsunuz.")
time.sleep(2)
print("Her birinizin korkusu gittikçe artıyor fakat merak duygunuz daha ağır basıyor ve ilerliyorsunuz")
time.sleep(5)
print("\nTAK!")
time.sleep(2)
print("\nO ses de neydi? Mağara boş, biz de ses çıkartmadık.")
time.sleep(3)

bug2 = 0
while bug2 == 0:
    secim = int(input("\n1- Sesin nereden geldiğini araştır\n2- Yoluna devam et\nSeçimin:"))
    if(secim==1):
        bug2 += 1

    elif(secim==2):
        time.sleep(3)
        print("\nDümdüz devam ettiniz ve bir şey bulamadınız")
        son_mu = int(input("\n1- Sesi araştır\n2- Mağaradan çık\nSeçimin:"))
        if(son_mu==1):
            bug2+=1
        else:
            print("\n~MAĞARADAN ÇIKILIYOR~")
            time.sleep(2)
            print("\n~MAĞARADAN ÇIKTINIZ~")
            time.sleep(2)
            print("\nHepiniz oturup çantadaki yiyeceklerden yediniz")
            time.sleep(2)
            print("\nEvlerinize gittiniz ve normal şekilde hayatınıza devam ettiniz""\n\nSon")
            exit()
time.sleep(2)
#Kodlayan @hevesli.coder & @tubbynugget_tr
while bug2 == 1:
    print("\nArkadaşlarına sordun ve sol taraftan geldiğini söylediler o tarafa doğru yol alıyorsunuz")
    bug2+=1
time.sleep(4)
print("\nTam da düşündüğüm gibi taşlar devrilmiş. Hatta burda bir giriş var.")
time.sleep(4)
print("\n~MERAKINIZA HAKIM OLAMAYIP ICERI GIRIYORSUNUZ~")
time.sleep(4)
print("\nBurası daha önceden kullanılmış olmalı. Baksanıza masa ve sandalyeler var.")
time.sleep(4)
print("\nANAM! O DA NE! GAZ LAMBASI MI YOKSA. BURASI ÇOK ESKIDEN KULLANILMIŞ OLMALI")
time.sleep(4)

bug3 = 0

while bug3 == 0:
    sence = int(input("\n1- Araştırmaya devam et\n2- Mağaradan çık\nSeçimin:"))
    if(sence==1):
        time.sleep(3)
        print("\nEtrafta bakınırken bir adet kibrit buldun!")
        bug3+=1
    else:
        time.sleep(3)
        print("\n~MAĞARADAN ÇIKILIYOR~")
        time.sleep(2)
        print("\n~MAĞARADAN ÇIKTINIZ~")
        time.sleep(2)
        print("\nHepiniz oturup çantadaki yiyeceklerden yediniz")
        time.sleep(2)
        print("\nEvlerinize gittiniz ve hayatiniza devam ettiniz""\nSon")
        exit()

time.sleep(3)
print("\nBulduğun kibritle gaz lambasını yakmaya çalışıyorsun, fakat yanmıyor.")
time.sleep(2)
print("Baya eski olmalı")
time.sleep(2)

print("Etrafa bakmaya devam ediyorsunuz")
time.sleep(2)

say = 0
while say <= 7:
    print(".")
    time.sleep(1)
    say+=1

time.sleep(2)
print("\n-Bence daha fazla ilerlememeliyiz")
time.sleep(3)
print("\n+Bence de")
time.sleep(3)
print("\n~TAKIR TUKUR SESLER~")
time.sleep(3)
print("\n-AAHHHHHHHH!")
time.sleep(3)
print("-YARDIM EDIN SIKIŞTIM")
time.sleep(3)
print("\n+N-ne oldu Mustafa")
time.sleep(3)
print("\n-TAŞLAR DEVRILINCE ALTINDA KALDIM! BENI KURTARIN NOLUR")
time.sleep(3)
print("-BEN DEMIŞTIM AYRI AYRI GEZMEYELIM DIYE")
time.sleep(3)
print("\n+Tamam, sakin ol geliyoruz")
time.sleep(5)
print("\n~MUSTAFANIN YANINA GELDINIZ~")
time.sleep(3)
print("\n+Dostum çok fena şıkışmışsın")

kurtar = 0

while kurtar <= 1:
    hadi=int(input("\n1- Taşları Mustafa'nın üstünden kaldırın"
                   "\n2- Mustafa'yı kollarından tutup çekmeye çalışın"
                   "\nSeçimin:"))
    if(hadi==1):
        time.sleep(3)
        print("\nTaşlar çok ağır hareket etmiyorlar :(")
        kurtar+=1
    elif(hadi==2):
        time.sleep(3)
        print("\nKollarından çektiniz fakat fena şıkışmış :(")
        kurtar+=1

time.sleep(3)
print("\n-Ne yapacağız")
time.sleep(3)
print("\n+Bilmiyorum :(")
time.sleep(5)
print("\n-Kasabadakileri çağırabiliriz!")
time.sleep(3)
print("\n+Olmaz! Bize kızarlar neden buraya girdiniz diye")
time.sleep(3)
print("\n-BAŞKA SEÇENEĞIMIZ VAR MI DA BOYLE KONUŞUYORSUN!")
time.sleep(3)
print("\n+Bi daha deneyelim")

kurtar = 0

while kurtar <= 1:
    hadi = int(input("\n1- Taşları Mustafa'nın üstünden kaldırın"
                     "\n2- Mustafa'yı kollarından tutup cekmeye çalışın"
                     "\nSeçimin:"))
    if (hadi == 1):
        print("\nTaşlar çok ağır hareket etmiyorlar :(")
        kurtar += 1
    elif (hadi == 2):
        print("\nKollarından çektiniz fakat fena şıkışmış :(")
        kurtar += 1

while kurtar == 2:
    hadi = int(input("\n1- Taşları Mustafa'nın üstünden kaldırın"
                     "\n2- Mustafa'yı kollarından tutup çekmeye çalışın"
                     "\n3- Allah'a dua edin"
                     "\nSeçimin:"))
    if (hadi == 1):
        print("\nTaşlar çok ağır hareket etmiyorlar :(")

    elif (hadi == 2):
        print("\nKollarından çektiniz fakat fena şıkışmış :(")

    elif(hadi==3):
        print("\nAllah'a dua ettiniz ve gaza gelip taşları tekrar oynatmayı denediniz")
        kurtar+=1

time.sleep(3)
print("\n~TAŞ HAREKET ETME SESLERI~")
time.sleep(3)
print("\n-OLEYYYYYYY")
time.sleep(3)
print("\n+Hadi hemen burdan çıkalım")
time.sleep(3)

say = 0
while say <= 5:
    print(".")
    time.sleep(1)
    say+=1

print("\n-Olamaz taşlar yolumuzu kapatmış!")
time.sleep(3)
print("\n+Taşları ittirelim her türlü çıkarız")
time.sleep(3)
print("\n~TAŞLARI İTTİRDİNİZ")
time.sleep(5)
print("\n~ÇIKIŞA DOĞRU KOŞARAK ILERLIYORSUNUZ~")
time.sleep(3)

say = 0

while say <= 2:
    print(".")
    time.sleep(1)
    say+=1
print("\n~ÇIKIŞA ULAŞTINIZ~")
time.sleep(5)
print("\n-Oh be gün ışığı ne güzel!")
time.sleep(3)
print("\n-Ama öğlen olmuş şapkaları takmamız lazım")
time.sleep(1)
print("\n+Şu ağacın altına oturalım mı?")
time.sleep(3)

agac = 0

while agac == 0:
    agac1 = int(input("\n1- Ağacın altına oturun\n2- Eve gidin\nSeçimin:"))
    if(agac1==1):
        agac+=1
    elif(agac1==2):
        agac+=2

while agac == 1:
    print("\nNe yemek istersin?\nHatırlıyorsan en başta çantanıza gerekli şeyler almıştınız")
    time.sleep(1)
    print("\n~Aldığınız Malzemeler: Fener, Kraker, Bisküvi, Su, Kek, Bıçak, Şapka")
    time.sleep(3)
    agacalti = int(input("\n1- Kraker\n2- Bisküvi\n3- Kek\nSeçimin:"))

    if(agacalti==1):
        print("Krakerleri yedikten sonra çok susadım. Bana suyu uzatır mısın kanka")
        agac+=1
        print('Hüüp! Ohh, teşekkür ederim')
    elif(agacalti==2):
        print("Bisküviler susattı. Suyu uzatabilir misin")
        agac+=1
        print('Hüüp! Ohh, teşekkür ederim')
    elif(agacalti==3):
        print("Ulan iyi ki bıçak almışız. Aha şu parça senin kanka. Afiyet olsun :>")
        agac+=1

time.sleep(3)

ev = input("Eve gitmek icin Enter'a basın")

time.sleep(3)

if(ev==""):
    print("Eve doğru yol almaya başladınız")
else:
    print("Mecbur eve gidecen")
    time.sleep(2)
    print("Eve doğru yol almaya başladınız")

time.sleep(3)
print("\n~KASABAYA VARDINIZ~")
time.sleep(2)
print("\nArkadaşlarınla evin önünde oturmak ve konuşmak ister misin?")
time.sleep(1)

iste = int(input("\n1- Kal ve olaylar hakkında konuş\n2- Eve git\nSeçimin:"))
soru = 0

if(iste==1):
    soru+=1
else:
    print("\nArkadaşlarına görüşürüz dedin ve hepiniz evlerinize dağıldınız."
          " O mağara hakkında bi daha hiç konuşmadınız")
    time.sleep(5)
    print('Son')
    exit()

sorular = 0

while sorular <=2:
    if(soru==1):
        print("\nOnlara ne sormak istersin?")
        sor = int(input("\n1- İyi misiniz?"
                        "\n2- Nasıl hissediyorsunuz?"
                        "\n3- Bi daha o mağaraya gidecek miyiz?"
                        "\n(3 soru hakkiniz var)"
                        "\nSeçimin:"))
        if(sor==1):
            print("\n-İyi misiniz?\n+Hepimiz iyiyiz")
            sorular+=1
            time.sleep(3)

        elif(sor==2):
            print("\n-Nasıl hissediyorsunuz?\n+Benim kalbim hala küt küt atiyor")
            sorular+=1
            time.sleep(3)

        elif(sor==3):
            print("\n-Bi daha o mağaraya gidecek miyiz?"
              "\n+Mümkünse bi daha hiç gitmeyelim")
            sorular+=1
            time.sleep(3)

time.sleep(5)
print("\n~AKŞAM EZANI OKUNUR~")
time.sleep(3)
print("\nNeyse arkadaşlar evlere dağılalım bu kadar macera yeter")
time.sleep(2)
print("\n~EVLERE DAĞILDINIZ~")
time.sleep(2)
print("\nEve geldin. Oturuyorsun. Annen çay demlemiş ve poğaça yapmış")
time.sleep(2)
print("\nBaban: Oğlum bugün arkadaşlarınla ne yaptın?")
time.sleep(2)

anlat = int(input("\nBabana mağaradan bahsetmek ister misin?\n1- Evet\n2- Hayır\nSeçimin:"))
anlatti = 0
son = 0
if(anlat==1):
    time.sleep(1)
    print("\nBaba bugün ormanın ordaki mağaraya gittik. Sonra mağaraya girdik...")
    time.sleep(3)
    print("\nIşte böyle bir macera yaşadık")
    time.sleep(2)
    print("\nBaba:\nCidden mi? Bundan seneler önce ben küçükken"
          " arkadaşlarımla oraya gidip oyunlar oynardım."
          "\nHatta oradaki gaz lambasını babaannen vermişti bana orada kullanayım diye")
    time.sleep(10)
    print("\nVay be! Baba, çok güzel ve kocaman bir yer orası")
    time.sleep(5)
    print("\nBaba yarın gidip oraları düzenlesek olur mu?"
          "Ben de arkadaşlarımla orada oynarım")
    time.sleep(2)
    print("\nBaba: Bakarız oğlum :)")
    time.sleep(2)
    anlatti+=1
else:
    time.sleep(1)
    print("\nBir şey olmadı baba öyle gezinip durduk")
    time.sleep(2)
    son+=1
print("\nBaba:\nYorulmuş olmalısın gidip yatmak ister misin")
time.sleep(2)
yat = int(input("\n1- Evet\n2- Hayır\nSeçimin: "))

time.sleep(3)

if(yat==1):
    print("\nBaba: Iyi geceler oğlum")
else:
    print("\nBaba: Tamam sen bilirsin")
    time.sleep(3)
    print("\n~SAAT 22 OLDU VE UYKUN GELDIGI ICIN GIDIP UYUDUN~")

time.sleep(5)
if(anlatti==1):
    print("\n~SABAH OLDU, UYANDIN~")

if(anlatti==0):
    print("\n~SABAH OLDU, UYANDIN~")
    time.sleep(2)
    print("\nBi daha o mağaraya hiç uğramadınız ve orası efsane olarak kaldı")

time.sleep(2)

if(anlatti==1):
    print("\nBabanla gidip mağarada düzenleme yaptiniz"
          " ve orası arkadaşlarınla beraber oynamak için hazır hale geldi! Mutlu Son!")

time.sleep(5)

if(son==0):
    print("Yaramazlık yapsanda doğruyu söylediğin için teşekkür ederim. Sonsuza kadar mutlu olarak yaşa!"
          "\nDoğru çıkışa ulaştın bu hesaba şu şekilde mesaj at '19283746oyun' @hevesli.coder "
          "\nSeni gördüğüm an diğer görevi vereceğim")

if(son==1):
    print("Doğruyu söylemeyi öğrenmelisin."
          "\n Ne kadar kötü bir şey yapmış olsan da anaya babaya doğruyu söylemelisin."
          "\n Bu hareketinden dolayı seni kınıyorum!")

time.sleep(10)

print("""\n\n
----------------------------------------------------------------------------------------
OYUNU OYNADIĞINIZ IÇIN TEŞEKKÜR EDERIM

UMARIM OLAYLARI HAYAL EDEREK OYNAMIŞSINIZDIR YOKSA ÇOK FAZLA BIR ETKI BIRAKTIĞINI DÜŞÜNMÜYORUM

EĞER DOĞRU KARARLAR VERDIYSENIZ MUTLU SONA ULAŞMIŞSINIZDIR

PYTHONU TAM OLARAK BILMIYORUM O YUZDEN BU ŞEKILDE YAPABILDIM EN FAZLA,

DAHA FAZLA BILSEYDIM EMINIM DAHA IYISINI YAPABILIRDIM

Önemli bir kısım: Oyundaki karakterlerin sınırı yok 
siz kaç kişi düşünüp kaç kişiyle oynadıysanız o kadar karakter vardı.
Umarım hayal ederek oynamışsınızdır :)

Not: Yazım yanlışları, mantık hataları, cümleyi yanlış yerde kullanma 
gibi hatalar yapmış olabilirim affola

Not2: Oyunun birden fazla (4) farklı sonu vardır. 
Başka kararlar vererek farklı sonuçlara ulaşabilirsiniz

KODLAYAN @hevesli.coder & @tubbynugget_tr

IKISIDE BENIM HESABIM TAKIP EDERSENIZ SEVINIRIM
----------------------------------------------------------------------------------------
""")

#Kodlayan @hevesli.coder & @tubbynugget_tr