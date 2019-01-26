import requests
import json

def main():
    print("Estabelecendo conexão com o link...")
    cambio_dollar(None)
    cambio_euro(None)
    cambio_libra(None)


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
        print("O valor do Dollar atual é: %.2f reais" % real)

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
        print("O valor do Euro atual é: %.2f reais" % real2)

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
        print("O valor da Libra atual é: %.2f reais" % real3)

#execulta o main
if __name__ == '__main__':
    main()