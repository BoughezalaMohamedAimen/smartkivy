import sqlite3 as sql
from kivy.network.urlrequest import UrlRequest
import urllib
from kivymd.toast import toast

class UrlsList:
    def __init__(self):
        self.headers=""
        self.headers_json=""
        
        con=sql.connect("db.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM adresse""")
        result=cur.fetchall()


        for local,internet in result:
            self.local=str(local)
            self.internet=str(internet)

        cur.execute("""SELECT * FROM token""")
        result=cur.fetchall()
        for token in result:
            self.headers={'Authorization': 'Token '+token[0]}
            self.headers_json={
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token '+token[0],
            }

        con.close()

        self.init_urls()




    def init_urls(self):
        self.local_send_commande=self.local+"/chambres/commande/"
        self.local_chambres_sync=self.local+"/chambres/api?format=json"
        self.local_devices_sync=self.local+"/chambres/commandes/api?format=json"
        self.chalenge_url=self.local+"/chambres/chalenge"


        self.internet_send_commande=self.internet+"/chambres/todo/api/"
        self.internet_chambres_sync=self.internet+"/chambres/api?format=json"
        self.internet_devices_sync=self.internet+"/chambres/commandes/api?format=json"
        self.internet_auth=self.internet+"/api-auth/"


    def set_network(self,local,internet):
        con=sql.connect("db.db")
        cur=con.cursor()
        cur.execute("""DELETE FROM adresse""")
        con.commit()
        self.local=local
        self.internet=internet
        cur.execute("""INSERT INTO adresse (local,internet) VALUES (?,?)""",(self.local,self.internet))
        con.commit()
        con.close()
        self.init_urls()
        toast("Sauvegardé avec succès")



    def login(self,username,password):
        headers={'Content-type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json'}
        body=urllib.parse.urlencode({'username':username, 'password':password })

        req = UrlRequest(url=self.internet_auth,
        on_success=self.login_success,
        on_failure=self.login_failure,
        on_error=self.login_failure,
        req_body=body,
        req_headers=headers,
        timeout=5
        )


    def login_success(self,req,result):
        con=sql.connect('db.db')
        cur=con.cursor()
        cur.execute("""DELETE  FROM token """)
        con.commit()
        cur.execute("""INSERT INTO token  VALUES (?)""",(result['token'],))
        con.commit()
        con.close()
        self.headers={'Authorization': 'Token '+result['token']}
        toast("connecté avec success")

    def login_failure(self,req,result):
        toast("erreur veuillez réessayer")
