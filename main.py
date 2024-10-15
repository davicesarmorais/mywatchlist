from flask import Flask, render_template, request,redirect, url_for
import sqlite3

app = Flask(__name__)

def data_by_user(user_id: int) -> list:
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()
        cur.execute(
            f"""SELECT title_name, type, genre, watched
            FROM title_by_user
            JOIN title ON title_by_user.title_id = title.id
            WHERE user_id = {user_id}"""
        )
        data = cur.fetchall()
    
    dados = [
        {"titulo": item[0],
        "tipo": item[1],
        "genero": [x for x in item[2].split(",")],
        "status": "Assistido" if item[3] == 1 else "Não assistido"} 
        for item in data
    ]

    return dados
    

@app.route('/')
def home():
    dados = data_by_user(1)
    
    status = request.args.get('status', "Todos")
    if status == 'Todos':
        dados_filtrados = dados
    else:
        dados_filtrados = [item for item in dados if item['status'] == status]
    
    return render_template("home.html", data=dados_filtrados, status=status)


@app.route('/add', methods=['POST'])
def add():
    title = request.form['novo_titulo']
    with sqlite3.connect('data.db') as con:
        cur = con.cursor()  
        cur.execute(
            f"""INSERT INTO title_by_user (user_id, title_id, title_order, watched)
            VALUES (1, (SELECT id FROM title WHERE title_name = '{title}'), 7, 1)"""
        )
        con.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)