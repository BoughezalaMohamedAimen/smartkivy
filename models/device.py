from .chalenge import Chalenge
from .urls import UrlsList
from .internetSender import InternetSender
import sqlite3 as sql
from kivymd.toast import toast

class Device:

    def __init__(self,id,nom,type,etat,chambre):
        self.id=id
        self.nom=nom
        self.etat=etat
        self.type=type
        self.chambre=chambre
        self.chalenge=Chalenge()







    def send_commande(self,button):
        try:
            urls=UrlsList()
            self.chalenge.url=urls.local_send_commande+str(self.id)+'/'
            self.chalenge.get_chalenge_and_send(url=urls.chalenge_url)
        except:
            toast("erreur veuillez reéssayer")

    def pause(self,button):
        try:
            urls=UrlsList()
            self.chalenge.url=urls.local_send_commande+str(self.id)+'/3'
            self.chalenge.get_chalenge_and_send(url=urls.chalenge_url)
        except:
            toast("erreur veuillez reéssayer")

    def send_commande2(self,button):
        try:
            urls=UrlsList()
            self.chalenge.url=urls.local_send_commande+str(self.id)+'/2'
            self.chalenge.get_chalenge_and_send(url=urls.chalenge_url)
        except:
            toast("erreur veuillez reéssayer")




    def send_commande_internet(self,button):
        try:
            urls=UrlsList()
            self.internet_sender=InternetSender(headers=urls.headers_json)
            self.internet_sender.send_commande(url=urls.internet_send_commande,local_id=self.id,commande_to_send=1)
        except:
            toast("erreur veuillez reéssayer")


    def pause_internet(self,button):
        try:
            urls=UrlsList()
            self.internet_sender=InternetSender(headers=urls.headers_json)
            self.internet_sender.send_commande(url=urls.internet_send_commande,local_id=self.id,commande_to_send=3)
        except:
            toast("erreur veuillez reéssayer")

    def send_commande2_internet(self,button):
        try:
            urls=UrlsList()
            self.internet_sender=InternetSender(headers=urls.headers_json)
            self.internet_sender.send_commande(url=urls.internet_send_commande,local_id=self.id,commande_to_send=2)
        except:
            toast("erreur veuillez reéssayer")
