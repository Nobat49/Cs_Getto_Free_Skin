from selenium.webdriver.firefox.options import Options
from time import sleep, strftime
from selenium import webdriver
from random import randint
from os import getcwd

pages = []
frfOptions = Options()
frfOptions.headless = True
driver = webdriver.Firefox(getcwd())
#driver = webdriver.Firefox(getcwd(), options=frfOptions) # Безоконный режим

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

	driver.find_element_by_id('steamAccountName').send_keys('ЛОГИН') # Вписываем логин
	sleep(randint(2,4))

	driver.find_element_by_id ('steamPassword').send_keys('ПАРОЛЬ') # Вписываем пароль
	sleep(randint(2,4))

	driver.find_element_by_id('imageLogin').click() # Нажимаем логин
	sleep(randint(2,4))

	code = input("Enter your Steam Guard code: ")
	driver.find_element_by_id('twofactorcode_entry').send_keys(code) # Вписываем 2F код 
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
