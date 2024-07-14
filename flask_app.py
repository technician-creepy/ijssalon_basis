from flask import Flask
# Altijd de Eerste regel
app=Flask(__name__)
# Hoofd route
@app.route('/')
def home():
    return "Welkom op mijn eerste Flask-website"

# Route voor prijzen
@app.route('/prijzen')
def prijzen():
    return "Binnenkort verschijnen hier onze actuele prijzen"

# route voor recepten
@app.route('/recepten')
def recepten():
    return "Binnenkort verschijnen hier enkele recepten"

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