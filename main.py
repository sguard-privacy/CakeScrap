from bs4 import BeautifulSoup

# lecture en local des données HTML
fichier = open("SITE_RECETTE/recette.html", "r")
html_content = fichier.read()
fichier.close()

body = BeautifulSoup(html_content, "html.parser")

titre_h1 = body.find("h1")

class_description = body.find("p", class_="description")

div_info = body.find("div", class_="info")
img = div_info = body.find("img")
   


print("Le titre de la page : ", titre_h1.text)
print("La description de la page : ", class_description.text)
print("Le nom de l'image est  : ", img["src"])

print()