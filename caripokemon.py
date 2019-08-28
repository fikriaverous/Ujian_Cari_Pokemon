from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepokemon.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    body = request.form
    pokemon = str(body['find'])
    pokemon = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

    data_api = requests.get(url)

    if data_api.status_code == 200:
        data = data_api.json()
    
        nama = data['name']
        nama = nama.capitalize()
        pokeid = data['id']
        tinggi = data['height']
        berat = data['weight']
        gambar = data['sprites']['front_default']

        return render_template('hasilpokemon.html', data1=nama, data2=pokeid, data3=gambar, data4=tinggi, data5=berat)
    elif data_api.status_code == 404:
        return render_template('pokemonerror.html')

if __name__ == '__main__':
    app.run(debug=True)