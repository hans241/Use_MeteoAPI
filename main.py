import requests

# Demande à l'utilisateur d'entrer le nom d'une ville
cityName = input("Mettre le nom de la ville : ")

langage = "fr"  # Définition de la langue des résultats (français)
clef = "b22bd5df0fe72865f3e46c264b021e46"  # Clé API pour accéder aux services d'OpenWeatherMap

# Construction de l'URL de l'API pour obtenir les informations météo de la ville spécifiée
apilien = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={clef}&lang={langage}&units=metric"

# Envoi de la requête GET à l'API et conversion de la réponse en format JSON
json = requests.get(apilien).json()

# Vérification si la réponse contient des données sur la météo
if json['cod'] == 200:
    # Extraction des informations pertinentes
    description = json['weather'][0]['description']
    temperature = json['main']['temp']  # Température en degrés Celsius
    humidity = json['main']['humidity']  # Humidité en pourcentage
    wind_speed = json['wind']['speed']  # Vitesse du vent en m/s

    # Affichage des informations météo
    print(f"Météo à {cityName} :")
    print(f"Description : {description}")
    print(f"Température : {temperature}°C")
    print(f"Hygrométrie : {humidity}%")
    print(f"Vitesse du vent : {wind_speed} m/s")
else:
    print("Erreur : la ville n'a pas été trouvée.")
