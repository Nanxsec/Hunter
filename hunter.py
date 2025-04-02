import os
import sys
import asyncio
import re
import datetime
import requests
import socket
import threading
from urls import *
from emails import *
from hunter_style import *

# bibliotecas que estarei utilizando no decorrer do desenvolvimento!

# Atualmente estou desenvolvendo e aprimorando a primeira parte: buscas por nomes de usuários!

os.system("cls")
Baner()

# Script em desenvolvimento
# Tem muito mais opções para ser adicionada
# No final você poderá buscar por: nome de usuário, email, telefone e cpf, mapeando assim tudo que tiver cadastrado!

# Script sendo escrito por: Nano
print("""
\033[1;34mMenu:\n\033[m
1 - Buscas por nome de usuário
2 - Buscas por email
3 - Fazer todas as buscas""")

try:
    escolha = str(input("\n\033[1;36m>>>>:\033[m ")).strip()
except KeyboardInterrupt:
    raise SystemExit
if escolha == "1":
    Baner()
    try:
        Username = str(input("\n\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m \033[1mUsername:\033[m ")).replace(" ","")
    except KeyboardInterrupt:
        raise SystemExit
    else:
        if Username != "":
            asyncio.run(sites_urls(name=Username))
elif escolha == "2":
    Baner()
    try:
        Email = str(input("\n\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m \033[1mEmail:\033[m ")).replace(" ","")
    except KeyboardInterrupt:
        raise SystemExit
    else:
        if Email != "":
            asyncio.run(CheckSitesByEmail(email=Email))
elif escolha == "3":
    Baner()
    try:
        user = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m User:\033[m ")).strip()
        mail = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Mail:\033[m ")).strip()
    except KeyboardInterrupt:
        raise SystemExit
    else:
        if user and mail != "":
            while True:
                asyncio.run(sites_urls(name=user,armaz=True))
                asyncio.run(CheckSitesByEmail(email=mail,armaz=True))
                print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Relatório gerado e guardado em um arquivo de texto!!")
                break
