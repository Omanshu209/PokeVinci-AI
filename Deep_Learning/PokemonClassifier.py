import torch
import torch.nn as nn
from torchvision import transforms, models

labels : dict = {'Abra': 0, 'Aerodactyl': 1, 'Alakazam': 2, 'Alolan Sandslash': 3, 'Arbok': 4, 'Arcanine': 5, 'Articuno': 6, 'Beedrill': 7, 'Bellsprout': 8, 'Blastoise': 9, 'Bulbasaur': 10, 'Butterfree': 11, 'Caterpie': 12, 'Chansey': 13, 'Charizard': 14, 'Charmander': 15, 'Charmeleon': 16, 'Clefable': 17, 'Clefairy': 18, 'Cloyster': 19, 'Cubone': 20, 'Dewgong': 21, 'Diglett': 22, 'Ditto': 23, 'Dodrio': 24, 'Doduo': 25, 'Dragonair': 26, 'Dragonite': 27, 'Dratini': 28, 'Drowzee': 29, 'Dugtrio': 30, 'Eevee': 31, 'Ekans': 32, 'Electabuzz': 33, 'Electrode': 34, 'Exeggcute': 35, 'Exeggutor': 36, 'Farfetchd': 37, 'Fearow': 38, 'Flareon': 39, 'Gastly': 40, 'Gengar': 41, 'Geodude': 42, 'Gloom': 43, 'Golbat': 44, 'Goldeen': 45, 'Golduck': 46, 'Golem': 47, 'Graveler': 48, 'Grimer': 49, 'Growlithe': 50, 'Gyarados': 51, 'Haunter': 52, 'Hitmonchan': 53, 'Hitmonlee': 54, 'Horsea': 55, 'Hypno': 56, 'Ivysaur': 57, 'Jigglypuff': 58, 'Jolteon': 59, 'Jynx': 60, 'Kabuto': 61, 'Kabutops': 62, 'Kadabra': 63, 'Kakuna': 64, 'Kangaskhan': 65, 'Kingler': 66, 'Koffing': 67, 'Krabby': 68, 'Lapras': 69, 'Lickitung': 70, 'Machamp': 71, 'Machoke': 72, 'Machop': 73, 'Magikarp': 74, 'Magmar': 75, 'Magnemite': 76, 'Magneton': 77, 'Mankey': 78, 'Marowak': 79, 'Meowth': 80, 'Metapod': 81, 'Mew': 82, 'Mewtwo': 83, 'Moltres': 84, 'MrMime': 85, 'Muk': 86, 'Nidoking': 87, 'Nidoqueen': 88, 'Nidorina': 89, 'Nidorino': 90, 'Ninetales': 91, 'Oddish': 92, 'Omanyte': 93, 'Omastar': 94, 'Onix': 95, 'Paras': 96, 'Parasect': 97, 'Persian': 98, 'Pidgeot': 99, 'Pidgeotto': 100, 'Pidgey': 101, 'Pikachu': 102, 'Pinsir': 103, 'Poliwag': 104, 'Poliwhirl': 105, 'Poliwrath': 106, 'Ponyta': 107, 'Porygon': 108, 'Primeape': 109, 'Psyduck': 110, 'Raichu': 111, 'Rapidash': 112, 'Raticate': 113, 'Rattata': 114, 'Rhydon': 115, 'Rhyhorn': 116, 'Sandshrew': 117, 'Sandslash': 118, 'Scyther': 119, 'Seadra': 120, 'Seaking': 121, 'Seel': 122, 'Shellder': 123, 'Slowbro': 124, 'Slowpoke': 125, 'Snorlax': 126, 'Spearow': 127, 'Squirtle': 128, 'Starmie': 129, 'Staryu': 130, 'Tangela': 131, 'Tauros': 132, 'Tentacool': 133, 'Tentacruel': 134, 'Vaporeon': 135, 'Venomoth': 136, 'Venonat': 137, 'Venusaur': 138, 'Victreebel': 139, 'Vileplume': 140, 'Voltorb': 141, 'Vulpix': 142, 'Wartortle': 143, 'Weedle': 144, 'Weepinbell': 145, 'Weezing': 146, 'Wigglytuff': 147, 'Zapdos': 148, 'Zubat': 149}

class PokemonClassifier:
	
	def __init__(self, model_path = "Model/PokemonClassifier_CNN_Model.pt"):
		
		self.transform = transforms.Compose(
			[
				transforms.Resize((250, 250)),
				transforms.ToTensor(),
				
				transforms.Normalize(
					mean = [0.485, 0.456, 0.406],
					std = [0.229, 0.224, 0.225]
				)
			]
		)
		
		self.device = "cuda" if torch.cuda.is_available() else "cpu"
		self.Model = self.load_model(model_path)
	
	def load_model(self, model_path):
		Model = models.resnet18(pretrained = True)
		
		for p in Model.parameters():
			p.requires_grad = False
		
		Model.fc = nn.Linear(512, 150)
		
		Model.load_state_dict(
			torch.load(
				model_path, 
				map_location = self.device
			)
		)
		
		return Model
	
	def transform_image(self, image):
		transformed_image = self.transform(image.convert("RGB"))
		return transformed_image
	
	def predict(self, transformed_image):
		self.Model.eval()
		with torch.no_grad():
			y_pred = self.Model(transformed_image.unsqueeze(0).to(self.device))
			y_pred_tensor = torch.max(y_pred, 1)[1]
			y_pred_string = [i for i in labels if labels[i] == y_pred_tensor][0]
		return y_pred_string