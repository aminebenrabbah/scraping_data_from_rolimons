from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
#if you want work scripte you need webdriver 

web = webdriver.Chrome()

web.get('https://www.rolimons.com/deals')
#this functione for save informations
def save(nom_file ,a_or_write_or_read,text):
    file = open(nom_file+'.txt',a_or_write_or_read)
    file.write(text+str('\n'))
    file.close()

# this function for get data 
def get_data():
    try:
        try:
            web.find_element(By.XPATH, value = '/html/body/div[3]/div/div/div[1]/button').click()
        except:
            print('')
        
        dectioner = {}
        for number in range(1,140):
            #for get title
            title  = web.find_element(By.XPATH, value = '/html/body/div[2]/div[2]/div[5]/div['+str(number)+']/a/div/div[1]/div').text
            #for get price
            princ = web.find_element(By.XPATH, value = '/html/body/div[2]/div[2]/div[5]/div['+str(number)+']/a/div/div[3]/div[1]/div[2]').text
            #for get rap
            rap = web.find_element(By.XPATH, value = '/html/body/div[2]/div[2]/div[5]/div['+str(number)+']/a/div/div[3]/div[2]/div[2]').text
            #for get deal
            deal=web.find_element(By.XPATH, value = '/html/body/div[2]/div[2]/div[5]/div['+str(number)+']/a/div/div[3]/div[3]/div[2]').text
            # for cancatinations data 
            iinfo = title +':'+princ+':'+rap+':'+deal
            dectioner[title]={'princ':princ,'rap':rap,deal:deal}
            print(iinfo)
        info_json = json.dumps(dectioner,indent = 140)
        
        file = open('data.json','w')
        
        json.dump(dectioner, file)
        json     
    except:
        print('')
        
    

get_data()

    
