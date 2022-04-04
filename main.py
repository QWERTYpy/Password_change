from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
# import os


def beward(user_name, old_password, new_password, ip_camera, ver):
    """ Данная функция эмулирует действия пользователя по смене пароля в Web интерфейсе для камер Beward


    :param user_name:
    :param old_password:
    :param new_password:
    :param ip_camera:
    :param ver:
    :return:
    """
    # Initialize Chrome WebDriver
    # EXE_PATH = r'chromedriver.exe'
    driver = webdriver.Chrome()
    driver.set_window_size(1600, 500)
    # Открываем адрес
    driver.get(f'http://{user_name}:{old_password}@{ip_camera}/')
    time.sleep(3)
    if ver == 'old':
        x_offset = 700
        y_offset = 70
    elif ver == 'new':
        x_offset = 700
        y_offset = 70
    elif ver == 'new2':
        x_offset = 1300
        y_offset = 40
    ActionChains(driver).move_by_offset(x_offset, y_offset).click().perform()
    time.sleep(2)
    ActionChains(driver).reset_actions()
    # ActionChains(driver).move_by_offset(270, 200).context_click().perform()
    if ver == 'old':
        x_offset = 280
        y_offset = 200
    elif ver == 'new':
        x_offset = 280
        y_offset = 170
    elif ver == 'new2':
        x_offset = 100
        y_offset = 270
    ActionChains(driver).move_by_offset(x_offset, y_offset).click().perform()
    time.sleep(1)
    ActionChains(driver).reset_actions()
    if ver == 'old':
        y_offset = 230
    elif ver == 'new':
        y_offset = 200
    ActionChains(driver).move_by_offset(290, y_offset).click().perform()
    time.sleep(1)

    ActionChains(driver).reset_actions()
    if ver == 'old':
        x_offset = 700
        y_offset = 240
    elif ver == 'new':
        x_offset = 800
        y_offset = 210
    elif ver == 'new2':
        x_offset = 500
        y_offset = 200
    ActionChains(driver).move_by_offset(x_offset, y_offset).click().perform()

    for _ in range(10):
        ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(new_password).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
    ActionChains(driver).send_keys(new_password).perform()
    ActionChains(driver).reset_actions()
    if ver == 'old':
        x_offset = 800
        y_offset = 270
    elif ver == 'new':
        x_offset = 850
        y_offset = 235
    elif ver == 'new2':
        x_offset = 450
        y_offset = 260
    ActionChains(driver).move_by_offset(x_offset, y_offset).context_click().perform()
    time.sleep(3)


file = open('config.txt', 'r', encoding="utf8")
user_name = ''
old_password = ''
new_password = ''
ip_camera = ''
for line in file:
    if line[0] == '#':
        continue
    if line[0].isalpha():
        user_name, old_password, new_password = line.split(',')
        # print(user_name, old_password, new_password)
    if line[0].isdigit():
        ip_camera, ver = line.split()
    if len(ip_camera) > 0:
        print(ip_camera, '->', ver)
        beward(user_name, old_password, new_password, ip_camera, ver)
        ip_camera = ''


file.close()
