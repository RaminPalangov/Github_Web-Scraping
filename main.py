import requests
from bs4 import BeautifulSoup

input_1=input('Website:')
headers={
      'user-agent':"Your User-Agent"
  }
link=[input_1]
cl=input('div class name input:')
try:
  for l in link:
    url=l
    r=requests.get(url=url,headers=headers)
    soup=BeautifulSoup(r.text,'lxml')
    print('\nAll LINK')
    for x in soup.findAll('div',class_=cl):
      for d in x.findAll('a'):
        print(d.get('href'))
except:
  print("\nWrong Website link")
else:
  print("\nIf You don't See links.Should be true class name.")

