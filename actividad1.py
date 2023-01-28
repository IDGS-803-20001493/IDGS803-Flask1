from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/operasBas",methods=["GET" ,"POST"])
def operasBas():
    if request.method == "POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opcion = request.form.get("opcion")

        if opcion == '1':
            return "la suma es {}".format(str(int(num1) + (int(num2))))
        elif opcion == '2':
            return "la resta es {}".format(str(int(num1) - int(num2)))
        elif opcion == '3':
            return "la multiplicacion es {}".format(str(int(num1) * int(num2)))
        elif opcion == '4':
            return "la division es {}".format(str(int(num1) / int(num2)))

    else:
       return '''
        <form action="/operasBas" method = "POST">
        <label> N1 : </label>
        <input type="text"  name="num1" /></br></br>

        <label> N2 : </label>
        <input type="text"  name="num2" /></br></br>

        <input type="radio" value="1" name="opcion"/> sumar
        <input type="radio" value="2" name="opcion"/>restar
        <input type="radio" value="3" name="opcion"/>multiplicar
        <input type="radio" value="4" name="opcion"/>dividir

        <input type="submit" value="calcular" />
        </form> 
       ''' 


    

if __name__ == "__main__":
    app.run(debug = True)

