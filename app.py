# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
  if(request.method == "GET"):
    return render_template("index.html")
  else:
    if(request.form["numero1"] != "" and request.form["numero2"] != ""):
      numero1 = request.form["numero1"]
      numero2 = request.form["numero2"]
      
      if(request.form["opc"] == "soma"):
        soma = int(numero1) +  int(numero2)
        return {
          "Resultado":str(soma)
        }
      elif(request.form["opc"] == "subtracao"):
        subtracao = int(numero1) - int(numero2)
        return {
          "Resultado":str(subtracao)
        }
      elif(request.form["opc"] == "multiplicacao"):
        multiplicacao = int(numero1) * int(numero2)
        return {
          "Resultado":str(multiplicacao)
        }
      elif(request.form["opc"] == "divisao"):
        divisao = int(numero1) // int(numero2)
        return {
          "Resultado":str(divisao)
        }
      elif(request.form["opc"] == "juros"):
        desconto = int(numero1) // 100 * int(numero2)
        juros = int(numero1) - desconto
        return {
          "Resultado":str(juros)
        }
    else:
      return "Preencha os dois campos!!"



@app.errorhandler(404)
def not_found(error):
  return render_template("error.html")


app.run(port=8080, debug=True)
