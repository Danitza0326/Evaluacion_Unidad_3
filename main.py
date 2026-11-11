from flask import Flask, render_template, request

app = Flask(__name__)


# MENU PRINCIPAL
@app.route("/")
def index():
    return render_template("index.html")


# EJERCICIO 1: NOTAS Y ASISTENCIA
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    if request.method == "POST":

        try:
            nota1 = float(request.form.get("nota1", ""))
            nota2 = float(request.form.get("nota2", ""))
            nota3 = float(request.form.get("nota3", ""))
            asistencia = float(request.form.get("asistencia", ""))

        except ValueError:
            return render_template(
                "ejercicio1.html",
                error="Debes ingresar valores numéricos en todos los campos."
            )

        notas = [nota1, nota2, nota3]

        if not all(10 <= nota <= 70 for nota in notas):
            return render_template(
                "ejercicio1.html",
                error="Las notas deben estar entre 10 y 70."
            )

        if not 0 <= asistencia <= 100:
            return render_template(
                "ejercicio1.html",
                error="La asistencia debe estar entre 0 y 100."
            )

        promedio = round(sum(notas) / 3, 2)

        if promedio >= 40 and asistencia >= 75:
            resultado = "ESTUDIANTE APROBADO"
        else:
            resultado = "ESTUDIANTE REPROBADO"

        return render_template(
            "ejercicio1.html",
            promedio=promedio,
            asistencia=asistencia,
            resultado=resultado
        )

    return render_template("ejercicio1.html")


# EJERCICIO 2: COMPARACION DE NOMBRES
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    if request.method == "POST":

        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        nombres = [nombre1, nombre2, nombre3]

        if not all(nombres):
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar los tres nombres."
            )

        if len(set(nombre.casefold() for nombre in nombres)) != 3:
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar tres nombres diferentes."
            )

        nombre_mayor = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mayor)

        return render_template(
            "ejercicio2.html",
            nombre_mayor=nombre_mayor,
            cantidad_caracteres=cantidad_caracteres
        )

    return render_template("ejercicio2.html")


# INICIAR APLICACION
if __name__ == "__main__":
    app.run(debug=True)