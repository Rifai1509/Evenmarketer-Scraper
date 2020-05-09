import requests
import csv
from bs4 import BeautifulSoup

res = requests.get('https://it-list.eventmarketer.com/?q=winners')
# #
# f = open('res.html', 'w+')
# f.write(res.text)
#f.close()


soup = BeautifulSoup(open('./res.html'), 'html.parser')
winners = soup.find_all('div', attrs={'class':'modal-content'})

datas = []
for winner in winners:
    name = winner.find('h2').text
    p = winner.find_all('p')
    for i in p:
        split = i.text.split('<br />')
    #    print(len(split))
    split = split[-1].split('\n')
    #
    web = split[-2].replace('WEB:','').strip()
    print(web)
    contact = split[-1].replace('RFP CONTACT:','').split(',')

    if len(contact) > 1:
        contact_name = contact[0].strip()
        email = contact[1].strip()
    else:
        contact_name = contact[0].strip()
        email = contact[0].strip()

    print(name)
    print(web)
    print(contact_name)
    print(email)

    datas.append([name, web, contact_name, email])

with open('results.csv', 'w',newline='') as file:
    writer = csv.writer(file)
    headers = [
         'Name',
         'Web',
         'Contact Name',
         'Contact Email',
    ]
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)



