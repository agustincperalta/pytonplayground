 
import imapclient, pyzmail
from bs4 import BeautifulSoup

messages = []
filename = 'Problemas.docx'
CUENTA = input("introduce tu correo de gmail")
PASSWORD = input("introduce tu password")
o = imapclient.IMAPClient('imap.gmail.com', ssl=True)
o.login(CUENTA, PASSWORD)
o.select_folder('INBOX', readonly=True)
# Buscar solo los mensajes que contienen problemas DONE
cadena = 'Daily Coding Problem: Problem #'
UIDS = o.search(['FROM', 'founders@dailycodingproblem.com', 'SUBJECT', cadena])
rawMessages = o.fetch(UIDS, ['BODY[]', 'FLAGS'])

for i in rawMessages:
    messages.append(pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]']))

'''for i in messages:
    print(i.text_part.get_payload().decode('UTF-8'))
'''

with open(filename, 'w') as file:
    for i in messages:
        file.write(i.get_subject() + "\n")
        #TODO Hacer que solo imprima el texto donde se encuentra el problema
        codigo = i.html_part.get_payload().decode('UTF-8')
        sopa = BeautifulSoup(codigo, 'html.parser')
        parrafos = sopa.find_all('p')
        for p in parrafos:
            file.write(p.text.strip() +'\n')
        file.write('\n\n')
o.logout()
