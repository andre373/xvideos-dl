#!/usr/bin/python3
import time, os

print("="*60)
print('É NECESSÁRIO TER O MODULO | REQUESTS | INSTALADO\n >> COMANDO PARA INSTALAR >> pip3 install requests')
print("="*60)
time.sleep(5)
os.system('clear')

import requests
import socket
import re
import urllib
import sys

def main():

     url = sys.argv[1]

     inicial=['https://www.xnxx.com','https://www.xnxx.com/','www.xnxx.com','xnxx.com','www.xnxx.com/','xnxx.com/',
     'https://www.xvideos.com','https:www.xvideos.com/','www.xvideos.com','www.xvideos.com/','xvideos.com','xvideos.com']
        
     for x in inicial:
        if x == url:
            print("Página Inicial")
            exit(0)

     if conection() == True:
        try:
            xn ='xnxx'
            xv = 'xvideos'
            if xn in url or xv in url:
                link(url)
            else:
                print("URL NÃO ACEITA")

        except IndexError:
            print("DIGITE UM ARGUMENTO")
     else:
         print("Sem Conexão com a internet")

def conection():

    print("="*30)
    print("TESTANDO CONEXÃO")
    confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
    for host in confiaveis:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)

        try:
            b = a.connect_ex((host, 80))
            if b == 0:  # ok, conectado
                return True
        except:
            pass
        a.close()
    return False

def link(arg):

    a = arg
    padrao_title = re.compile(r"\t\w*\.\w.+Title\(\'(\w+.+)\'\)")
    links=[]
    titulo=[]
    padrao_link = re.compile(r'\t\w+\.\w+\(.(https.\/\/w*.*).\)')
    soup = requests.get(a)
    url = re.findall(padrao_link, soup.text)
    title = re.findall(padrao_title, soup.text)
    links.append(url[1])
    for x in title:
        titulo.append(x)
    download(links[0], titulo[0])

def download(link, title):

    a = link
    tit = title
    ##########################
    #SALVAR NA PASTA DOWNLOAD#
    ##########################
    user = os.path.expanduser('~')
    os.chdir('%s/Downloads'%user)
    
    ##########################
    print("="*30)
    print('BAIXANDO O ARQUIVO - %s'%tit)
    print("AGUARDE!!!")
    print("=" * 30)
    urllib.request.urlretrieve(a, '%s'%tit)
    print("DOWNLOAD CONCLUIDO COM SUCESSO!\nSALVO NA PASTA DOWNLOAD")
    print("=" * 30)

if __name__ == '__main__':
    main()

