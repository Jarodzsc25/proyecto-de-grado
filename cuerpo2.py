import psycopg2

try:
    # Conexión
    conexion = psycopg2.connect(
        host="localhost",
        database="prueba",
        user="postgres",
        password="latorrededruaka",
        port="5432"
    )
    cursor = conexion.cursor()
    print("✅ Conectado a PostgreSQL")

    # ============================
    # PEDIR DATOS AL USUARIO
    # ============================
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")
    direccion = input("Ingrese la dirección: ")

    # ============================
    # INSERTAR DATOS DESDE CONSOLA
    # ============================
    cursor.execute("""
        INSERT INTO cliente (nombre, apellido, correo, telefono, direccion)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_cliente;
    """, (nombre, apellido, correo, telefono, direccion))

    nuevo_id = cursor.fetchone()[0]
    print(f"🆕 Cliente insertado con ID: {nuevo_id}")

    # Guardar cambios
    conexion.commit()

    # ============================
    # CONSULTAR DATOS
    # ============================
    cursor.execute("SELECT id_cliente, nombre, apellido, correo FROM cliente;")
    clientes = cursor.fetchall()

    print("\n Lista de clientes:")
    for c in clientes:
        print(f"ID: {c[0]} | {c[1]} {c[2]} | {c[3]}")

    # ============================
    # EJEMPLO JOIN: PEDIDOS CON CLIENTES
    # ============================
    cursor.execute("""
        SELECT p.id_pedido, c.nombre, c.apellido, p.fecha_pedido, p.estado
        FROM pedido p
        JOIN cliente c ON p.id_cliente = c.id_cliente;
    """)
    pedidos = cursor.fetchall()

    print("\n Pedidos registrados:")
    for p in pedidos:
        print(f"Pedido #{p[0]} - Cliente: {p[1]} {p[2]} - Fecha: {p[3]} - Estado: {p[4]}")

    # Cerrar conexión
    cursor.close()
    conexion.close()

except Exception as e:
    print("Error:", e)
