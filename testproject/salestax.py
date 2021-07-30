# # 2 Feladat: Sales tax applikáció funkcióinak automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a sales tax app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html](https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a sales tax kalkulátort.
#
# # Az alábbi tesztesetekete fedd le:
#
# ## TC01: üres kitöltés helyessége
# * nem kell ellenőrizni, hogy üresek-e a mezők, csak azt, hogy alapból a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 0.00 értéket kell mutasson.
# * illetve a "Calculate Order" gomb megyomására a `gtotal` mező 4.95 értéket kell mutasson
#
# ## TC02: 6" x 6" Volkanik Ice kitöltés helyessége
# * válasszuk ki a Product Item feliratú mezőből a `6" x 6" Volkanik Ice` értéket
# * a quantity feliratú mezőbe írjunk 1-et
# * ellenőrizzük, hogy a "Subtotal" feliratú gomb megnyomásakor a `salestax` azonosítójú mező 4.95 értéket kell mutasson.
# * illetve a "Calculate Order" gomb megyomására a `gtotal` mező 9.90 értéket kell mutasson
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `salestax.py`
# * a lokálisan kidolgozott megoldásokat előbb commitold `git commit`
# * majd ne felejtsd el `git push` segítségével a Github szerverre is felküldeni
# * ne felejtsd el, hogy pontokat ér a szintaktikai legjobb praktikák megvalósítása (`ctlr`+`alt`+`l`)
# * akkor is add be megodásod, ha nem vagy benne biztos, mert részpontokat ér mindennemű a tárgyhoz kötődő kód beadása
# * a megodás fájlba írjál kommentet amiben elmagyarázod, hogy mit akartál csinálni. Ne vidd túlzásba, de ne is legyen komment nélkül leadott fájlod.
# * nem beadott vagy üres fálj formájában beadott feladat megoldás `0` pontot ér


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select

opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html")

subtotal_button = driver.find_element_by_id("subtotalBtn")
usps_button = driver.find_element_by_id("select2")
calculate_o_button = driver.find_element_by_id("gtotalBtn")

product_item = driver.find_element_by_id("Proditem")
quantity_text = driver.find_element_by_id("quantity")
subtotal_text = driver.find_element_by_id("subtotal")
tax_text = driver.find_element_by_id("salestax")
total_text = driver.find_element_by_id("gtotal")

try:
    # tesztadatok
    # TC01: üres kitöltés helyessége
    # assert (tax_text.text != '0.00')  # TC1 hibás, mert nem a `salestax` mező van megadva ellenőrzésre, ahol megjelenik az adat az a 'subtotal'
    subtotal_button.click()
    print(subtotal_text.get_attribute("value"))
    assert subtotal_text.get_attribute("value") == '0.00'
    time.sleep(1)

    calculate_o_button.click()
    print(total_text.get_attribute("value"))
    print(tax_text.get_attribute("value"))
    assert total_text.get_attribute("value") == '4.95'
    assert tax_text.get_attribute("value") == '0.00'  #A 'Calculate Order' gombra kattintást követően jelenik meg a '0.00' a 'salestax'-ban és a 4.95 `gtotal`-ban
    time.sleep(5)

    # TC02: 6" x 6" Volkanik Ice kitöltés helyessége
    # Product Item feliratú mezőből a `6" x 6" Volkanik Ice` értéket
    # quantity feliratú mezőbe írjunk 1 - et
    # Subtotal " feliratú gomb megnyomásakor a `salestax` azonosítójú mező 4.95 értéket kell mutasson.
    # * illetve a "Calculate Order" gomb megyomására a `gtotal` mező 9.90 értéket kell mutasson
    # bevitt adatok ellenőrzése
    #product_item.click()
    #product_item.send_keys("4.95")
    subtotal_text.clear()
    a = Select(driver.find_element_by_id('Proditem'))
    a.select_by_visible_text('6" x 6" Volkanik Ice')
    quantity_text.send_keys('1')
    subtotal_button.click()
    print(subtotal_text.get_attribute("value")) # újabb hiba, mert nem a `salestax` mező van megadva ellenőrzésre, ahol megjelenik az adat az a 'subtotal'
    assert subtotal_text.get_attribute("value") == '4.95'
    calculate_o_button.click()
    print(total_text.get_attribute("value"))
    assert total_text.get_attribute("value") == '9.90'

    time.sleep(5)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()
