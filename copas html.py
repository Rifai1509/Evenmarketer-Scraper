import requests
from bs4 import BeautifulSoup
import csv

url = 'https://it-list.eventmarketer.com/?q=winners'
r = requests.get(url)

# f = open('r.html', 'w+')
# f.write(r.text)
# f.close()

soup = BeautifulSoup(open('./r.html'), 'html.parser')
winners = soup.findAll('div','modal-content')

datas = []
for win in winners:
    name = win.find('h2').text
    # print(name)
    p = win.find('div','modal-body').findAll('p')
    # print(p)
    for x in p:
        # print(x.text.split('<br />'))
        split1= x.text.split('<br />')
        # print(split1)
    # print(split1)
    split2 = split1[-1].split('\n')
    # print(split2)
    web = split2[-2].replace('WEB:','')
    # print(web)
    contact = split2[-1].replace('RFP CONTACT:','').split(',')
    # print(contact)
    if len(contact) > 1:
        contact_name = contact[0].strip()
        email = contact[1].strip()
    else:
        contact_name = contact[0].strip()
        email = contact[0].strip()
    # print(contact_name)
    # print(email)

    datas.append([name, web, contact_name, email])
    # print(datas)
# print(datas)
# for d in datas:
#     print(d)

# writer = csv.writer(open('results.csv', 'w'))
# headers = [
#     'Name',
#     'Web',
#     'Contact Name',
#     'Contact Email',
# ]
# writer.writerow(headers)
# for data in datas:
#     writer.writerow(data)