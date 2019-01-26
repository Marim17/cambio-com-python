import requests
import json
import pandas as pd

def main():
    print("Estabelecendo conexão com o link...")
    dollar = cambio_dollar(None)
    euro = cambio_euro(None)
    libra = cambio_libra(None)
    exportar_csv(dollar, euro, libra)


def cambio_dollar(url):
    if url is None:
        url = "http://data.fixer.io/api/latest?access_key=822e4f212a9a468acfcab74eda3af982&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl/taxa_usd
        real = round(real, 2)
        return real #enviar valor para onde a função foi chamada
    else:
        print("Link defeituoso")

def cambio_euro(url):
    if url is None:
        url = "http://data.fixer.io/api/latest?access_key=822e4f212a9a468acfcab74eda3af982&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_brl = dados['rates']['BRL']
        taxa_eur = dados['rates']['EUR']
        real2 = taxa_brl / taxa_eur
        real2 = round(real2, 2)
        return real2
    else:
        print("Link defeituoso")

def cambio_libra(url):
    if url is None:
        url = "http://data.fixer.io/api/latest?access_key=822e4f212a9a468acfcab74eda3af982&format=1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()
        taxa_brl = dados['rates']['BRL']
        taxa_gbp = dados['rates']['GBP']
        real3 = taxa_brl / taxa_gbp
        real3 = round(real3, 2)
        return real3
    else:
        print("Link defeituoso")

def exportar_csv(dollar, euro, libra):
    linha = {'Dollar - USD': [dollar], 'Euro - EUR': [euro], 'Libra - GBP': [libra]}
    frame = pd.DataFrame(linha, columns = ['Dollar - USD', 'Euro - EUR', 'Libra - GBP'])
    frame.to_csv('moeda.csv')
    print('Dados salvos na tabela.')



#execulta o main
if __name__ == '__main__':
    main()