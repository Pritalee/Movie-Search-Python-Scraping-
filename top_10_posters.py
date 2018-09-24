from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
str1 = "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=600ca544-31f5-4bd8-ae38-"
str2 = "ea4014c93bab&pf_rd_r=04S9H97MWCDD7KS11JTX&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_india_tr_rhs_1"
driver.get(str1+str2)
ht = driver.page_source
#print(ht)
soup = BeautifulSoup(ht, 'lxml')
head_code = soup.find("table", "chart full-width")
#print(head_code)
tr = head_code.find_all('tr')
del tr[0]
#print(tr)

page_href = []
img_href = []
i=0
while(i<=10):
    page_href.append('https://www.imdb.com'+tr[i].find('td', class_='posterColumn').find('a')['href'])
    #print(page_href)
    driver.get(page_href[i])
    t=driver.page_source
    #print(t)
    soup1 = BeautifulSoup(t,'lxml')
    print(soup1.find('div',class_="title_wrapper").find("h1").text)
    img_href.append(soup1.find('div', class_='poster').find("img")['src'])
    f = open(str(i) + '.jpg', 'wb')
    f.write(requests.get(img_href[i]).content)
    f.close()
    i=i+1
#print(img_href)

#print(ht)

