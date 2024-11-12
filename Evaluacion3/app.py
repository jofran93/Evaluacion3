from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        estado = "APROBADO" if promedio >= 40 and asistencia >= 75 else "REPROBADO"
        return render_template('ejercicio1.html', promedio=promedio, estado=estado)
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtenemos los nombres desde el formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encuentra el nombre con más caracteres
        max_nombre = max([nombre1, nombre2, nombre3], key=len)

        # Calcula la longitud del nombre más largo
        max_length = len(max_nombre)

        return render_template('ejercicio2.html', max_nombre=max_nombre, max_length=max_length)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)