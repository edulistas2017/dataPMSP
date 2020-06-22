import smtplib
import locale
import requests
from bs4 import BeautifulSoup
import time

def enviaEmail(subject, body, URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('edulistas2007@gmail.com', 'meaqaudjjdfdgyyq')
    subject = 'PRODUTO monitorado:' + subject
    body =  subject + 'Preço monitorado: \n\n'+ 'Valor: ' + body + '\n\n Link: ' + URL + '\n\n Assinado: O MONITOR'
    originario = 'edulistas2007@gmail.com'
    destinatario = 'earaujo@hotmail.com'
    msg = f'Subject: {subject} \n\n {body}'
    codificacao = locale.getpreferredencoding()
    server.sendmail(originario,destinatario,msg.encode(codificacao))
    print( 'email enviado ok !')
    server.quit()    
    
def checaPreco():
        URL = 'https://www.amazon.com.br/dp/B07KD8HB2G?pf_rd_r=DZ2AYX0VDQG8QR39612D&pf_rd_p=2d4dda82-b8f4-4535-a7f7-501b9a3dab2c'
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
        page = requests.get(URL, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        #productTitle
        title = soup.find(id="productTitle").get_text().strip()
        #priceblock_dealprice
        price = soup.find(id="priceblock_dealprice").get_text().strip()
        converted_price = float(price[2:5])
        if (converted_price < 600 ):
            print(title,price, converted_price)
            enviaEmail(title,price, URL)

while(True):
    checaPreco()
    time.sleep(60)

    
