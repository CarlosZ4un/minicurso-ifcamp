import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Ola, IFCAMP! Este site esta rodando dentro de um container."

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))