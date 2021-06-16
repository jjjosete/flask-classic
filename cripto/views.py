from cripto import app
from flask import jsonify, render_template
import sqlite3

@app.route("/")
def index():
    conexion = sqlite3.connect("cripto.db")
    cur = conexion.cursor()

    cur.execute("SELECT * FROM cripto;")

    claves=(cur.description)
    filas = cur.fetchall()
    movimientos = []
    #Aquí habría que calcular el valor unitario
    for fila in filas: 
        d = {}
        for tclave, valor in zip(claves, fila):
            d[tclave[0]] = valor
        movimientos.append(d)
    
    print(movimientos)
    conexion.close()

    return render_template("movimientos.html", datos=movimientos)

@app.route('/purchase')
    return 'Aquí irá un formulario'

@app.route('/status')
    return "Aquí irá el balance"