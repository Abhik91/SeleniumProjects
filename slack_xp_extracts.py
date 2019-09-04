from selenium import webdriver
from getpass import getpass
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd


asu_user_name  = input('Enter your ASURITE ID- ')
asu_password = getpass('Enter your password- ')

driver = webdriver.Chrome(executable_path='E:\Study\Python\Programs\chromedriver.exe')
result =driver.get('https://cee300.slack.com')
driver.close

login_page = driver.find_element_by_id('enterprise_member_guest_account_signin_link')
login_page.click()

asu_uname_box = driver.find_element_by_id('username')
asu_uname_box.send_keys(asu_user_name)

asu_pass_box = driver.find_element_by_id('password')
asu_pass_box.send_keys(asu_password)

asu_sign_in_btn =  driver.find_element_by_class_name('submit')
asu_sign_in_btn.submit()

driver.implicitly_wait(20)

asu_xp_channel = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div/nav/div[2]/div[1]/div/div[1]/div/div/div[10]/a')
asu_xp_channel.click()

driver.implicitly_wait(20)

get_send_by = driver.find_elements_by_xpath("//div[@class='c-message__content_header']")
get_send_msg = driver.find_elements_by_xpath("//span[@class='c-message__body']")


send_user = []
for send_by in get_send_by:
    #print('-----------------------------------------------------------------')
    #print(send_by.text)
    send_user.append(send_by.text[:-8].strip())

message  = []   
for msg in get_send_msg:
    #print('-----------------------------------------------------------------')
    #print(msg.text)
    message.append(msg.text)

#print(send_user)
#print(message)

record = []
for i in range(0, len(send_user)):
    for j in range(0,len(message)):
        if i==j:
            users_pts_given=re.findall(r'[@]\w+',message[j])
            user_string = str(users_pts_given).strip('[]')
            points=message[j][message[j].find('award')+len('award'):message[j].find('xp')+len('xp')].strip()
            #print(points)

            record.append((send_user[i],points,user_string))
            break;

#print(record)

df = pd.DataFrame(record, columns=['Commented By', 'Points', 'User'])
df.to_csv('E:\Study\Python\Programs\Extract.csv', index=False, encoding='utf-8')




#print (len(records))
#print (records)
