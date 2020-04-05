from kivy.network.urlrequest import UrlRequest
from kivymd.toast import toast

class Chalenge:
    def __init__(self,chalenge=None,url=None):
        self.chalenge=chalenge
        self.url=url




    def get_chalenge_and_send(self,url):
        req = UrlRequest(
        url=url,
        on_success=self.chalenge_success,
        on_failure=self.chalenge_failure,
        on_error=self.chalenge_failure,
        timeout=5)



    def chalenge_success(self,req,result):
        self.chalenge=self.decrypt(result)
        self.url+='?ch='+self.chalenge
        self.send()


    def chalenge_failure(self,req,result):
        toast("echec veuillez réessayer")



    def send(self):
        req = UrlRequest(
        url=self.url,
        on_success=self.send_success,
        on_failure=self.send_failure,
        on_error=self.send_failure,
        timeout=5)


    def send_success(self,req,result):
        toast("action terminé avec succes")


    def send_failure(self,req,result):
        toast("echec veuillez réessayer")








    def decrypt(self,to_encrypt):
        numbers=[int(s) for s in to_encrypt if s.isdigit()]
        crypted=''
        i=0
        for s in to_encrypt:

            crypted_char=chr(ord(s)+numbers[i])  if i % 2 ==0 else chr(ord(s)-numbers[i]*2)
            if not crypted_char.isalnum():
                crypted_char=str(ord(crypted_char))
            if numbers[i] % 2 == 0:
                crypted+=crypted_char
            else:
                crypted=crypted_char+crypted

            i+=1
            if(i==len(numbers)):
                i=0
        return crypted
