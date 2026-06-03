from flask import Flask, jsonify
# O Flask possui a extensão CORS para permitir que arquivos HTML externos acessem a API.
# Como estamos desmembrando, precisamos permitir esse acesso.
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) # Isso permite que o seu HTML independente converse com o Python

@app.route("/api/dados")
def obter_dados():
    # Em vez de carregar um HTML, o Python agora só envia dados puros
    informacoes = {
        "mensagem": "Olá, Mundo! Este dado veio direto do Python (Back-end)!",
        "status": "Sucesso",
        "ano": 2026
    }
    return jsonify(informacoes)

if __name__ == "__main__":
    app.run(debug=True)