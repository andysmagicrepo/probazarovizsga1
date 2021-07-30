# ## 1 Feladat: Hogwards express jegyautomata
#
# A Hogwards express nemrég rájött, hogy érdemes lenne önkiszolgálóvá tenni a
# jegykiállító rendszert a hallgatók vasútvonalán. Lehet, hogy drágák a baglyok.
#
# Itt találod az önkiszolgáló webes applikáció prototípusát:
# [https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html](https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html)
#
# Készíts egy Python python applikációt (akár csak egy darab python fileban) ami selenium-ot használ.
#
# Teszteld le, hogy az általad megadott adatokkal tölti-e ki a jegyet az applikáció. (vigyázz,
# mert elkézpelhető, hogy némely adatokat egynél több helyen is megjeleníti a jegyen az applikáció)
# Nem kell negatív tesztesetet készítened. Egy pozitív teszteset teljesen elég lesz.
#
# Az ellenőrzésekhez __NEM kell__ teszt keretrendszert használnod (mint pl a pytest).
# Egyszerűen használj elágazásokat __NEM kell__ OOP-t használnod.
# Viszont tartalmazzon vizsgálatot a megodásod. Lehetőleg használj az `assert` összehasonlításokat.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time

opt = Options()
opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html")

try:
    # tesztadatok
    passenger_name = driver.find_element_by_id("passenger")
    passenger_name.send_keys('Bazsalya Andras')

    departure_date = driver.find_element_by_id("departure-date")
    departure_time = driver.find_element_by_id("departure-time")
    issue_ticket_Button = driver.find_element_by_id("issue-ticket")

    ticket_passenger = driver.find_element_by_id("passenger-name")
    ticket_departure_date = driver.find_element_by_id("departure-date-text")
    ticket_departure_time = driver.find_element_by_id("departure-time-text")
    ticket_departure_date_side = driver.find_element_by_id("side-detparture-date")
    ticket_departure_time_side = driver.find_element_by_id("side-departure-time")

    date_to_set = datetime(2021, 7, 29, 12, 25, 00, 00)
    departure_time.send_keys(date_to_set.strftime('%I:%M'))
    departure_time.send_keys(date_to_set.strftime('%p'))
    time.sleep(5)
    departure_date.send_keys(date_to_set.strftime('%Y:%M:%D'))
    departure_date.click()
    time.sleep(5)

    # tesztadatok beírása issue ticket gombbal
    issue_ticket_Button.click()
    time.sleep(5)
# bevitt adatok ellenőrzése

    #print(driver.find_element_by_id("passenger-name").text)
    print(ticket_passenger.text)
    assert ticket_passenger.text == 'BAZSALYA ANDRAS'
    print(ticket_departure_date.text)
    assert ticket_departure_date.text == '202125-07-21'
    print(ticket_departure_time.text)
    assert ticket_departure_time.text == '12:25PM'
    print(ticket_departure_date_side.text)
    assert ticket_departure_date_side.text == '202125-07-21'
    print(ticket_departure_time_side.text)
    assert ticket_departure_time_side.text == '12:25PM'
    time.sleep(5)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    driver.close()
    driver.quit()