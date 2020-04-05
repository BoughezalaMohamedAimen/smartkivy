KV="""

<HeaderTitle>:
    size_hint:1,None
    height:"70dp"

<GridButtonsContainer>:
    cols:2
    size_hint:1,None


<GridRideauxContainer>:
    cols:3
    size_hint:1,None



# <CustomScrollView>:
#     spacing:"30dp"
#     do_scroll_x: False
#     do_scroll_y: True



<ButtonContainer>:
    size_hint:1,None
    height:"90dp"
    orientation:"vertical"

<EtatLabel>:
    color:1,1,0,.5
    halign:"center"
    pos_hint: {"center_x": .5, "center_y": 1}
    text:"on"




<TabBox>:
    size_hint_y:None
    height:self.minimum_height



<CustomButton>:
    pos_hint: {"center_x": .5, "center_y": .5}




<CustomPauseButton>:
    canvas.before:
        Color:
            rgba: app.theme_cls.primary_color
        Ellipse:
            pos: self.pos
            size: self.size
    pos_hint: {"center_x": .5, "center_y": .5}







BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: "My House"
        elevation: 10
        left_action_items: [['home-automation', lambda x: print()]]

    MDTabs:
        id:main_tabs
        on_tab_switch: app.on_tab_switch(*args)

        Tab:
            text:"rss"
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
                scroll_timeout:15
                scroll_distance:5
                GridLayout:
                    id:local_tab
                    cols:1
                    size_hint_y:None
                    height:self.minimum_height


        Tab:
            text:"earth"
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True
                scroll_timeout:15
                scroll_distance:5
                GridLayout:
                    id:internet_tab
                    cols:1
                    size_hint_y:None
                    height:self.minimum_height







        Tab:
            text:"settings"
            BoxLayout:
                orientation: 'vertical'
                size_hint:1,.5
                pos_hint:{"center_x":.5,"center_y":.7}
                padding:"40dp"
                spacing:"10dp"

                MDLabel:
                    text:"PARAMETRE RESEAU"
                    halign: "center"

                MDTextField:
                    id: wifi
                    hint_text: "adresse ip serveur local"
                    helper_text: "example: http://192.168.1.30"
                    helper_text_mode: "on_focus"

                MDTextField:
                    id:internet
                    hint_text: "adresse site internet"
                    helper_text: "adresse site web de synchronization"
                    helper_text_mode: "on_focus"

                MDFillRoundFlatIconButton:
                    icon: "content-save"
                    text:"Sauvgarder"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    on_release:app.network_config()


        Tab:
            text:"sync"
            GridLayout:
                cols:2
                RelativeLayout:
                    MDFillRoundFlatIconButton:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon:"wifi"
                        text:"local"
                        on_release:app.synch_local()

                RelativeLayout:
                    MDFillRoundFlatIconButton:
                        pos_hint: {"center_x": .5, "center_y": .5}
                        icon:"earth"
                        text:"internet"
                        on_release:app.synch_internet()

        Tab:
            text:"account"

            BoxLayout:
                orientation: 'vertical'
                size_hint:1,.5
                pos_hint: {"center_x": .5,"center_y": .7}
                spacing:"10dp"
                padding:"40dp"
                MDLabel:
                    text:"MON COMPTE"
                    halign: "center"

                MDTextField:
                    id: user
                    hint_text: "Identifiant"
                    helper_text: "Votre compte sur le site"
                    helper_text_mode: "on_focus"

                MDTextField:
                    id:password
                    hint_text: "Mot de passe"
                    password:True
                    helper_text: "veuillez saisir votre mot de passe ici"
                    helper_text_mode: "on_focus"

                MDFillRoundFlatIconButton:
                    icon: "login-variant"
                    text:"Connexion"
                    pos_hint: {"center_x": .5,"center_y": 1}
                    on_release:app.login()
"""
