from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open ('tests/teste.json', 'r', encoding='utf-8') as f:
    data = json.load(f)["data"]

@app.route('/')
def home():
    status = request.args.get('status', "Todos")
    if status == 'Todos':
        dados_filtrados = data
    else:
        dados_filtrados = [item for item in data if item['status'] == status]
    
    return render_template("ideia.html", data=dados_filtrados, status=status)
    return render_template("home.html", data=dados_filtrados, status=status)


if __name__ == '__main__':
    app.run(debug=True)