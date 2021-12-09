from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://divar.ir/")
for city in driver.find_elements_by_class_name("kt-button") :
    if city.text == "تهران" :
        city.click()
        break
time.sleep(0.5)

record = driver.find_elements_by_class_name("kt-accordion-item__header")
for type_record in record :
    if type_record.text == "املاک":
        type_record.click()
        break
time.sleep(0.5)

element = driver.find_elements_by_class_name("kt-accordion-item__header")
for type_element in element :
    if type_element.text == "فروش مسکونی":
        type_element.click()
        break
time.sleep(0.5)

more_details = driver.find_elements_by_class_name("kt-accordion-item__header")
for type_more_details in more_details :
    if type_more_details.text == "آپارتمان":
        type_more_details.click()
        break
time.sleep(0.5)

my_url = driver.current_url
driver.get(my_url)

def details():
    list_details = []
    url_of_record = driver.current_url
    title_of_record = driver.find_element_by_class_name("kt-page-title__title--responsive-sized").text
    detail_of_record = driver.find_element_by_class_name("post-description").text
    list_details.append(url_of_record)
    list_details.append(title_of_record)
    list_details.append(detail_of_record)
    return list_details

def scoroll(n):
    SCROLL_PAUSE_TIME = 0.2

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for i in range(n):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(3)

n = 0

record_list = driver.find_elements_by_class_name("kt-post-card")
i = 0
z = 0
while i < len(record_list)-1:
    try :
        record_list[i].click()
        time.sleep(0.5)
        print(details())
        time.sleep(0.5)
        driver.execute_script("window.history.go(-1)")
        record_list = driver.find_elements_by_class_name("kt-post-card")
        i += 1
        z += 1
        if z > 20 :
            n += 1
            z = 0
        scoroll(n)
    except :
        continue
