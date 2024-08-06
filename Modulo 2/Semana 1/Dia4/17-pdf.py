import PyPDF2 as pdf

from PyPDF2 import PdfReader
#1 - Versao e metodos dessa biblioteca
print(pdf.__version__)
print(dir(pdf))

#2 - Importando arquivo PDF

file = open('./Modulo 2/Semana 1/Dia4/helio.pdf', 'rb')
reader = PdfReader(file)
print(reader)
#print(reader.metadata)

info = reader.metadata

#3 - Extraindo informacoes do PDF
print(info.title)
print(info.author)
print(info.creator)
print(info.subject)
print(len(reader.pages))
print(reader.pages[0].extract_text())
print(reader.pages[1].extract_text())

