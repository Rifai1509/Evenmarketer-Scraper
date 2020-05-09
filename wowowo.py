import requests
import bs4

url = 'https://it-list.eventmarketer.com/?q=winners'
resa = requests.get(url)
f = open('resa.html', 'w+')
f.write(resa.text)
f.close()
soup = bs4.BeautifulSoup((open('./res.html'), 'html.parser')

area = soup.find('div', 'col-sm-12').find('div','row')
product = area.findAll('div', "modal-content")
# rincian = product.find('div','modal-body')

# print(product)
hitung = 0
for p in product:
    hitung +=1
    print('No.     :',hitung)
    print('Name    :',p.find('div', 'col-xs-6').text.replace('\n',''))
    rincian = p.find('div', 'modal-body').find('div', 'col-md-12').text
    if 'WEB' in rincian:
        print('Details :\n'+rincian.strip())
