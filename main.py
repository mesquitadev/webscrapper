import requests
import bs4
import pandas as pd
import numpy as np

# res = requests.get("https://g1.globo.com/busca/?q=assaltos+em+condominios")
for page in range(30):
    # res = requests.get("https://g1.globo.com/busca/?q=assaltos+em+condominios&order=recent&from=now-1y&page=" + str(int(page)))
    res = requests.get("https://g1.globo.com/busca/?q=assaltos+em+condominios&order=recent&from=2019-01-01T00%3A00%3A00-0300&page="+str(int(page))+"&to=2019-10-10T23%3A59%3A59-0300")
    try:
        # Tratamento de erro do HTTP
        res.raise_for_status()

        # Pegando dados do site
        objectSoup = bs4.BeautifulSoup(res.text, features="lxml")

        # Lista os Condomínios
        listCondominimuns = objectSoup.select('.widget--info__title')

        # Lista as Datas
        listDates = objectSoup.select('.widget--info__meta')
        print(len(listDates))

        # Lista o conteúdo de todas as datas
        # file = open("arquivo.txt", "wb")
        # for eachRow in listDates:
        #     len(listDates)
        #     countRows = len(listDates)
        #     print(countRows)
        #     # print(eachRow.getText())
            # file.write(int(eachRow))

    except Exception as e:
        print("Erro: %s" % e)