import sqlite3 as sql
from .device import Device


class Chambre:

    def __init__(self,id=None,nom=None,devices=None):
        self.id=id
        self.nom=nom
        self.devices=devices
        self.lampes=[]
        self.prises=[]
        self.rideaux=[]

    def all(self):
        con=sql.connect("db.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM chambres""")
        result=cur.fetchall()
        chambres=[]
        for id,nom in result:
            chambres.append(Chambre(id=id,nom=nom))

        con.close()
        return chambres

    def get_devices(self):
        con=sql.connect("db.db")
        cur=con.cursor()
        cur.execute("""SELECT * FROM commandes WHERE chambre=? """,(self.id,))
        result=cur.fetchall()
        self.devices=[]

        for id,nom,type,etat,chambre in result:
            if type=="Lampe":
                self.lampes.append(Device(id=id,nom=nom,etat=etat,chambre=chambre,type=type))
            if type=="Prise":
                self.prises.append(Device(id=id,nom=nom,etat=etat,chambre=chambre,type=type))
            if type=="Rideau":
                self.rideaux.append(Device(id=id,nom=nom,etat=etat,chambre=chambre,type=type))
        con.close()

          
