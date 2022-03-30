from selenium import webdriver
from time import sleep

navegador = webdriver.Edge()
navegador.get('https://www.youtube.com/')
sleep(3)
navegador.find_element_by_xpath('//*[@id="guide-button"]').click()