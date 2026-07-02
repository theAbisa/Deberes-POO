from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/estudiante')
def mostrarEstudiante():
    return render_template('estudiante.html')   
@app.route('/procesar_estudiante', methods=['POST'])
def promedioEstudiante():
    try:
        nombre = request.form.get("nombre")
        n1 = float(request.form.get("nota1"))
        n2 = float(request.form.get("nota2"))
        n3 = float(request.form.get("nota3"))
        promedio = (n1 + n2 + n3) / 3
        return f"""<h1>Resultados de Promedio</h1>
        <p>El nombre del estudiante es: {nombre}</p>
        <p>El promedio del estudiante es: {promedio}</p>
        <p>Estado de Estudiante: {"Aprobado" if promedio >= 7 else "Reprobado"}</p> <a href="/">Volver al inicio</a>
        <a href="/">Volver al inicio</a>
        """
    except ValueError:
        return f"""<h1>Error</h1>
        <p>Por favor, ingrese valores numéricos válidos para las notas.</p>
        <a href="/estudiante">Volver al formulario</a>
        """

@app.route('/calculadora')
def mostrarCalculadora():
    return render_template('calculadora.html')

@app.route("/menu", methods=["POST"])
def calculadora():
    n1 = float(request.form.get("numero1"))
    n2 = float(request.form.get("numero2"))
    resta = n1 - n2
    suma = n1 + n2
    multiplicacion = n1 * n2
    if n2 == 0:
            division = "No se puede dividir entre cero"
    else:
            division = n1 / n2

    return f"""
    <h1>Resultados de la calculadora</h1>
    <p>La suma de {n1} y {n2} es: {suma}</p>
    <p>La resta de {n1} y {n2} es: {resta}</p>
    <p>La multiplicación de {n1} y {n2} es: {multiplicacion}</p>
    <p>La división de {n1} y {n2} es: {division}</p>
    <a href="/">Volver al inicio</a>
    """

@app.route('/vehiculos')
def mostrarVehiculos():
    return render_template('vehiculos.html')
@app.route("/ventaVehiculos", methods=["POST"])
def ventaVehiculos():
    try:
        metodo_pago = request.form.get("metodoPago")
        nombre = request.form.get("nombre")
        precio = float(request.form.get("precio"))
        cantidad = int(request.form.get("cantidad"))
        if metodo_pago == "efectivo":
            descuento = 0.20
            precio -= precio * descuento
        elif metodo_pago == "tarjeta":  
            recargo = 0.10
            precio += precio * recargo 
        elif metodo_pago == "credito":
            total = precio * cantidad
            return f"""
            <h1>Resultados de la venta de vehículos</h1>
            <p>El nombre del vehículo es: {nombre}</p>
            <p>El precio del vehículo es: {precio}</p>
            <p>La cantidad de vehículos es: {cantidad}</p>
            <p>El total de la venta es: {total}</p>
            <p>El método de pago seleccionado es: {metodo_pago}</p>
            <a href="/">Volver al inicio</a>
            """
    
    except ValueError:
        return f"""
        <h1>Error</h1>
        <p>Por favor, ingrese valores válidos para el precio y la cantidad.</p>
        <a href="/vehiculos">Volver al formulario</a>
        """


if __name__ == '__main__':
    app.run(debug=True)