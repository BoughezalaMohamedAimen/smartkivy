from kivymd.toast import toast
from kivy.network.urlrequest import UrlRequest
import sqlite3 as sql

class Synchronizer:
    def __init__(self,chambres=None,devices=None,headers=None,app=None):
        self.chambres=chambres
        self.devices=devices
        self.headers=headers
        self.app_to_reload=app

    def synch_chambres(self,url):
        req = UrlRequest(url=url,
        on_success=self.save_chambres,
        on_failure=self.sync_failure,
        on_error=self.sync_failure,
        timeout=5)

    def synch_chambres_internet(self,url):
        req = UrlRequest(url=url,
        on_success=self.save_chambres_internet,
        on_failure=self.sync_failure,
        on_error=self.sync_failure,
        req_headers=self.headers,
        timeout=5)

    def save_chambres(self,req,result):
        con=sql.connect('db.db')
        cur=con.cursor()
        cur.execute("""DELETE  FROM chambres""")
        con.commit()
        cur=con.cursor()

        for single in result:
            cur.execute("""INSERT INTO chambres (id,nom) VALUES (?,?)""",(single['id'],single['nom']))

        con.commit()
        con.close()

    def save_chambres_internet(self,req,result):
        con=sql.connect('db.db')
        cur=con.cursor()
        cur.execute("""DELETE  FROM chambres""")
        con.commit()
        cur=con.cursor()

        for single in result:
            cur.execute("""INSERT INTO chambres (id,nom) VALUES (?,?)""",(single['local_id'],single['nom']))

        con.commit()
        con.close()


    def sync_failure(self,req,result):
        print(result)
        toast("erreur veuillez réessayer")



    def synch_devices(self,url):
        req = UrlRequest(url=url,
        on_success=self.save_devices,
        on_failure=self.sync_failure,
        on_error=self.sync_failure,
        timeout=5)

    def synch_devices_internet(self,url):
        req = UrlRequest(url=url,
        on_success=self.save_devices_internet,
        on_failure=self.sync_failure,
        on_error=self.sync_failure,
        req_headers=self.headers,
        timeout=5)

    def save_devices(self,req,result):
        con=sql.connect('db.db')
        cur=con.cursor()
        cur.execute("""DELETE  FROM commandes """)
        con.commit()
        cur=con.cursor()

        for single in result:
            cur.execute("""INSERT INTO commandes (id,nom,type,etat,chambre) VALUES (?,?,?,?,?)""",(single['id'],single['nom'],single['type'],single['etat'],single['chambre']))

        con.commit()
        con.close()
        self.app_to_reload.reload_chambres()
        toast("synchronization terminé avec success")


    def save_devices_internet(self,req,result):
        con=sql.connect('db.db')
        cur=con.cursor()
        cur.execute("""DELETE  FROM commandes """)
        con.commit()
        cur=con.cursor()

        for single in result:
            cur.execute("""INSERT INTO commandes (id,nom,type,etat,chambre) VALUES (?,?,?,?,?)""",(single['local_id'],single['nom'],single['type'],single['etat'],single['chambre_local']))

        con.commit()
        con.close()
        self.app_to_reload.reload_chambres()
        toast("synchronization terminé avec success")
