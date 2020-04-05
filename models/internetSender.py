from kivymd.toast import toast
from kivy.network.urlrequest import UrlRequest
import json

class InternetSender:
    def __init__(self,headers):
        self.headers=headers



    def send_commande(self,url,local_id,commande_to_send):
        data=json.dumps({
        'local_id':local_id,
        'commande':commande_to_send})


        req = UrlRequest(url=url,
        on_success=self.send_commande_internet_success,
        on_failure=self.send_commande_internet_failure,
        on_error=self.send_commande_internet_failure,
        req_body=data,
        req_headers=self.headers,
        timeout=5)

    def send_commande_internet_success(self,req,result):
        toast("commande envoyée avec succes")

    def send_commande_internet_failure(self,req,result):
        toast("echec veuillez réessayer")
