#!/usr/bin/python3

import socket
import re
import urllib
import sys
import os
import time

try:
    from colorama import *
    init(autoreset=True)
except:

    print("NECESSÁRIO INSTALAÇÃO DE MODULO EXTERNO")
    os.system('pip3 install colorama')
    from colorama import *
    init(autoreset=True)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
    print(Fore.WHITE + Style.BRIGHT + "COLORAMA INSTALADO COM SUCESSO")

try:
    import requests
except:
    print(Fore.LIGHTCYAN_EX +Style.BRIGHT+'='*30)
    print(Fore.WHITE+Style.BRIGHT+'INSTALANDO REQUESTS')
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' *30)
    os.system('pip3 install requests')
    print(Fore.WHITE_EX+Style.BRIGHT+'REQUESTS INSTALADO COM SUCESSO!')
    import requests

def banner ():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT +
    """    ####################################################################
    ##                                                                ##
    ##              Xvideos-dl | Download sem complicação  ♥          ##
    ##                                                                ##
    ##               Feito com ♥ by @ndreh L | 2017.2                 ##
    ##                   GNU GENERAL PUBLIC LICENSE                   ##
    ##                                                   Version 1.0  ##
    ####################################################################\n""" )
    time.sleep(2)
    os.system('clear')

def main():
    
     banner()
     if conection() == True:
        verifica_url()
     else:
         print(Fore.WHITE + Style.BRIGHT +"Sem Conexão com a internet")

def conection():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
    print(Fore.WHITE+Style.BRIGHT+"TESTANDO CONEXÃO")
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

def download(link, title):

    a = link
    tit = title

    user = os.path.expanduser('~')
    os.chdir('%s/Downloads'%user)
    
    ##########################
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
    print(Fore.WHITE + Style.BRIGHT +'BAIXANDO O ARQUIVO - %s'%tit)
    print(Fore.WHITE + Style.BRIGHT +"AGUARDE!!!")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
    urllib.request.urlretrieve(a, '%s'%tit)
    print(Fore.WHITE + Style.BRIGHT +"DOWNLOAD CONCLUIDO COM SUCESSO!\nSALVO NA PASTA DOWNLOAD")
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)

def verifica_url():
    try:
        url = sys.argv[1]

        if 'http://' not in url:
            url = 'http://'+url

        inicial = ['https://www.xnxx.com', 'https://www.xnxx.com/', 'www.xnxx.com', 'xnxx.com', 'www.xnxx.com/',
        'xnxx.com/','https://www.xvideos.com', 'https:www.xvideos.com/', 'www.xvideos.com', 'www.xvideos.com/',
        'xvideos.com', 'xvideos.com']

        for x in inicial:
            if x == url:
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
                print(Fore.WHITE + Style.BRIGHT + "Página Inicial")
                exit(0)

        xn = 'xnxx'
        xv = 'xvideos'
        code = requests.get(url)

        if code.status_code == 404:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
            print(Fore.WHITE + Style.BRIGHT +'VÍDEO NAO ENCONTRADO')
            exit(0)

        elif xn in url or xv in url:
            link(url)

        else:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
            print(Fore.WHITE + Style.BRIGHT +"URL NÃO ACEITA")

    except:
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)
        print(Fore.WHITE + Style.BRIGHT +"COMANDO >> ./xvideos-dl LINK_DO_VIDEO")
        print(Fore.LIGHTCYAN_EX + Style.BRIGHT + '=' * 30)

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

if __name__ == '__main__':
    main()


