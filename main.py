from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open ('tests/teste.json', 'r', encoding='utf-8') as f:
    data = json.load(f)["data"]

@app.route('/')
def home():
    return render_template("home.html", data=data)

@app.route('/filtrar', methods=['GET'])
def filtrar():
    status = request.args.get('status')
    if status == 'Todos':
        itens_filtrados = data
    else:
        itens_filtrados = [item for item in data if item['status'] == status]
        
    return jsonify(itens_filtrados)

if __name__ == '__main__':
    app.run(debug=True)