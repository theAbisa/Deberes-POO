from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/producto')
def mostrarEstudiante():
    return render_template('producto.html')   
@app.route('/procesarProducto', methods=['POST'])
def promedioEstudiante():
    try:
        nombreProducto = request.form.get("nombreProducto")
        precioProducto = float(request.form.get("precioProducto"))
        cantidadProducto = int(request.form.get("cantidadProducto"))
        iva = float((precioProducto * cantidadProducto) * 0.15)
        subtotal = float(precioProducto * cantidadProducto)
        total = float(subtotal + iva)

        return f"""<h1>Resultados de la venta de producto</h1>
        <p>El nombre del prudcto es: {nombreProducto}</p>
        <p>El precio del producto es: {precioProducto}</p>
        <p>La cantidad del producto es: {cantidadProducto}</p>
        <h2>Resultados de la venta</h2>
        <p>El subtotal es: {subtotal}</p>
        <p>El IVA es: {iva}</p>
        <p>El total es: {total}</p>
        <a href="/">Volver al inicio</a>
        """
    except ValueError:
        return f"""<h1>Error</h1>
        <p>Por favor, ingrese valores numéricos válidos para la venta.</p>
        <a href="/producto">Volver al formulario</a>
        """




if __name__ == '__main__':
    app.run(debug=True)