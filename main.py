import requests
from flask import Flask, render_template

app = Flask(__name__)

#API Endpoint for JSON Champions data and images
DATA_URL = f"https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/champion.json"
ICON_URL = f"https://ddragon.leagueoflegends.com/cdn/16.5.1/img/champion"

@app.route("/")
def index():

    #Ensures API's json data gets stored in the 'data' variable
    data = requests.get(DATA_URL).json()

    #Allows access to individual champions data dictionary
    champions_data = data.get("data", {})

    champions = []

    #Loops through each champion, appending the accessed data keys in the empty list
    for champ in champions_data.values():
        champion = {
            "id": champ["id"],
            "name": champ["name"],
            "title": champ["title"],
            "tags": champ["tags"],
            "icon": f"{ICON_URL}/{champ['id']}.png"
        }
        champions.append(champion)

    #Sends Python list 'champions' to index.html as HTML variable 'champions'
    return render_template(
        "index.html",
        champions = champions
    )

if __name__ == "__main__":
    app.run(debug=True)