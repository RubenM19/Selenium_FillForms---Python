from selenium import webdriver
import time
import random

# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\Ruben\\Desktop\\PROG\\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options = options)
time.sleep(1)

#Damos la url a la que queremos scrappear
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc8WWN_IW9KeSqLx6fEhmFKzXZXrPqP4MkAZXQKKpKZ1O87gw/viewform'
#Iniciamos el navegador
driver.get(url)


def fill_forms (ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9):
    question1 = None
    question2 = None
    question3 = None
    question4 = None
    question5 = None
    question6 = None
    question7 = None
    question8 = None
    question9 = None
    
    questionGroup = driver.find_elements_by_class_name("Qr7Oae")

    if questionGroup:
        question1 = questionGroup[0].find_elements_by_class_name("AB7Lab.Id5V1")
        question2 = questionGroup[1].find_elements_by_class_name("AB7Lab.Id5V1")
        question3 = questionGroup[2].find_elements_by_class_name("AB7Lab.Id5V1")
        question4 = questionGroup[3].find_elements_by_class_name("AB7Lab.Id5V1")
        question5 = questionGroup[4].find_elements_by_class_name("AB7Lab.Id5V1")
        question6 = questionGroup[5].find_elements_by_class_name("AB7Lab.Id5V1")
        question7 = questionGroup[6].find_elements_by_class_name("AB7Lab.Id5V1")
        question8 = questionGroup[7].find_elements_by_class_name("AB7Lab.Id5V1")
        question9 = questionGroup[8].find_elements_by_class_name("AB7Lab.Id5V1")

    if question1:
        question1[int(ans1)].click()
    if question2:
        question2[int(ans2)].click()
    if question3:
        question3[int(ans3)].click()
    if question4:
        question4[int(ans4)].click()
    if question5:
        question5[int(ans5)].click()
    if question6:
        question6[int(ans6)].click()
    if question7:
        question7[int(ans7)].click()
    if question8:
        question8[int(ans8)].click()
    if question9:
        question9[int(ans9)].click()

    submit = driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span')
    submit.click()

    driver.close()


button_range1 = random.randint(0,3)
button_range2 = random.randint(0,4)
button_range3 = 0
button_range4 = random.randint(0,2)
button_range5 = 0
button_range6 = 0
button_range7 = random.randint(0,2)
button_range8 = random.randint(0,2)
button_range9 = random.randint(0,1)

fill_forms(button_range1, button_range2, button_range3, button_range4, button_range5, button_range6, button_range7, button_range8, button_range9)