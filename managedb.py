import sqlite3

con = sqlite3.connect("data.db")
print("Opened database successfully")

# con.execute("CREATE TABLE IF NOT EXISTS title(id INTEGER PRIMARY KEY AUTOINCREMENT, title_name TEXT, type TEXT, genre TEXT)")
# con.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, password TEXT)")
# con.execute("CREATE TABLE IF NOT EXISTS title_by_user(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title_id INTEGER, watched BOOLEAN, title_order INTEGER, FOREIGN KEY(user_id) REFERENCES user(id), FOREIGN KEY(title_id) REFERENCES title(id))")

# con.execute("INSERT INTO user(name, password) VALUES (?,?)", ("davi", "123"))
# con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("The Godfather", "Filme", "Drama"))
# con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("Inception", "Filme", "Ação"))
# con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("Dexter", "Serie", "Crime"))
# con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("Breaking Bad", "Serie", "Crime"))
# con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("Nome super grande para testar o limite de caracteres que o sistema suporta", "Serie", "Crime"))
con.execute("INSERT INTO title(title_name, type, genre) VALUES (?,?,?)", ("Mama Mia", "Filme", "Musical"))

con.commit()

