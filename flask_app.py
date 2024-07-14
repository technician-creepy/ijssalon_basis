from flask import Flask, render_template
# Altijd de Eerste regel
app=Flask(__name__)
# Hoofd route
@app.route('/')
def home():
    return render_template("home.html")

# Route voor prijzen
@app.route('/prijzen')
def prijzen():
    items = [
        {"product": "vanille-ijs 1 liter", "prijs": "2 euro"},
        {"product": "chocolade-ijs 1 liter", "prijs" : "2 euro"}
    ]
    return render_template("prijzen.html", items=items)

# route voor recepten
@app.route('/recepten')
def recepten():
    items = [
        {"recept": "Tiramisu di nona",
         "img": "tiramisu.png"},
         {"recept": "Ijstaart met chocolade",
          "img" : "ijstaart.png"}
    ]
    return render_template("recepten.html", items=items)

# Altijd de laatste 2 regels
# Na testen debug=True vervangen met debug=False
if __name__ == '__main__':
    app.run(port=5000,debug=True)
'''
Opstarten van flask:
- windows:      $ set FLASK_APP=flask_app.py
- PowerShell:   $ $env:FLASK_APP = flask_app.py   
- *nix :        $ export FLASK_APP=flask_app.py

- $ flask run
'''