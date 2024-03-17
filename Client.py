from decouple import config

import requests

resposta = input("[1]LOGIN, \n[2]CADASTRAR\n: ")

if resposta == "1": 
    login = input("LOGIN : ")
    senha = input("SENHA : ")
    resposta = requests.get(f"{config('link_api_principal')}/{config('link_api_3')}/{login},{senha}")
    print(resposta.content)

elif resposta == "2":
    login = input("LOGIN : ")
    senha = input("SENHA : ")
    resposta = requests.post(f"{config('link_api_principal')}/{config('link_api_3')}/{login},{senha}")
    print(resposta.content)    
