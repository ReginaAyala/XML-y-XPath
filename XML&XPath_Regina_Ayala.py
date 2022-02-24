from lxml import etree
import sys

Tree = etree.parse (sys.argv[1])

Hijos = Tree.xpath('//book/title | //book/price')
for Nietos in Hijos:
    print(Nietos.text)

Titulo = Tree.xpath("//title | //price")
for Elemento in Titulo:
    print(Elemento.text)

Raiz = Tree.xpath("/bookstore/book/title | //price")
for Ancestro in Raiz:
    print(Ancestro.text)