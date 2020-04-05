from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.button import MDFillRoundFlatIconButton,MDIconButton
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelOneLine



class CustomScreen(Screen):
    pass




class CustomScrollView(ScrollView):
    pass




class ButtonContainer(RelativeLayout):
    pass




class CustomButton(MDFillRoundFlatIconButton):
    pass



class CustomPauseButton(MDIconButton):
    pass


class HeaderTitle(BoxLayout):
    pass

class GridButtonsContainer(GridLayout):
    pass


class GridRideauxContainer(GridLayout):
    pass


class TabBox(BoxLayout):
    pass

class EtatLabel(MDLabel):
    pass



class SingleChambre(BoxLayout):
    orientation="vertical"
    def __init__(self,chambre,**kwargs):
        self.chambre=chambre
        self.chambre.get_devices()
        super().__init__(**kwargs)





    def build_local(self):
        box=TabBox(orientation="vertical")
#---------------------------------------- LAMPES       ------------------------------------------------------------------------------
        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Lampes [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridButtonsContainer()

        for lampe in self.chambre.lampes:
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] on [/color]",markup = True)  if lampe.etat else EtatLabel(text="[color=#8B0000] off [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomButton(text=lampe.nom,icon="lightbulb",on_press=lampe.send_commande))
            grid_container.add_widget(container)




        grid_container.height=len(self.chambre.lampes)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDLAMPES       ------------------------------------------------------------------------------


#---------------------------------------- PRISES       ------------------------------------------------------------------------------


        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Prises [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridButtonsContainer()

        for prise in self.chambre.prises:
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] on [/color]",markup = True)  if prise.etat else EtatLabel(text="[color=#8B0000] off [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomButton(text=prise.nom,icon="electric-switch",on_press=prise.send_commande))
            grid_container.add_widget(container)

        grid_container.height=len(self.chambre.prises)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDPRISES       ------------------------------------------------------------------------------


#---------------------------------------- Rideau       ------------------------------------------------------------------------------
        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Rideaux [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridRideauxContainer()

        for rideau in self.chambre.rideaux:
            container=ButtonContainer()
            container.add_widget(CustomButton(text=rideau.nom,icon="arrow-down",on_press=rideau.send_commande))
            grid_container.add_widget(container)
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] ouvert [/color]",markup = True)  if rideau.etat else EtatLabel(text="[color=#8B0000] fermé [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomPauseButton(icon="pause",on_press=rideau.pause))
            grid_container.add_widget(container)
            container=ButtonContainer()
            container.add_widget(CustomButton(text=rideau.nom,icon="arrow-up",on_press=rideau.send_commande2))
            grid_container.add_widget(container)
        grid_container.height=len(self.chambre.rideaux)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDRIDEAU        ------------------------------------------------------------------------------


        box.height=(len(self.chambre.rideaux)*40+40)+(len(self.chambre.prises)*40+40) +(len(self.chambre.lampes)*40+40)+100
        panel=MDExpansionPanel(icon="assets/room.png",
                content=box,
                panel_cls=MDExpansionPanelOneLine(
                    text=self.chambre.nom,
                ))
        return panel






#------------------------------------------       Build INTERNET TAB          ------------------------------------------------------------------------------------------


    def build_internet(self):
        box=TabBox(orientation="vertical")
#---------------------------------------- LAMPES       ------------------------------------------------------------------------------
        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Lampes [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridButtonsContainer()

        for lampe in self.chambre.lampes:
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] on [/color]",markup = True)  if lampe.etat else EtatLabel(text="[color=#8B0000] off [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomButton(text=lampe.nom,icon="lightbulb",on_press=lampe.send_commande_internet))
            grid_container.add_widget(container)




        grid_container.height=len(self.chambre.lampes)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDLAMPES       ------------------------------------------------------------------------------


#---------------------------------------- PRISES       ------------------------------------------------------------------------------


        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Prises [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridButtonsContainer()

        for prise in self.chambre.prises:
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] on [/color]",markup = True)  if prise.etat else EtatLabel(text="[color=#8B0000] off [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomButton(text=prise.nom,icon="electric-switch",on_press=prise.send_commande_internet))
            grid_container.add_widget(container)

        grid_container.height=len(self.chambre.prises)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDPRISES       ------------------------------------------------------------------------------


#---------------------------------------- Rideau       ------------------------------------------------------------------------------
        title=HeaderTitle()
        title.add_widget(MDLabel(text='[color=#6699CC] Rideaux [/color]',markup = True,halign="center",font_style="Subtitle1"))
        box.add_widget(title)



        grid_container=GridRideauxContainer()

        for rideau in self.chambre.rideaux:
            container=ButtonContainer()
            container.add_widget(CustomButton(text=rideau.nom,icon="arrow-down",on_press=rideau.send_commande_internet))
            grid_container.add_widget(container)
            container=ButtonContainer()
            etat_label=EtatLabel(text="[color=#32CD32] ouvert [/color]",markup = True)  if rideau.etat else EtatLabel(text="[color=#8B0000] fermé [/color]",markup = True)
            container.add_widget(etat_label)
            container.add_widget(CustomPauseButton(icon="pause",on_press=rideau.pause_internet))
            grid_container.add_widget(container)
            container=ButtonContainer()
            container.add_widget(CustomButton(text=rideau.nom,icon="arrow-up",on_press=rideau.send_commande2_internet))
            grid_container.add_widget(container)
        grid_container.height=len(self.chambre.rideaux)*40+40

        box.add_widget(grid_container)
#---------------------------------------- ENDRIDEAU        ------------------------------------------------------------------------------


        box.height=(len(self.chambre.rideaux)*40+40)+(len(self.chambre.prises)*40+40) +(len(self.chambre.lampes)*40+40)+100
        panel=MDExpansionPanel(icon="assets/room.png",
                content=box,
                panel_cls=MDExpansionPanelOneLine(
                    text=self.chambre.nom,
                ))
        return panel
