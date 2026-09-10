from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/search?q=pokemon&oq=pokemon&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIMCAEQLhhDGIAEGIoFMgYIAhAjGCcyCQgDECMYJxjwBTIPCAQQABhDGLEDGIAEGIoFMgoIBRAuGLEDGIAEMgYIBhBFGDwyBggHEEUYPdIBCDM1ODhqMGo3qAIAsAIA&sourceid=chrome&source=chrome.ob&ie=UTF-8")

time.sleep(5)

driver.quit()