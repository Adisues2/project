from googletrans import Translator
 
translator = Translator()

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

RESULT = translator.translate(french_words,src = "fr", des = "en")

for i in RESULT:
    print(f"{i.origin} => {i.text}")

