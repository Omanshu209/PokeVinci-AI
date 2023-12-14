from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.loader import Loader
from requests import get
from kivymd.uix.toolbar import MDTopAppBar
from json import loads
from PIL import Image
from Deep_Learning.PokemonClassifier import PokemonClassifier

classifier = PokemonClassifier(model_path = "Deep_Learning/Model/PokemonClassifier_CNN_Model.pt")

class SliverToolbar(MDTopAppBar):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Headline medium"

class MainApp(MDApp):
	
	def build(self):
		Loader.loading_image = 'assets/loading.png'
		self.theme_cls.theme_style = 'Dark' 
		self.theme_cls.primary_palette = 'Red'
		return Builder.load_file("Design.kv")
	
	def loading_screen(self):
		self.root.ids.pokemon_image.source = "assets/loading.png"
	
	def UpdatePokemon(self, Pokemon):
		try:
			raw_data = get(f"https://pokeapi.co/api/v2/pokemon/{Pokemon}")
			data = loads(raw_data.text)
			
			pokemon_id = data['id']
			name = str(data['name'])[0].upper() + str(data['name'])[1:]
				
			pokemon_img = data['sprites']['front_default']
			self.root.ids.pokemon_image.source = pokemon_img
			
			self.root.ids.viewer.text = name
			self.root.ids.PokeDetailImg.source = pokemon_img
			
			self.root.ids.PokeID.text = f"ID : {pokemon_id}"
			self.root.ids.PokeName.title = name
			self.root.ids.PokeHeight.text = f"HEIGHT : {data['height']}"
			self.root.ids.PokeWeight.text = f"WEIGHT : {data['weight']}"
			self.root.ids.PokeTypes.text = "TYPE : "
			
			for t in data['types']:
				self.root.ids.PokeTypes.text += f"\n~ {t['type']['name']}"
				
			self.root.ids.PokeAbilities.text = "ABILITIES :- \n"
			
			for a in data['abilities']:
				self.root.ids.PokeAbilities.text += f"\n~ {a['ability']['name']}"
			
			for s in data['stats']:
				if s['stat']['name'] == 'hp':
					self.root.ids.PokeHP.text = f"HP : {s['base_stat']}"
					self.root.ids.HP_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'attack':
					self.root.ids.PokeAttack.text = f"ATTACK : {s['base_stat']}"
					self.root.ids.Attack_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'defense':
					self.root.ids.PokeDefence.text = f"DEFENCE : {s['base_stat']}"
					self.root.ids.Defence_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'special-attack':
					self.root.ids.PokeSpecialAttack.text = f"SPECIAL ATTACK : {s['base_stat']}"
					self.root.ids.SpAttack_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'special-defense':
					self.root.ids.PokeSpecialDefence.text = f"SPECIAL DEFENCE : {s['base_stat']}"
					self.root.ids.SpDefence_bar.value = s['base_stat'] / 200 * 100
				elif s['stat']['name'] == 'speed':
					self.root.ids.PokeSpeed.text = f"SPEED : {s['base_stat']}"
					self.root.ids.Speed_bar.value = s['base_stat'] / 200 * 100
			
			self.root.ids.PokeBaseExperience.text = f"BASE EXPERIENCE : {data['base_experience']}"
			
		except Exception:
			self.root.ids.pokemon_image.source = "assets/error.png"
			
	def ClearWindow(self):
		self.root.ids.search_bar.text = ""
		self.root.ids.viewer.text = "Pokemon"
		self.root.ids.pokemon_image.source = "assets/pokeball.gif"
		#sm = self.manager.get_screen("PokemonDetails")
		self.root.ids.PokeDetailImg.source = "assets/pokeball.gif"
	
	def capture_image(self):
		self.root.ids.camera.export_to_png("assets/clicked_image.png")
		image = classifier.transform_image(Image.open("assets/clicked_image.png"))
		self.root.ids.prediction.text = classifier.predict(image)

if __name__ == '__main__':
	MainApp().run()