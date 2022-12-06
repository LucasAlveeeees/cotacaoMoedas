# importar o App, Builder (GUI)
# # criar o nosso aplicativo
# # criar a função build

from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")


class AplicativoLucas(App):
    def build(self):
        return GUI
    def on_start(self):
        self.root.ids["moeda1"].text = f"libraesterlina R${self.pegar_cotacao('GBP')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"
        self.root.ids["moeda5"].text = f"Lenedojapão R${self.pegar_cotacao('JPY')}"
        self.root.ids["moeda6"].text = f"rublorusso R${self.pegar_cotacao('RUB')}"
    def pegar_cotacao(self,moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

AplicativoLucas().run()

