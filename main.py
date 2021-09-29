from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from selenium import webdriver
from random import randint
import os

pages = []
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

def time():
	return(strftime('%X'))

def login():
	driver.get(STEAM_GUARD_CODE)
	code = driver.find_element_by_id('title').text

	driver.get('https://csgetto.one/') # Открываем сайт
	sleep(randint(1,3))

	driver.find_element_by_xpath('/html/body/div[17]/div[2]/span').click() # Закрываем приветствие
	sleep(2)

	driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/a').click() # Заходим через стим
	sleep(randint(1,3))

	for handle in driver.window_handles: # Выбираем окно со входом
		pages.append(handle)

	driver.switch_to.window(pages[-1])
	sleep(1)

	try:
		driver.find_element_by_id('acceptAllButton').click() # Принимаем куки
		sleep(1)
	except:
		print('Coockies was accept')

	driver.find_element_by_id('steamAccountName').send_keys(STEAM_LOGIN) # Вписываем логин
	sleep(randint(1,3))

	driver.find_element_by_id ('steamPassword').send_keys(STEAM_PASSWORD, Keys.ENTER) # Вписываем пароль
	sleep(randint(2,3))

	driver.find_element_by_id('twofactorcode_entry').send_keys(code, Keys.ENTER) # Вписываем 2F код
	sleep(randint(1,2))

#	driver.find_element_by_xpath('//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]').click() # Подтверждаем 2F код

	driver.switch_to.window(pages[0]) # Выбираем первое окно

	driver.close() # Закрываем окно

	driver.switch_to.window(pages[-1]) # Выбираем основное окно

	try: # Проверяем, вошли ли мы
		driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/a').click() 
		sleep(randint(1,4))
		driver.find_element_by_id('imageLogin').click()
		print(f'[{time()}] Login Success')
	except:
		print(f'[{time()}] Login Success')

login()
sleep(randint(1,4))

while True:
	driver.get('https://csgetto.win/freeskin')
	try:
		driver.find_element_by_id('getFreeSkin').click()
		print(f'[{time()}] Skin received, cooldown 40 minutes')
		sleep(2400)
	except:
		print(f'[{time()}] Impossible to get skin, cooldown 20 minutes')
		sleep(1200)
