from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/Ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro
        descuento = 0

        # Descuento según la edad
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento

        return render_template('Ejercicio_1.html',
                               nombre=nombre,
                               total_sin_descuento=total_sin_descuento,
                               descuento=descuento,
                               total_con_descuento=total_con_descuento)

    return render_template('Ejercicio_1.html')


@app.route('/Ejercicio_2', methods=['GET', 'POST'])
def ejercicio_2():
    usuarios = {
        'juan': 'admin',
        'pepe': 'user'
    }

    mensaje = ""
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == 'juan':
                mensaje = f"Bienvenido Administrador {usuario}"
            elif usuario == 'pepe':
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('Ejercicio_2.html', mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
