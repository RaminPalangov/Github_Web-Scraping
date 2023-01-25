print('Web scraping')
input_1=input('Website:')
headers={
      'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"
  }
link=[input_1]
cl=input('div class name input:')
for l in link:
  url=l
  r=requests.get(url=url,headers=headers)
  soup=BeautifulSoup(r.text,'lxml')
  try:
    print('\nAll LINK')
    for x in soup.findAll('div',class_=cl):
      a=x.find('a')
      print(a.get('href'))
  finally:
    print("\nIf You don't See links.Should be true class name and website")
