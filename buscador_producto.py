import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="prueba",
        user="postgres",
        password="latorrededruaka",
        port="5432"
    )

def agregar_producto():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        print("\n Agregar nuevo producto")
        nombre = input("Nombre: ")
        descripcion = input("Descripción: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        id_distribuidor = int(input("ID del distribuidor: "))

        consulta = """
            INSERT INTO producto (nombre, descripcion, precio, stock, id_distribuidor)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_producto;
        """
        cursor.execute(consulta, (nombre, descripcion, precio, stock, id_distribuidor))
        nuevo_id = cursor.fetchone()[0]

        conexion.commit()
        print(f" Producto agregado con ID {nuevo_id}")

    except Exception as e:
        print("️ Error al agregar producto:", e)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print(" Conexión cerrada")

def buscar_producto():
    try:
        conexion = conectar()
        cursor = conexion.cursor()

        nombre_buscar = input("\n Ingrese el nombre del producto a buscar: ")

        consulta = """
            SELECT id_producto, nombre, descripcion, precio, stock
            FROM producto
            WHERE nombre ILIKE %s;
        """
        cursor.execute(consulta, ('%' + nombre_buscar + '%',))
        resultados = cursor.fetchall()

        if resultados:
            print("\n Resultados encontrados:")
            for producto in resultados:
                print(f"""
                ID: {producto[0]}
                Nombre: {producto[1]}
                Descripción: {producto[2]}
                Precio: {producto[3]} Bs
                Stock: {producto[4]}
                """)
        else:
            print(" No se encontraron productos con ese nombre.")

    except Exception as e:
        print(" Error en la búsqueda:", e)
    finally:
        if conexion:
            cursor.close()
            conexion.close()
            print(" Conexión cerrada")

# ================================
# MENÚ PRINCIPAL
# ================================
while True:
    print("\n Menú:")
    print("1. Buscar producto")
    print("2. Agregar producto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        buscar_producto()
    elif opcion == "2":
        agregar_producto()
    elif opcion == "3":
        print(" Saliendo del programa...")
        break
    else:
        print(" Opción no válida, intente nuevamente.")
