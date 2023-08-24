from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.loader import Loader
from kivymd.uix.screen import MDScreen
from requests import get
from kivymd.uix.toolbar import MDTopAppBar
from json import loads

class SliverToolbar(MDTopAppBar):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Headline medium"

class FirstWindow(MDScreen):
	
	def loading_screen(self):
		self.ids.pokemon_image.source = "assets/loading.png"
	
	def UpdatePokemon(self, Pokemon):
		
		try:
			raw_data = get(f"https://pokeapi.co/api/v2/pokemon/{Pokemon}")
			data = loads(raw_data.text)
			
			pokemon_id = data['id']
			name = str(data['name'])[0].upper() + str(data['name'])[1:]
				
			pokemon_img = data['sprites']['front_default']
			self.ids.pokemon_image.source = pokemon_img
			
			self.ids.viewer.text = f"{name}'s Stats"
			
			sm = self.manager.get_screen("PokemonDetails")
			sm.ids.PokeDetailImg.source = pokemon_img
			
			sm.ids.PokeID.text = f"ID : {pokemon_id}"
			sm.ids.PokeName.title = name
			sm.ids.PokeHeight.text = f"HEIGHT : {data['height']}"
			sm.ids.PokeWeight.text = f"WEIGHT : {data['weight']}"
			sm.ids.PokeTypes.text = "TYPE : "
			
			for t in data['types']:
				sm.ids.PokeTypes.text += f"\n~ {t['type']['name']}"
				
			sm.ids.PokeAbilities.text = "ABILITIES :- \n"
			
			for a in data['abilities']:
				sm.ids.PokeAbilities.text += f"\n~ {a['ability']['name']}"
			
			for s in data['stats']:
				if s['stat']['name'] == 'hp':
					sm.ids.PokeHP.text = f"HP : {s['base_stat']}"
					sm.ids.HP_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'attack':
					sm.ids.PokeAttack.text = f"ATTACK : {s['base_stat']}"
					sm.ids.Attack_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'defense':
					sm.ids.PokeDefence.text = f"DEFENCE : {s['base_stat']}"
					sm.ids.Defence_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'special-attack':
					sm.ids.PokeSpecialAttack.text = f"SPECIAL ATTACK : {s['base_stat']}"
					sm.ids.SpAttack_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'special-defense':
					sm.ids.PokeSpecialDefence.text = f"SPECIAL DEFENCE : {s['base_stat']}"
					sm.ids.SpDefence_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'speed':
					sm.ids.PokeSpeed.text = f"SPEED : {s['base_stat']}"
					sm.ids.Speed_bar.value = s['base_stat'] / 200 * 100
			
			sm.ids.PokeBaseExperience.text = f"BASE EXPERIENCE : {data['base_experience']}"
			
		except Exception:
			self.ids.pokemon_image.source = "assets/error.png"
			
	def ClearWindow(self):
		self.ids.search_bar.text = ""
		self.ids.viewer.text = "Pokemon"
		self.ids.pokemon_image.source = "assets/pokeball.gif"
		sm = self.manager.get_screen("PokemonDetails")
		sm.ids.PokeDetailImg.source = "assets/pokeball.gif"		
	
class SecondWindow(MDScreen):
	pass
	
class WindowManager(MDScreenManager):
	pass

class MainApp(MDApp):
	
	def build(self):
		Loader.loading_image = 'assets/loading.png'
		self.theme_cls.theme_style = 'Dark' 
		self.theme_cls.primary_palette = 'Red'
		return Builder.load_file("Design.kv")
		
	def ChangeScreen(self):
		self.root.current = "PokemonLoader"

if __name__ == '__main__':
	MainApp().run()