# 5 Feladat: Landtransfer tax automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a Landtransfer tax app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html](https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Landtransfer tax app tesztelését.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# # Az alábbi tesztesetekete fedd le:
#
# ## TC01: üres kitöltés helyessége
# * ha nincs kitoltve az "Estimate of property you wish you to purchase:" mező de mégis csak megnyomjuk a "Go" feliratú gombot
# * ellenőrizzük, hogy a "Land Transfer Fee" feliratú mező pontosan üres marad-e
# * ellenőrizzük, hogy megjelenik-e a következő felirat: "Enter the property value before clicking Go button."
#
# ## TC02: helyes kitöltés helyes kitöltése
# * töltsük ki a következő adatokkal a formot:
#     * 33333
# * nyomjuk meg a "Go" feliratú gombot
# * ellenőrizzük, hogy a "Land Transfer Fee" feliratú mező pontosan: 16.665 értéket mutatja-e
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `landtrasfertax.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér :(
