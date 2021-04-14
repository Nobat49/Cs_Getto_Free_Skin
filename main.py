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
	driver.get('https://csgetto.win/') # Открываем сайт
	sleep(randint(1,3))

	driver.find_element_by_xpath('/html/body/div[17]/div[2]/span').click() # Закрываем приветствие
	sleep(randint(1,3))

	driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/a').click() # Заходим через стим
	sleep(randint(1,3))

	for handle in driver.window_handles: # Выбираем окно со входом
		pages.append(handle)

	driver.switch_to.window(pages[-1])
	sleep(randint(2,4))

	driver.find_element_by_id('steamAccountName').send_keys('noibat49') # Вписываем логин
	sleep(randint(2,4))

	driver.find_element_by_id ('steamPassword').send_keys('19216812a') # Вписываем пароль
	sleep(randint(2,4))

#	driver.find_element_by_id('imageLogin').click() # Нажимаем логин
#	sleep(randint(2,4))

	main_page = driver.page_source
	print(main_page)

login()
"""
	code = input("Enter your Steam Guard code: ")
	#code = STEAM_CODE
	driver.find_element_by_id('twofactorcode_entry').send_keys(code) # Вписываем 2F код http://www.realix.ru/?p=1144
	sleep(randint(2,4))

	driver.find_element_by_xpath('//*[@id="login_twofactorauth_buttonset_entercode"]/div[1]').click() # Подтверждаем 2F код

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
		print(f'[{time()}] Skin received, cooldown 24 hours')
		sleep(86450)
	except:
		print(f'[{time()}] Impossible to get skin, cooldown 10 minutes')
		sleep(600)
"""