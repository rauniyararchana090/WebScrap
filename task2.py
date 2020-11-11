import csv
import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error 



def site(code):
    url='https://en.wikipedia.org/wiki/'+code+'_Airport'
    page_html = requests.get(url)
    return  page_html
def wbscrap():
    with open('C:/Users/Dell/Desktop/Task2/airportcode_2.csv','r') as csv_file:
        csv_reader= csv.reader(csv_file)
        next (csv_reader)
        for line in csv_reader:
            code=line[0]
            print(code)
            respond = site(code)
            #source = requests.get(respond)
            soup = BeautifulSoup(respond.text, "lxml")
            '''
            try:
                table = soup.findAll("table", {"class" : "infobox vcard"})
                table= table[0]
            except:
                print('Not found')
                '''        
            try:
                code = soup.findAll("div",{"class" : "hlist hlist-separated"})
                code = code[0]
                data = soup.findAll("span", {"class": "nickname"})
                iata = code
                icao = data[1].text
            except:
                print('not found code!!')
            try:
                Airport_name = name= soup.find('div', class_='fn org').text
                
            except:
                print(' Airport name not found')
            
            Airport_loc = soup.findAll("tr")
            loc=soup.find_all('td', class_='label')
            try :
                location=loc[0].text
                #location = Airport_loc[8].td.text.split(":")
            except:
                print('No location')
            try:
                gps=soup.find('span', class_="geo-dec").text
            except:
                    gps='unknown'   
    value =[iata,icao, Airport_name,location,gps]
    print(value) 
                
with open ('new_info.csv','w') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(['iata', 'icao', 'airport_name', 'location', 'gps'])
        writer.writerow(wbscrap())
                            
                                        
    