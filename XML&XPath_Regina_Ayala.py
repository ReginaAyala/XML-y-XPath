import xml.etree.ElementTree as ET
import sys

Tree = ET.parse (sys.argv[1])
root = Tree.getroot()

Hijos = Tree.findall('.//book/title | .//book/price')
for Nietos in Hijos:
    print(Nietos.text)

Titulo = Tree.findall(".//title | .//price")
for Elemento in Titulo:
    print(Elemento.text)

Raiz = Tree.findall("./bookstore/book/title | .//price")
for Ancestro in Raiz:
    print(Ancestro.text)