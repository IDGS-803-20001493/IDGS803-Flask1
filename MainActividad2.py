from flask import Flask, render_template
from flask import request

from clasesActividad2 import clasesActividad2

app = Flask(__name__)

@app.route("/menu")
def menu():
    return render_template("indexActividad2.html")


@app.route("/resultado", methods = ["POST"])
def resultado():
    obj=clasesActividad2()

    obj.nombre = request.form.get("txtnombre")
    obj.tarjeta = int(request.form.get("btnTarjeta"))
    obj.cantidadCompradores = int(request.form.get("txtCantidadCompradores"))
    obj.cantidadBoletas = int(request.form.get("txtCantidadBoletas"))

    return render_template("resultadoActividad2.html", total = obj.comprobarCompradores(), nombre = obj.nombre)

if __name__ == "__main__":
    app.run(debug = True)

