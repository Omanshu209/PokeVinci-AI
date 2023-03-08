from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.loader import Loader
from kivymd.uix.screen import MDScreen
from pokebase import pokemon as pb
from kivymd.uix.toolbar import MDTopAppBar
from pokebase import SpriteResource as pokeimg

KV="""
#:import SliverToolbar __main__.SliverToolbar


WindowManager:
	FirstWindow:
	SecondWindow:
		
<FirstWindow>:
	name:"PokemonLoader"
	
	MDScreen:
		
		MDTextField:
			id:search_bar
			mode:'round' 
			hint_text:"Enter Pokemon's Name/ID"
			icon_left:'pokeball' 
			pos_hint:{'center_y':.96}
			size_hint:.9,None
			padding:15
			
		MDRoundFlatButton:
			text:'PokeSearch' 
			pos_hint:{'center_x':.5,'center_y':.89}
			size_hint:.2,.06
			on_press:
				root.loading_screen()
			on_release:
				root.UpdatePokemon(root.ids.search_bar.text.lower())

		MDRoundFlatButton:
			text:'Clear' 
			pos_hint:{'center_x':.95,'center_y':.96}
			size_hint:.09,.004
			on_release:
				root.ClearWindow()
		
		MDCard:
			size_hint:.95,.72
			pos_hint:{'center_x':.5,'center_y':.47}
			elevation:7
			padding:25
			spacing:25
			orientation:'vertical' 
			
			AsyncImage:
			    id:pokemon_image
			    source:"pokeball.png"
			    pos_hint:{"center_x":.5}
			    allow_stretch:True
    		    
    		MDRectangleFlatButton:
    			id:viewer
    			text:"Pokemon"
    			size_hint:.4,.1
    			pos_hint:{"center_x":.5}
    			on_release:
    				app.root.current = "PokemonDetails"
                	root.manager.transition.direction = "left"
		
		MDRectangleFlatButton:
			text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
			pos_hint:{'center_x':.5,'center_y':0.045}
			size_hint:1,.05
			bold:True
	
<SecondWindow>:
	name:"PokemonDetails"
	MDSliverAppbar:
        background_color: "2d4a50"
        toolbar_cls: SliverToolbar()

        MDSliverAppbarHeader:

            MDRelativeLayout:

                AsyncImage:
                    id:PokeDetailImg
                    allow_stretch:True
                    source: "pokeball.png"

        MDSliverAppbarContent:
            id: content
            orientation: "vertical"
            padding: "12dp"
            spacing: "12dp"
            adaptive_height: True
            MDCard:
            	size_hint_y: None
			    height: "650dp"
			    padding: "4dp"
			    radius: 12
			
			    MDBoxLayout:
			        orientation: "vertical"
			        adaptive_height: True
			        spacing: "6dp"
			        padding: "12dp", 0, 0, 0
			        pos_hint: {"center_y": .5}
			        
			        MDTopAppBar:
			        	id:PokeName
			        	title:"Pokemon"
			        
			        MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					    	
					MDLabel:
					    id:PokeID
					    text: "ID : "
					    font_style: "Button"
					    bold: True
					    adaptive_height: True
					    
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeTypes
					    text: "TYPE : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					    
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					    
					MDLabel:
					    id:PokeHeight
					    text: "HEIGHT : "
					    font_style: "Button"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeWeight
					    text: "WEIGHT : "
					    font_style: "Button"
					    bold:True
					    adaptive_height: True
					    
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True        
					
					MDLabel:
					    id:PokeAbilities
					    text: "ABILITY : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeHP
					    text: "HP : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					 
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True    
					   
					MDLabel:
					    id:PokeAttack
					    text: "ATTACK : "
					    font_style: "Button"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeDefence
					    text: "DEFENCE : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					 
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True    
					     
					MDLabel:
					    id:PokeSpecialAttack
					    text: "SPECIAL ATTACK : "
					    font_style: "Button"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeSpecialDefence
					    text: "SPECIAL DEFENCE : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True    
					    
					MDLabel:
					    id:PokeSpeed
					    text: "SPEED : "
					    font_style: "Button"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
					
					MDLabel:
					    id:PokeBaseExperience
					    text: "BASE EXPERIENCE : "
					    font_style: "Overline"
					    bold:True
					    adaptive_height: True
					
					MDLabel:
			        	text: "--------------------"
					    font_style: "Overline"
					    bold: True
					    adaptive_height: True
"""

class SliverToolbar(MDTopAppBar):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Headline medium"
        self.left_action_items = [["arrow-left", lambda x: self.ChangeScreen()]]
        
    def ChangeScreen(self):
    	pass

class FirstWindow(MDScreen):
	
	def loading_screen(self):
		self.ids.pokemon_image.source="loading.gif"
	
	def UpdatePokemon(self,Pokemon):
		id=False
		try:
			pokemon_id=int(Pokemon)
			Pokemon=int(Pokemon)
			id=True
		except ValueError:
			pass
		try:
			pokemon=pb(Pokemon)
			if id==False:
				pokemon_id=pokemon.id
				name=str(pokemon)[0].upper()+str(pokemon)[1:]
			else:
				pokemon_id=Pokemon
				name=pokemon.name
				name=str(name)[0].upper()+str(name)[1:]
			pokemon_img=pokeimg('pokemon',pokemon_id).url
			self.ids.pokemon_image.source=pokemon_img
			self.ids.viewer.text=f"{name}'s Stats"
			sm=self.manager.get_screen("PokemonDetails")
			sm.ids.PokeDetailImg.source=pokemon_img
			sm.ids.PokeID.text=f"ID : {pokemon_id}"
			sm.ids.PokeName.title=name
			sm.ids.PokeHeight.text=f"HEIGHT : {pokemon.height}"
			sm.ids.PokeWeight.text=f"WEIGHT : {pokemon.weight}"
			sm.ids.PokeTypes.text="TYPE : "
			for t in pokemon.types:
				sm.ids.PokeTypes.text+=f"\n~ {t.type}"
			sm.ids.PokeAbilities.text="ABILITIES :- \n"
			for a in pokemon.abilities:
				sm.ids.PokeAbilities.text+=f"\n~ {a.ability}"
			sm.ids.PokeHP.text=f"HP : {pokemon.stats[0].base_stat}"
			sm.ids.PokeAttack.text=f"ATTACK : {pokemon.stats[1].base_stat}"
			sm.ids.PokeDefence.text=f"DEFENCE : {pokemon.stats[2].base_stat}"
			sm.ids.PokeSpecialAttack.text=f"SPECIAL ATTACK : {pokemon.stats[3].base_stat}"
			sm.ids.PokeSpecialDefence.text=f"SPECIAL DEFENCE : {pokemon.stats[4].base_stat}"
			sm.ids.PokeSpeed.text=f"SPEED : {pokemon.stats[5].base_stat}"
			sm.ids.PokeBaseExperience.text=f"BASE EXPERIENCE : {pokemon.base_experience}"
		except:
			self.ids.pokemon_image.source="pokeball.png"
	def ClearWindow(self):
		self.ids.search_bar.text=""
		self.ids.viewer.text="Pokemon"
		self.ids.pokemon_image.source="pokeball.png"
		sm=self.manager.get_screen("PokemonDetails")
		sm.ids.PokeDetailImg.source="pokeball.png"		
	
class SecondWindow(MDScreen):
	pass
	
class WindowManager(MDScreenManager):
	pass

class MainApp(MDApp):
	
	def build(self):
		Loader.loading_image = 'loading.gif'
		self.theme_cls.theme_style='Dark' 
		self.theme_cls.primary_palette='Red'
		return Builder.load_string(KV)

if __name__=='__main__':
	MainApp().run()