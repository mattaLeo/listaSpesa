from flask import Flask, render_template, request, redirect
from models import DatabaseWrapper

app = Flask(__name__)

listaSpesa = []

db = DatabaseWrapper(
    host = "mysql-1e5e0afb-pallascats.i.aivencloud.com",
    user = "avnadmin",
    port = 12223,
    password = "AVNS_yQYeMS3IIA_ODp_IoLN",
    database = "esercitazioneFlask"
)

@app.route('/')
def home():
    listaSpesa = db.get_elemento()
    return render_template("index.html", lista=listaSpesa)

@app.route("/aggiungi", methods=["POST"])
def aggiungi():
    element = request.form["element"]
    listaSpesa.append(element)
    db.aggiungi_elemento(element)
    return redirect("/")

@app.route("/rimuovi/<int:index>", methods=["POST"])
def rimuovi(index):
    db.rimuovi_elemento(index)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)