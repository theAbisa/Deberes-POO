pacientes = []

def registrar():
    codigo = input("Codigo: ")
    nombre = input("Nombre del Paciente: ")
    edad = input("Edad: ")
    diagnostico = input("Diagnostico: ")
    pacientes.append([codigo, nombre, edad, diagnostico])
    print("Registro Exitoso!")

def mostrar():
    if len(pacientes) == 0:
        print("No hay pacientes registrados")
        return
    print("=== LISTA DE PACIENTES ===")
    for fila in pacientes:
        print()
        print("Codigo: ", fila[0])
        print("Nombre del Paciente: ", fila[1])
        print("Edad: ", fila[2])
        print("Diagnostico: ", fila[3])
        print("==========================")

def buscar(criterio, tipo_busqueda):
    encontrados = []
    
    for fila in pacientes:
      
        codigo_paciente = fila[0]
        nombre_paciente = fila[1]
        diagnostico_paciente = fila[3]
        
        
        if tipo_busqueda == "codigo":
            if codigo_paciente == criterio:
                encontrados.append(fila)
                
        elif tipo_busqueda == "nombre":
            # Si el criterio está dentro del nombre, lo guardamos
            if criterio.lower() in nombre_paciente.lower():
                encontrados.append(fila)
                
        elif tipo_busqueda == "diagnostico":
           
            if criterio.lower() in diagnostico_paciente.lower():
                encontrados.append(fila)
                
    return encontrados

           
def editar():
    print("--- Editar Paciente ---")
    codigo = input("Ingrese el código del paciente a editar: ")
    pacienteEncontrado = buscar(codigo, "codigo")

    if pacienteEncontrado:
        paciente = pacienteEncontrado[0]  
        print("Paciente encontrado: ", paciente)
        paciente[1] = input("Registra el nuevo nombre del apciente:")
        paciente[2] = input("Registra la nueva edad del paciente:")
        paciente[3] = input("Registra el nuevo diagnóstico del paciente:")
        print("Datos actualizados exitosamente")
      
def eliminar():
    print("--- Eliminar Paciente ---")
    codigo = input("Ingrese el código del paciente a eliminar: ")
    pacienteEliminar = buscar(codigo, "codigo")
    if len (pacienteEliminar) == 0:
        print("No se encontró el paciente con el código proporcionado.")
    else:
        objetoPaciente = pacienteEliminar[0]  # Obtener el primer paciente encontrado
        pacientes.remove(objetoPaciente)
        print("Paciente eliminado exitosamente")
        
    
while True:
    print("\n === MENU DE PACIENTES ===")
    print("[1] Registrar paciente")
    print("[2] Mostrar paciente")
    print("[3] Editar paciente")
    print("[4] Eliminar paciente")
    print("[5] Busqueda por codigo de paciente")
    print("[6] Busqueda por nombre de paciente")
    print("[7] Busqueda por diagnostico de paciente")
    print("[N] Salir")

    opcion = input("Seleccione una opcion: ")

    match opcion:
        case "1":
            registrar()
        case "2":
            mostrar()
        case "3":
            editar()
        case "4":
            eliminar()
        case "5":
            criterio = input("Ingrese el codigo del paciente a buscar: ")
            resultados = buscar(criterio, "codigo")
            # Muestra los resultados en pantalla
            if resultados:
                print(f"Encontrado: {resultados[0]}")
            else:
                print("No se encontró ningún paciente con ese código.")
        case "6":
            criterio = input("Ingrese el nombre del paciente a buscar: ")
            resultados = buscar(criterio, "nombre")
            if resultados:
                print("=== PACIENTES ENCONTRADOS ===")
                for p in resultados:
                    print(f"Código: {p[0]} | Nombre: {p[1]} | Diagnóstico: {p[3]}")
            else:
                print("No se encontraron pacientes con ese nombre.")
        case "7":
            criterio = input("Ingrese el diagnostico del paciente a buscar: ")
            resultados = buscar(criterio, "diagnostico")
            if resultados:
                print("=== PACIENTES ENCONTRADOS ===")
                for p in resultados:
                    print(f"Código: {p[0]} | Nombre: {p[1]} | Diagnóstico: {p[3]}")
            else:
                print("No se encontraron pacientes con ese diagnóstico.")
        case "N":
            print("Salio del sistema")
            break