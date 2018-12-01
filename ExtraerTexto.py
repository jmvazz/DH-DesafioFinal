import requests
import lxml.html

url = "https://pythonista.io/cursos/py101/modulos-y-paquetes"

def TextoDeURL(url):
    html = requests.get(url)
    doc  = lxml.html.fromstring(html.content)
    tags = doc.xpath('//p')
    texto = ""
    for tag in tags:
        texto += tag.text_content()
    return texto

lista_de_palabras = TextoDeURL(url)
print(lista_de_palabras)

