import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_petfriends(selenium):
    # Open PetFriends base page:
    selenium.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")

    btn_newuser.click()

    # click existing user button
    btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("elvsab@bk.ru")

    # add password
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("14416641")

    # click submit button
    btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
    if selenium.current_url == 'https://petfriends.skillfactory.ru/all_pets':
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_petfriends.png')
    else:
        raise Exception("login error")

def test_show_my_pets():

    # Вводим email
    pytest.driver.find_element(By.ID, 'email').send_keys('vasya@mail.com')
    time.sleep(3)
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys('12345')
    time.sleep(3)
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    #pytest.driver.implicitly_wait(10)

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0



def test_show_all_my_pets(selenium):

    # Open PetFriends base page:
    selenium.get("https://petfriends.skillfactory.ru/")

    # click on the new user button
    selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]").click()

    # click existing user button
    selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт").click()

    # add email
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("vasya@mail.com")

    # add password
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("12345")

    # click submit button
    selenium.find_element(By.XPATH, "//button[@type='submit']").click()

    #click my_pets button
    selenium.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
    #pets_cards = selenium.find_elements(By.XPATH, "//tbody//tr")
    pets = WebDriverWait(selenium, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody//tr")))
    #pets = selenium.find_elements(By.XPATH, "//tbody//tr")
    pets_quantity = len(pets)

    pets_amount = selenium.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(':')[1]

    assert int(pets_amount) == pets_quantity


#50% of pets have photo
def test_pets_with_photo(selenium):
    selenium.get("https://petfriends.skillfactory.ru/")
    selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]").click()
    selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт").click()
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("vasya@mail.com")
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("12345")
    selenium.find_element(By.XPATH, "//button[@type='submit']").click()
    selenium.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()

    pets_with_photo = selenium.find_elements(By.XPATH, "//img[contains(@src, 'data')]")
    num_pets_with_photo = len(pets_with_photo)
    pets_amount = selenium.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(':')[1]
    pets_amount_half = int(pets_amount)/2
    if num_pets_with_photo >= pets_amount_half:
        assert True

def test_all_my_pets_info(selenium):
#check if all pets have name, age and breed
    selenium.get("https://petfriends.skillfactory.ru/")
    selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]").click()
    selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт").click()
    field_email = selenium.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("vasya@mail.com")
    field_pass = selenium.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("12345")
    selenium.find_element(By.XPATH, "//button[@type='submit']").click()
    selenium.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()

    names = selenium.find_elements(By.XPATH, '*//tr//td[1]')
    breeds = selenium.find_elements(By.XPATH, '*//tr//td[2]')
    ages = selenium.find_elements(By.XPATH, '*//tr//td[3]')

    for i in range(len(names)):
        assert names[i].text != ''
    for i in range(len(breeds)):
        assert breeds[i].text != ''
    for i in range(len(ages)):
        assert ages[i].text != ''


