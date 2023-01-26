import requests
from bs4 import BeautifulSoup
import pandas as pd

name=[]
price=[]
marketcap=[]
vol_24=[]
total_vol=[]
chg=[]
headers={
      'user-agent':"Your User-Agent"
  }
link=['https://www.investing.com/crypto/currencies']
for l in link:
  r=requests.get(url=l,headers=headers)
  soup=BeautifulSoup(r.text,'lxml')
  for a in soup.findAll('tbody'):
    for d in a.findAll('tr'):
      for l in d.findAll('a')[0]:
        name.append(l)
        for z in d.findAll('a')[1]:
          price.append(z)
          for zz2 in d.findAll('td',class_='js-market-cap'):
            marketcap.append(zz2.text.strip())
            for v in d.findAll('td',class_='js-24h-volume'):
              vol_24.append(v.text.strip())
              for t in d.findAll('td',class_='js-total-vol'):
                total_vol.append(t.text.strip())
                for c in d.findAll('td',class_='js-currency-change-7d greenFont'):
                  chg.append(c.text.strip())
df=pd.DataFrame()
df['Name']=name
df['Price']=pd.Series(price)
df['Market Cap']=pd.Series(marketcap)
df['Vol (24H)']=pd.Series(vol_24)
df['Total Vol']=pd.Series(total_vol)
df['Chg (7D)']=pd.Series(chg)
display(df)
