import requests
from flask import Flask, render_template

app = Flask(__name__)

#API Endpoint for JSON Champions data and images
DATA_URL = f"https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/champion.json"
ICON_URL = f"https://ddragon.leagueoflegends.com/cdn/16.5.1/img/champion"

#API Endpoint for Champion specific detail, will append Champ ('...champion/Aatrox.json')
CHAMPION_DETAIL_URL = "https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/champion"

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

#Route for champion-specific page with required champ_id
@app.route("/champion-page/<champ_id>")
def champion_page(champ_id):

    #Appends the given champ_id to the API endpoint
    url = f"{CHAMPION_DETAIL_URL}/{champ_id}.json"

    data = requests.get(url).json()

    #Extracts all data from the champ_id key
    champ = data["data"][champ_id]

    #Creates a list of all the data pairs retrieved and stored in 'champion'
    champion = {
        "id": champ["id"],
        "name": champ["name"],
        "title": champ["title"],
        "lore": champ["lore"],
        "tags": champ["tags"],
        "icon": f"{ICON_URL}/{champ['id']}.png",
        "splash": f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ_id}_0.jpg",
        "passive": champ["passive"],
        "spells": champ["spells"]
    }

    #Sends the data to the champion-page
    return render_template(
        "champion-page.html",
        champion=champion
    )


if __name__ == "__main__":
    app.run(debug=True)
