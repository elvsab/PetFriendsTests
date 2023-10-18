from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()
# 10 тестов для задания 24.7.2
"""Проверка на корректность ввода данных при обновлении для поля возраст"""


def test_post_wrong_age(name='kotopes', animal_type='unknown', age='unknown', pet_photo='images/catdog.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_info_about_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert type(result['age']) != int

"""проверка на заполнение всех обязательных полей"""


def test_unseccessful_fields_fill(name=' ', animal_type=' ', age=' '):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_info_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == ' '
    assert result['animal_type'] == ' '
    assert result['age'] == ' '

"""проверка на наличие файла при добавлении нового питомца"""


def test_incorrect_format_of_data(name='kotopes', animal_type='unknown', age='3', pet_photo='images/tram.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    try:
         status, result = pf.add_info_about_new_pet(auth_key, name, animal_type, age, pet_photo)
    except FileNotFoundError:
        assert True
    else:
        assert False
