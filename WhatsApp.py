from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
import pyperclip
import time
from csv import reader

#browser = webdriver.Chrome(executable_path='C:/Users/ansar/Downloads/Whatsapp Automation/Whatsapp-automation-using-python-selenium-master/chromedriver.exe')
browser=webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://web.whatsapp.com/')
browser.maximize_window()



f = open("line.txt", "r")
k=f.read()
f.close()
l=int(k)
#print(l)
groups =[]
with open('contacts.csv',"r") as f:     #################----------change file name here-----------########################
	csv_reader = reader(f)
	for row in csv_reader:
		groups.append(row[2])

msg = "Hello this is automation testing"
print(groups)
for i in range(l,len(groups)):
    print("Hamza")
    try:
        group=groups[i]
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    
        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )
    
        search_box.clear()
    
        time.sleep(1)
    
        pyperclip.copy(group)
    
        search_box.send_keys(Keys.CONTROL, 'v') 
    
        time.sleep(1)
    
        group_xpath = f'//span[@title="{group}"]'
        group_title = browser.find_element_by_xpath(group_xpath)
    
        group_title.click()
    
        time.sleep(1)
    
        input_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
        input_box = browser.find_element_by_xpath(input_xpath)
    
        pyperclip.copy(msg)
        input_box.send_keys(Keys.CONTROL, 'v')  
        input_box.send_keys(Keys.ENTER)
    
        time.sleep(2)
    except Exception as e:
        if i==len(groups)-1:
            f = open("line.txt", "w")
            f.write("1")
            f.close()
        else:
            f = open("line.txt", "w")
            f.write(str(i))
            f.close()
        print(group,"no name found")
        pass
