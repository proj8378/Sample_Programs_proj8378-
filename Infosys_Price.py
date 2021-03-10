

import requests
from bs4 import BeautifulSoup


def Infosys_Price_Tracker():
    url = 'https://finance.yahoo.com/quote/INFY.BO?p=INFY.BO&.tsrc=fin-srch'
    resp = requests.get(url)

    #   print (resp)

    #if resp == 200:
    soup = BeautifulSoup(resp.text,'lxml')

    infy_price = soup.find_all('div',{'class':'D(ib) Mend(20px)'})[0].find('span').text

    print (infy_price)


while True :
    print ("Price of Infosys is ")
    Infosys_Price_Tracker()
    
    


"""

url_for_best_stocks = "https://getmoneyrich.com/top-stocks-to-buy-in-india/"

resp = requests.get(url_for_best_stocks)
soup = BeautifulSoup(resp.text,'lxml')


for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    print (tds[0],tds[1].text, tds[2].text,tds[3].text,tds[4].text,tds[5].text)
    


"""

"""

url_for_bluechip = "https://www.reliancesmartmoney.com/stocks/exotic/blue-chip-stocks"
resp = requests.get(url_for_bluechip)

soup = BeautifulSoup(resp.text,'lxml')

#tcs_price = soup.find_all('div',{'class':'cardbg stockcardbg stockcard'})[0].find('name').text

print(soup.get_text())

print (tcs_price)

"""

