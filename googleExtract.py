import requests, webbrowser, bs4

# Inserção dos termos
termosBuscados = input()
print("Digite os termos a serem buscados:" + termosBuscados)

#requisição no google
res = requests.get("https://google.com/search?q=" + termosBuscados)

#verifica o status code
res.raise_for_status()

#analisa o content
parser = bs4.BeautifulSoup(res.text, features="lxml")

#receber a lista com as primeiras páginas do google

linksList = parser.select('.r a')

print(linksList[0])