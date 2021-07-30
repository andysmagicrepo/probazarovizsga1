# 3 Feladat: Timesheet automatizálása
#
# Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.
#
# A program töltse be a timesheet app-ot az [https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html](https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html) oldalról.
#
# Feladatod, hogy automatizáld selenium webdriverrel a Timesheet  app tesztelését.
#
# Az ellenőrzésekhez __NEM__ kell teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat vagy `assert` összehasonlításokat.
#
# # Az alábbi tesztesetekete fedd le:
#
# ## TC01: üres kitöltés helyessége
# * ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
# * ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni a "next" feliratú gombot
#
# ## TC02: helyes kitöltés helyes köszönet képernyő
# * töltsük ki a következő adatokkal a formot:
#     * test@bela.hu
#     * 2 hours and 0 minutes
#     * working hard
#     * types of work: Time working on visual effects for movie
# * nyomjuk meg a "next" feliratú gombot
# * ellenőrizzük a megjelenő tartalomban az órák és percek helyességét
#
#
# ### A megoldás beadása
# * a megoldásokat a `testproject` mappába tedd, `timesheet.py`
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

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html")

# add_new_button = driver.find_element_by_id("/div/button[@ng-click]')
add_new_button = driver.find_element_by_xpath('//button[text()="Add New"]')
clear_button = driver.find_element_by_xpath('//button[text()="Clear"]')
next_button = driver.find_element_by_xpath('//*[@id="buttons"]/input')
# next_button = driver.find_element_by_class_name('button flex-item')


email = driver.find_element_by_xpath('/html/body/div/section[1]/div[1]/form/input[1]')
time_h = driver.find_element_by_xpath('/html/body/div/section[1]/div[1]/form/input[2]')
time_m = driver.find_element_by_xpath('/html/body/div/section[1]/div[1]/form/input[3]')
messages_window = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
types_of_work_window = driver.find_element_by_xpath('//*[@id="dropDown"]')
add_new_window = driver.find_element_by_xpath('//*[@id="create-new"]/input')

# email = driver.find_element_by_class_name("ng-pristine ng-valid-email ng-invalid ng-invalid-required ng-touched")
# time_h = driver.find_element_by_class_name("ng-pristine ng-valid-min ng-invalid ng-invalid-required ng-touched")
# time_m = driver.find_element_by_class_name("ng-pristine ng-valid-min ng-valid-max ng-invalid ng-invalid-required ng-touched")
# messages_window = driver.find_element_by_class_name("ng-pristine ng-valid ng-touched")
# types_of_work_window = driver.find_element_by_class_name("ng-pristine ng-invalid ng-invalid-required ng-touched")
# add_new_window = driver.find_element_by_class_name("ng-pristine ng-valid ng-touched")

try:
    # tesztadatok
    # ## TC01: üres kitöltés helyessége
    # * ha nincs kitoltve az e-mail mező nem lehet megnyomni a "next" feliratú gombot
    # * ha helytelen (formailag helytelen) e-mailcimmel probáljuk kitölteni a formot nem lehet megnyomni a "next" feliratú gombot
    next_button.click()
    assert next_button.get_property('disabled') == True
    time.sleep(5)
    email.send_keys('ab@exampleom')
    next_button.click()
    assert next_button.get_property('disabled') == True
    # print(subtotal_text.get_attribute("value"))
    # assert subtotal_text.get_attribute("value") == '0.00'
    time.sleep(5)

    # ## TC02: helyes kitöltés helyes köszönet képernyő
    # * töltsük ki a következő adatokkal a formot:
    #     * test@bela.hu
    #     * 2 hours and 0 minutes
    #     * working hard
    #     * types of work: Time working on visual effects for movie
    # * nyomjuk meg a "next" feliratú gombot
    # * ellenőrizzük a megjelenő tartalomban az órák és percek helyességét
    email.clear()
    email.send_keys('test@bela.hu')
    time_h.send_keys('2')
    time_m.send_keys('0')
    messages_window.send_keys('working hard')
    a = Select(driver.find_element_by_name('dropDown'))
    a.select_by_visible_text('Time working on visual effects for movie')
    print(next_button.get_property('disabled'))
    time.sleep(5)
    assert next_button.get_property('disabled') == False
    next_button.click()


except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()
