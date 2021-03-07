import requests
from bs4 import BeautifulSoup
import traceback


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    }

url = input('Введите ссылку с результатом: ')
request = requests.get(url).text
soup = BeautifulSoup(request, 'html.parser')

open('links.txt','w').close()

with open('links.txt', 'a') as output:
    for link in soup.findAll('h4'):
        if link is None:
            continue
        else:
            try:
                ready_url = link.find('a').get('href')
            except:
                continue
            output.write(ready_url + '\n')
            print(ready_url)
    output.close()


try:
    for x in range(2,50):
        request = requests.get(url+f'/page:{x}',headers = headers).text
        soup = BeautifulSoup(request,'html.parser')

        with open('links.txt', 'a') as output:
            for link in soup.findAll('h4'):

                if link is None:
                    continue
                else:
                    try:
                        ready_url = link.find('a').get('href')
                    except:
                        continue
                    output.write(ready_url + '\n')
                    print(ready_url)
    output.close()
except Exception as error:
    print(error)