import random

restaurant = ["Peters Brauhaus at Martinsviertel",
				"Lommerzheim at Deutz",
				"Bei Oma Kleinmann at Rathenauviertel",
				"FRÜH am Dom at Martinsviertel",
				"Die fette Kuh at Südstadt",
				"Momotaro at Apostelnviertel",
				"Kebapland at Ehrenfeld",
				"Freddy Schilling at Rathenauviertel"
				"Beef Brothers at Belgisches Viertel",
				"Mongo’s at Deutz",
				"Hans Im Glück at Apostelnviertel",
				"Brauerei Päffgen at Gereonsviertel"
				"Vapiano at Deutz"
				"XII Apostel at Martinsviertel",
				"Das kleine Steakhaus at Martinsviertel",
				"Bulgogi-Haus at Weidenpesch",
				"Habibi at Rathenauviertel"]

random_restaurant	= random.choice(restaurant)

print(f"It looks like you're in cologne hungry and not sure what to have for dinner. How about {random_restaurant}?")