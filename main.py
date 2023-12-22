from flask import Flask, render_template, jsonify, send_from_directory
import json

app = Flask(__name__, static_url_path='/static')  # Configurando o caminho para arquivos estáticos

@app.route('/')
def home():
    return render_template('Pagina_web_reviver.html')

@app.route('/static/<path:filename>')  # Rota para servir arquivos estáticos
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
