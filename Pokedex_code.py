from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.loader import Loader
from kivymd.uix.screen import MDScreen
from pokebase import pokemon as pb
from kivymd.uix.toolbar import MDTopAppBar
from pokebase import SpriteResource as pokeimg

class SliverToolbar(MDTopAppBar):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.type_height = "medium"
        self.headline_text = "Headline medium"

class FirstWindow(MDScreen):
	
	def loading_screen(self):
		self.ids.pokemon_image.source = "assets/loading.png"
	
	def UpdatePokemon(self,Pokemon):
		id = False
		
		try:
			pokemon_id = int(Pokemon)
			Pokemon = int(Pokemon)
			id = True
			
		except ValueError:
			pass
			
		try:
			pokemon = pb(Pokemon)
			
			if id == False:
				pokemon_id = pokemon.id
				name = str(pokemon)[0].upper() + str(pokemon)[1:]
				
			else:
				pokemon_id = Pokemon
				name = pokemon.name
				name = str(name)[0].upper() + str(name)[1:]
				
			pokemon_img = pokeimg('pokemon',pokemon_id).url
			self.ids.pokemon_image.source = pokemon_img
			self.ids.viewer.text = f"{name}'s Stats"
			sm = self.manager.get_screen("PokemonDetails")
			sm.ids.PokeDetailImg.source = pokemon_img
			sm.ids.PokeID.text = f"ID : {pokemon_id}"
			sm.ids.PokeName.title = name
			sm.ids.PokeHeight.text = f"HEIGHT : {pokemon.height}"
			sm.ids.PokeWeight.text = f"WEIGHT : {pokemon.weight}"
			sm.ids.PokeTypes.text = "TYPE : "
			
			for t in pokemon.types:
				sm.ids.PokeTypes.text += f"\n~ {t.type}"
				
			sm.ids.PokeAbilities.text = "ABILITIES :- \n"
			
			for a in pokemon.abilities:
				sm.ids.PokeAbilities.text += f"\n~ {a.ability}"
				
			sm.ids.PokeHP.text = f"HP : {pokemon.stats[0].base_stat}"
			sm.ids.PokeAttack.text = f"ATTACK : {pokemon.stats[1].base_stat}"
			sm.ids.PokeDefence.text = f"DEFENCE : {pokemon.stats[2].base_stat}"
			sm.ids.PokeSpecialAttack.text = f"SPECIAL ATTACK : {pokemon.stats[3].base_stat}"
			sm.ids.PokeSpecialDefence.text = f"SPECIAL DEFENCE : {pokemon.stats[4].base_stat}"
			sm.ids.PokeSpeed.text = f"SPEED : {pokemon.stats[5].base_stat}"
			sm.ids.PokeBaseExperience.text = f"BASE EXPERIENCE : {pokemon.base_experience}"
			
		except:
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
