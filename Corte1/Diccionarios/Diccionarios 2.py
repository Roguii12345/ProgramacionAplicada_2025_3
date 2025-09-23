#### Get A Key
# you can access the values in it by providing the key:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
# Se crea un diccionario con edificios y sus alturas.

print(building_heights["Burj Khalifa"]) # Prints 828
# Muestra el valor asociado a la clave "Burj Khalifa" → 828.

print(building_heights["Ping An"]) # Prints 599
# Muestra el valor de "Ping An" → 599.

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# Diccionario donde cada elemento zodiacal (agua, fuego, tierra, aire) tiene una lista de signos.

print(zodiac_elements["earth"])
# Imprime la lista asociada a "earth": ["Taurus", "Virgo", "Capricorn"].

print(zodiac_elements["fire"])
# Imprime ["Aries", "Leo", "Sagittarius"].

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights["Landmark 81"])
# ERROR → KeyError porque "Landmark 81" no existe en el diccionario.

key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])
# No se ejecuta porque "Landmark 81" no está en el diccionario.

zodiac_elements["energy"] = "Not a Zodiac element"
# Agrega una nueva clave "energy" con el valor "Not a Zodiac element".

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])
# Sí se imprime → "Not a Zodiac element".

building_heights.get("Shanghai Tower")
# Devuelve 632 (sin error si existe la clave).

building_heights.get("My House")
# Devuelve None porque no existe "My House".


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
# Diccionario con usuarios y sus IDs.

user_ids.get("teraCoder")
# Devuelve 100019.

if user_ids.get("teraCoder") == None:
   tc_id = 1000
else: 
   tc_id = user_ids.get("teraCoder")
print(tc_id)
# Como sí existe, imprime 100019.

if user_ids.get("superStackSmash") == None:
     stack_id = 100000
print(stack_id)
# Como NO existe, se crea stack_id = 100000 y eso se imprime.

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))
# Elimina la clave 320291 y devuelve su valor → "Gift Basket".

print(raffle)
# Ahora ya no contiene el 320291.

print(raffle.pop(100000, "No Prize"))
# No existe la clave, devuelve "No Prize".

print(raffle)
# Igual que antes, no cambia.

print(raffle.pop(872921, "No Prize"))
# Elimina "Concert Tickets".

print(raffle)
# Ya no aparece 872921.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
# Elimina "stamina grains" (15) y lo suma a health_points → ahora 35.

health_points += available_items.pop("power stew", 0)
# Elimina "power stew" (30) → ahora 65.

health_points += available_items.pop("mystic bread", 0)
# No existe, devuelve 0, no cambia.

print(available_items)
# Ya no están "stamina grains" ni "power stew".

print(health_points)
# Imprime 65.

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))
# Imprime todas las claves (nombres).

for student in test_scores.keys():
  print(student)
# Recorre e imprime cada clave una por una.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)
# Imprime los objetos con las claves (usuarios y temas).

for score_list in test_scores.values():
  print(score_list)
# Recorre e imprime todas las listas de notas.

total_exercises = 0
for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)
# Suma todas las cantidades de ejercicios → 115.

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
# Recorre claves y valores → imprime frases con cada empresa y su valor.

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
# Recorre cada profesión y porcentaje → imprime una frase descriptiva.
