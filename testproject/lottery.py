# 4 Feladat: Lottoszámok automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Lotto app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html](https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Lotto app tesztelését.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# # Az alábbi tesztesetekete fedd le:
#
# ## TC01: lotto huzas elott nem ismertek a szamok
# * nem szabad, hogy akár csak egy szám is megjelenjen mielőt az első alkalommal a "Generate" feliratú gombra kattintunk
#
# ## TC02: lottohuzás működik
# * Nyomjuk meg hatszor a "Generate" feliratú gombot
# * Ellenőrizzük, hogy pontosan 6db szám jelenik meg a képernyőn
# * Olvassuk ki a számokat és ellnőrizzük, hogy mind 1 és 59 között vannak
#
# ## TC03: lottohúzás befejeződött
# * Nyomjuk meg 7x is a "Generate" feliratú gombot
# * Ellenőrizzük, hogy pontosan nem jelent meg hetedik szám
# * Nyomjuk meg a "Reset" feliratú gombot
# * nem szabad, hogy akár csak egy szám is megjelenjen miután a "Reset" gombot megnyomtuk
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `lottery.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
