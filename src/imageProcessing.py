#Bilder drehen, zuschneiden und verbessern
from PIL import Image
from PIL import ImageEnhance #Bild verbessern
from PIL import ImageFilter #Filter aufsetzen
from PIL import ImageOps
import os, sys

input = "C:/Users/Frank/Desktop/Lego2/Defekt/JPEG-Bild 2.jpeg" #Dateiname des Bildes
im = Image.open(input)
#size = (450, 450)

#f, e =os.path.splitext(input)
#output = "legodefekt" + ".jpg"
#print(output)

#input1 = "legodefekt.jpg"
#im = Image.open(input)
#width = im.size[0]
#height = im.size[1]
#size = (1000, 1000)

enhancedfarbe = ImageEnhance.Color(im)
enhancedfarbe.enhance(0).save("original.jpg")

input2 = "original.jpg" #Dateiname des Bildes
im = Image.open(input2)
width = im.size[1]
height = im.size[1]
size = (600, 600)
#Abschnitte erstellen

cropbox = (40, 0, 240, 200) #1. Wert = Anfangswert x-Achse, 2. Wert = Anfangswert y-Achse, 3./4. Wert = Ende des Betrachtungsraums
abschnitt = im.crop(cropbox) # Erstellt den Abschnitt

#Speichern des Abschnitts

abschnitt.save("C:/Users/Frank/Desktop/Pics/testbild.jpg")

#Drehung erstellen

rotationList = [Image.ROTATE_90, Image.ROTATE_180, Image.ROTATE_270]

i = 0

for i in rotationList:
    drehung = im.transpose(i)
    drehung.save("C:/Users/Frank/Desktop/Pics/testbild" + str(i) + ".jpg")
    i += 1



"""
drehung90 = im.transpose(Image.ROTATE_90) #Drehung gegen den Uhrzeigersinn um 90 Grad
drehung180 = im.transpose(Image.ROTATE_180) #Drehung gegen den Uhrzeigersinn um 180 Grad
drehung270 = im.transpose(Image.ROTATE_270) #Drehung gegen den Uhrzeigersinn um 270 Grad
spiegelung = im.transpose(Image.FLIP_LEFT_RIGHT) #Spiegelung
umdrehung = im.transpose(Image.FLIP_TOP_BOTTOM) #auf den Kopf gedreht
drehungfrei1 = im.rotate(5) #gewünschte Gradzahl der Drehung eingeben
drehungfrei2 = im.rotate(10) #gewünschte Gradzahl der Drehung eingeben
drehungfrei3 = im.rotate(15) #gewünschte Gradzahl der Drehung eingeben
drehungfrei4 = im.rotate(20) #gewünschte Gradzahl der Drehung eingeben
drehungfrei5 = im.rotate(25) #gewünschte Gradzahl der Drehung eingeben
drehungfrei6 = im.rotate(30) #gewünschte Gradzahl der Drehung eingeben
drehungfrei7 = im.rotate(35) #gewünschte Gradzahl der Drehung eingeben
drehungfrei8 = im.rotate(40) #gewünschte Gradzahl der Drehung eingeben
drehungfrei9 = im.rotate(45) #gewünschte Gradzahl der Drehung eingeben
drehungfrei10 = im.rotate(50) #gewünschte Gradzahl der Drehung eingeben
drehungfrei11 = im.rotate(55) #gewünschte Gradzahl der Drehung eingeben
drehungfrei12 = im.rotate(60) #gewünschte Gradzahl der Drehung eingeben
drehungfrei13 = im.rotate(65) #gewünschte Gradzahl der Drehung eingeben
drehungfrei14 = im.rotate(70) #gewünschte Gradzahl der Drehung eingeben
drehungfrei15 = im.rotate(75) #gewünschte Gradzahl der Drehung eingeben
drehungfrei16 = im.rotate(80) #gewünschte Gradzahl der Drehung eingeben
drehungfrei17 = im.rotate(85) #gewünschte Gradzahl der Drehung eingeben
drehungfrei18 = im.rotate(95) #gewünschte Gradzahl der Drehung eingeben
drehungfrei19 = im.rotate(100) #gewünschte Gradzahl der Drehung eingeben
drehungfrei20 = im.rotate(105) #gewünschte Gradzahl der Drehung eingeben
drehungfrei21 = im.rotate(110) #gewünschte Gradzahl der Drehung eingeben
drehungfrei22 = im.rotate(115) #gewünschte Gradzahl der Drehung eingeben
drehungfrei23 = im.rotate(120) #gewünschte Gradzahl der Drehung eingeben
drehungfrei24 = im.rotate(125) #gewünschte Gradzahl der Drehung eingeben
drehungfrei25 = im.rotate(130) #gewünschte Gradzahl der Drehung eingeben
drehungfrei26 = im.rotate(135) #gewünschte Gradzahl der Drehung eingeben
drehungfrei27 = im.rotate(140) #gewünschte Gradzahl der Drehung eingeben
drehungfrei28 = im.rotate(145) #gewünschte Gradzahl der Drehung eingeben
drehungfrei29 = im.rotate(150) #gewünschte Gradzahl der Drehung eingeben
drehungfrei30 = im.rotate(155) #gewünschte Gradzahl der Drehung eingeben
drehungfrei31 = im.rotate(160) #gewünschte Gradzahl der Drehung eingeben
drehungfrei32 = im.rotate(165) #gewünschte Gradzahl der Drehung eingeben
drehungfrei33 = im.rotate(170) #gewünschte Gradzahl der Drehung eingeben
drehungfrei34 = im.rotate(175) #gewünschte Gradzahl der Drehung eingeben
drehungfrei35 = im.rotate(185) #gewünschte Gradzahl der Drehung eingeben
drehungfrei36 = im.rotate(190) #gewünschte Gradzahl der Drehung eingeben
drehungfrei37 = im.rotate(195) #gewünschte Gradzahl der Drehung eingeben
drehungfrei38 = im.rotate(200) #gewünschte Gradzahl der Drehung eingeben
drehungfrei39 = im.rotate(205) #gewünschte Gradzahl der Drehung eingeben
drehungfrei40 = im.rotate(210) #gewünschte Gradzahl der Drehung eingeben
drehungfrei41 = im.rotate(215) #gewünschte Gradzahl der Drehung eingeben
drehungfrei42 = im.rotate(220) #gewünschte Gradzahl der Drehung eingeben
drehungfrei43 = im.rotate(225) #gewünschte Gradzahl der Drehung eingeben
drehungfrei44 = im.rotate(230) #gewünschte Gradzahl der Drehung eingeben
drehungfrei45 = im.rotate(235) #gewünschte Gradzahl der Drehung eingeben
drehungfrei46 = im.rotate(240) #gewünschte Gradzahl der Drehung eingeben
drehungfrei47 = im.rotate(245) #gewünschte Gradzahl der Drehung eingeben
drehungfrei48 = im.rotate(250) #gewünschte Gradzahl der Drehung eingeben
drehungfrei49 = im.rotate(255) #gewünschte Gradzahl der Drehung eingeben
drehungfrei50 = im.rotate(260) #gewünschte Gradzahl der Drehung eingeben
drehungfrei51 = im.rotate(265) #gewünschte Gradzahl der Drehung eingeben
drehungfrei52 = im.rotate(275) #gewünschte Gradzahl der Drehung eingeben
drehungfrei53 = im.rotate(280) #gewünschte Gradzahl der Drehung eingeben
drehungfrei54 = im.rotate(285) #gewünschte Gradzahl der Drehung eingeben
drehungfrei55 = im.rotate(290) #gewünschte Gradzahl der Drehung eingeben
drehungfrei56 = im.rotate(295) #gewünschte Gradzahl der Drehung eingeben
drehungfrei57 = im.rotate(300) #gewünschte Gradzahl der Drehung eingeben
drehungfrei58 = im.rotate(305) #gewünschte Gradzahl der Drehung eingeben
drehungfrei59 = im.rotate(310) #gewünschte Gradzahl der Drehung eingeben
drehungfrei60 = im.rotate(315) #gewünschte Gradzahl der Drehung eingeben
drehungfrei61 = im.rotate(320) #gewünschte Gradzahl der Drehung eingeben
drehungfrei62 = im.rotate(325) #gewünschte Gradzahl der Drehung eingeben
drehungfrei63 = im.rotate(330) #gewünschte Gradzahl der Drehung eingeben
drehungfrei64 = im.rotate(335) #gewünschte Gradzahl der Drehung eingeben
drehungfrei65 = im.rotate(340) #gewünschte Gradzahl der Drehung eingeben
drehungfrei66 = im.rotate(345) #gewünschte Gradzahl der Drehung eingeben
drehungfrei67 = im.rotate(350) #gewünschte Gradzahl der Drehung eingeben
drehungfrei68 = im.rotate(355) #gewünschte Gradzahl der Drehung eingeben 


#Abspeichern der Abschnitte und der Drehungen

drehung90.save("testbildabschnitt2.jpg")
drehung180.save("testbildabschnitt3.jpg")
drehung270.save("testbildabschnitt4.jpg")
spiegelung.save("testbildabschnitt5.jpg")
umdrehung.save("testbildabschnitt6.jpg")
drehungfrei1.save("testbildabschnitt7.jpg")
drehungfrei2.save("testbildabschnitt8.jpg")
drehungfrei3.save("testbildabschnitt9.jpg")
drehungfrei4.save("testbildabschnitt10.jpg")
drehungfrei5.save("testbildabschnitt11.jpg")
drehungfrei6.save("testbildabschnitt12.jpg")
drehungfrei7.save("testbildabschnitt13.jpg")
drehungfrei8.save("testbildabschnitt14.jpg")
drehungfrei9.save("testbildabschnitt15.jpg")
drehungfrei10.save("testbildabschnitt16.jpg")
drehungfrei11.save("testbildabschnitt17.jpg")
drehungfrei12.save("testbildabschnitt18.jpg")
drehungfrei13.save("testbildabschnitt19.jpg")
drehungfrei14.save("testbildabschnitt20.jpg")
drehungfrei15.save("testbildabschnitt21.jpg")
drehungfrei16.save("testbildabschnitt22.jpg")
drehungfrei17.save("testbildabschnitt23.jpg")
drehungfrei18.save("testbildabschnitt24.jpg")
drehungfrei19.save("testbildabschnitt25.jpg")
drehungfrei20.save("testbildabschnitt26.jpg")
drehungfrei21.save("testbildabschnitt27.jpg")
drehungfrei22.save("testbildabschnitt28.jpg")
drehungfrei23.save("testbildabschnitt29.jpg")
drehungfrei24.save("testbildabschnitt30.jpg")
drehungfrei25.save("testbildabschnitt31.jpg")
drehungfrei26.save("testbildabschnitt32.jpg")
drehungfrei27.save("testbildabschnitt33.jpg")
drehungfrei28.save("testbildabschnitt34.jpg")
drehungfrei29.save("testbildabschnitt35.jpg")
drehungfrei30.save("testbildabschnitt36.jpg")
drehungfrei31.save("testbildabschnitt37.jpg")
drehungfrei32.save("testbildabschnitt38.jpg")
drehungfrei33.save("testbildabschnitt39.jpg")
drehungfrei34.save("testbildabschnitt40.jpg")
drehungfrei35.save("testbildabschnitt41.jpg")
drehungfrei36.save("testbildabschnitt42.jpg")
drehungfrei37.save("testbildabschnitt43.jpg")
drehungfrei38.save("testbildabschnitt44.jpg")
drehungfrei39.save("testbildabschnitt45.jpg")
drehungfrei40.save("testbildabschnitt46.jpg")
drehungfrei41.save("testbildabschnitt47.jpg")
drehungfrei42.save("testbildabschnitt48.jpg")
drehungfrei43.save("testbildabschnitt49.jpg")
drehungfrei44.save("testbildabschnitt50.jpg")
drehungfrei45.save("testbildabschnitt51.jpg")
drehungfrei46.save("testbildabschnitt52.jpg")
drehungfrei47.save("testbildabschnitt53.jpg")
drehungfrei48.save("testbildabschnitt54.jpg")
drehungfrei49.save("testbildabschnitt55.jpg")
drehungfrei50.save("testbildabschnitt56.jpg")
drehungfrei51.save("testbildabschnitt57.jpg")
drehungfrei52.save("testbildabschnitt58.jpg")
drehungfrei53.save("testbildabschnitt59.jpg")
drehungfrei54.save("testbildabschnitt60.jpg")
drehungfrei55.save("testbildabschnitt61.jpg")
drehungfrei56.save("testbildabschnitt62.jpg")
drehungfrei57.save("testbildabschnitt63.jpg")
drehungfrei58.save("testbildabschnitt64.jpg")
drehungfrei59.save("testbildabschnitt65.jpg")
drehungfrei60.save("testbildabschnitt66.jpg")
drehungfrei61.save("testbildabschnitt67.jpg")
drehungfrei62.save("testbildabschnitt68.jpg")
drehungfrei63.save("testbildabschnitt69.jpg")
drehungfrei64.save("testbildabschnitt70.jpg")
drehungfrei65.save("testbildabschnitt71.jpg")
drehungfrei66.save("testbildabschnitt72.jpg")
drehungfrei67.save("testbildabschnitt73.jpg")
drehungfrei68.save("testbildabschnitt74.jpg") """




#Farben und Kontraste ändern

enhancedkontrast = ImageEnhance.Contrast(im) #Kontrast einbauen
enhancedfarbe1 = ImageEnhance.Color(im) #Farben ändern

#Abspeichern der Farb- und Kontraständerung

enhancedkontrast.enhance(6).save("testbildabschnitt75.jpg")
enhancedfarbe1.enhance(0).save("testbildabschnitt76.jpg") #Faktor 0 = Schwarz-weiß

#Filter einsetzen

enhancedfilter1 = im.filter(ImageFilter.SMOOTH)
enhancedfilter2 = im.filter(ImageFilter.GaussianBlur)

#Abspeichern der Filteränderung

enhancedfilter1.save("testbildabschnitt77.jpg")
enhancedfilter2.save("testbildabschnitt78.jpg")

#Image Ops einsetzen

enhancedimaops1 = ImageOps.solarize(im)
enhancedimaops2 = ImageOps.posterize(im, 1)

#Image Ops abspeichern

enhancedimaops1.save("testbildabschnitt79.jpg")
enhancedimaops2.save("testbildabschnitt80.jpg")

#Farbauswahl

source = im.split()
zs = source[1].point(lambda i: 1 < 50 and 255) # source kann man die RGB farben ändern. R=0, G=1, B=2
zs2 = source[0].point(lambda i: 1 + 150)
source[0].paste(zs2, None, zs)
im = Image.merge(im.mode, source)

# Farbauswahl speichern

im.save("testbildabschnitt81.jpg")