# api_server.py


from flask import Flask, jsonify
from flask_cors import CORS
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Model.Usuario import Usuario
from Model.Livro import Livro
from Model.Emprestimo import Emprestimo

app = Flask(__name__)
CORS(app)  

@app.route("/api/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = [
        {"matricula": "2024001", "nome": "Ana Costa", "tipo": "aluno", "email": "ana@exemplo.com"},
        {"matricula": "2024002", "nome": "Lucas Pereira", "tipo": "professor", "email": "lucas@exemplo.com"},
    ]
    return jsonify(usuarios)

@app.route("/api/livros", methods=["GET"])
def listar_livros():
    livros = [
        {"isbn": "978-85-333", "titulo": "Python Básico", "categoria": "Didático", "estoque": 5},
        {"isbn": "978-85-444", "titulo": "Flask Avançado", "categoria": "Técnico", "estoque": 2},
    ]
    return jsonify(livros)

@app.route("/api/emprestimos", methods=["GET"])
def listar_emprestimos():
    emprestimos = [
        {"usuario": "Ana Costa", "livro": "Python Básico", "data": "2025-11-13", "prazo": "2025-11-20"},
    ]
    return jsonify(emprestimos)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
