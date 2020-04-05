from kivy.lang import Builder
from kivymd.app import MDApp

from mytemplates.base import KV
from mytemplates.menu import *


from models.chambre import Chambre
from models.synchronizer import Synchronizer
from models.urls import UrlsList
from mytemplates.single_chambre import SingleChambre

from kivymd.toast import toast





class SmartApp(MDApp):

    def login(self):
        self.urls_list.login(username=self.root.ids.user.text,password=self.root.ids.password.text)

    def network_config(self):
        self.urls_list.set_network(local=self.root.ids.wifi.text,internet=self.root.ids.internet.text)

    def synch_local(self):
        try:
            self.synchronizer.synch_chambres(self.urls_list.local_chambres_sync)
            self.synchronizer.synch_devices(self.urls_list.local_devices_sync)
        except:
            toast("erreur veuillez reéssayer")

    def synch_internet(self):
        try:
            self.synchronizer.headers=self.urls_list.headers
            self.synchronizer.synch_chambres_internet(self.urls_list.internet_chambres_sync)
            self.synchronizer.synch_devices_internet(self.urls_list.internet_devices_sync)
        except:
            toast("erreur veuillez reéssayer")





    def reload_chambres(self):
        self.root.ids.local_tab.clear_widgets(self.root.ids.local_tab.children)
        self.root.ids.internet_tab.clear_widgets(self.root.ids.local_tab.children)



        self.chambres=Chambre().all()
        self.urls_list=UrlsList()
        self.synchronizer=Synchronizer(headers=self.urls_list.headers,app=self)

        self.root.ids.wifi.text=self.urls_list.local
        self.root.ids.internet.text=self.urls_list.internet






        for chambre in self.chambres:
            single_chambre=SingleChambre(chambre)
            self.root.ids.local_tab.add_widget(single_chambre.build_local())
            self.root.ids.internet_tab.add_widget(single_chambre.build_internet())




    def build(self):
        self.theme_cls.primary_palette ="Blue"
        # self.theme_cls.accent_palette ="BlueGray"
        return Builder.load_string(KV)


    def on_start(self):
        self.reload_chambres()




    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        pass

smart_app=SmartApp()
smart_app.run()
