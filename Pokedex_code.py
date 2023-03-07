from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.loader import Loader
from kivymd.uix.screen import MDScreen
from pokebase import pokemon as pb
from pokebase import SpriteResource as pokeimg

KV="""
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
		
		MDRectangleFlatButton:
			text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
			pos_hint:{'center_x':.5,'center_y':0.045}
			size_hint:1,.05
			bold:True
	
<SecondWindow>:
	name:"PokemonDetails"
"""

class FirstWindow(MDScreen):
	
	def loading_screen(self):
		self.ids.pokemon_image.source="loading.gif"
	
	def UpdatePokemon(self,Pokemon):
		id=False
		try:
			pokemon_id=int(Pokemon)
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
		except:
			self.ids.pokemon_image.source="pokeball.png"
		#Details=requests.get(f"https://pokeapi.co/api/v2/pokemon/{Pokemon}")
	
	def ClearWindow(self):
		self.ids.search_bar.text=""
		self.ids.viewer.text="Pokemon"
		self.ids.pokemon_image.source="pokeball.png"
	
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