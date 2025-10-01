import psycopg2

# ===========================
# Conexión a PostgreSQL
# ===========================
try:
    conexion = psycopg2.connect(
        host="localhost",
        database="prueba",
        user="postgres",
        password="latorrededruaka",
        port="5432"
    )
    cursor = conexion.cursor()
    print("Conectado a PostgreSQL")
except Exception as e:
    print("Error al conectar a PostgreSQL:", e)

# ===========================
# FUNCIONES PARA CLIENTE
# ===========================
def agregar_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    correo = input("Correo: ")
    telefono = input("Teléfono (opcional): ") or None
    direccion = input("Dirección (opcional): ") or None
    try:
        cursor.execute("""
            INSERT INTO cliente (nombre, apellido, correo, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellido, correo, telefono, direccion))
        conexion.commit()
        print("Cliente agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

def buscar_cliente():
    correo = input("Correo del cliente: ")
    cursor.execute("SELECT * FROM cliente WHERE correo=%s", (correo,))
    cliente = cursor.fetchone()
    print(cliente if cliente else "Cliente no encontrado")

def actualizar_cliente():
    id_cliente = input("ID del cliente a actualizar: ")
    nombre = input("Nuevo nombre (dejar en blanco si no cambia): ") or None
    apellido = input("Nuevo apellido: ") or None
    correo = input("Nuevo correo: ") or None
    telefono = input("Nuevo teléfono: ") or None
    direccion = input("Nueva dirección: ") or None

    campos = []
    valores = []
    if nombre: campos.append("nombre=%s"); valores.append(nombre)
    if apellido: campos.append("apellido=%s"); valores.append(apellido)
    if correo: campos.append("correo=%s"); valores.append(correo)
    if telefono: campos.append("telefono=%s"); valores.append(telefono)
    if direccion: campos.append("direccion=%s"); valores.append(direccion)
    valores.append(id_cliente)

    if campos:
        sql = f"UPDATE cliente SET {', '.join(campos)} WHERE id_cliente=%s"
        try:
            cursor.execute(sql, tuple(valores))
            conexion.commit()
            print("Cliente actualizado")
        except Exception as e:
            conexion.rollback()
            print("Error:", e)
    else:
        print("⚠ No se actualizaron campos")

def eliminar_cliente():
    id_cliente = input("ID del cliente a eliminar: ")
    try:
        cursor.execute("DELETE FROM cliente WHERE id_cliente=%s", (id_cliente,))
        conexion.commit()
        print("Cliente eliminado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA EMPLEADO
# ===========================
def agregar_empleado():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ") or None
    correo = input("Correo: ") or None
    telefono = input("Teléfono: ") or None
    try:
        cursor.execute("""
            INSERT INTO empleado (nombre, apellido, cargo, correo, telefono)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellido, cargo, correo, telefono))
        conexion.commit()
        print("Empleado agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

def buscar_empleado():
    correo = input("Correo del empleado: ")
    cursor.execute("SELECT * FROM empleado WHERE correo=%s", (correo,))
    empleado = cursor.fetchone()
    print(empleado if empleado else "Empleado no encontrado")

def actualizar_empleado():
    id_empleado = input("ID del empleado a actualizar: ")
    nombre = input("Nuevo nombre: ") or None
    apellido = input("Nuevo apellido: ") or None
    cargo = input("Nuevo cargo: ") or None
    correo = input("Nuevo correo: ") or None
    telefono = input("Nuevo teléfono: ") or None

    campos = []
    valores = []
    if nombre: campos.append("nombre=%s"); valores.append(nombre)
    if apellido: campos.append("apellido=%s"); valores.append(apellido)
    if cargo: campos.append("cargo=%s"); valores.append(cargo)
    if correo: campos.append("correo=%s"); valores.append(correo)
    if telefono: campos.append("telefono=%s"); valores.append(telefono)
    valores.append(id_empleado)

    if campos:
        sql = f"UPDATE empleado SET {', '.join(campos)} WHERE id_empleado=%s"
        try:
            cursor.execute(sql, tuple(valores))
            conexion.commit()
            print("Empleado actualizado")
        except Exception as e:
            conexion.rollback()
            print("Error:", e)
    else:
        print("⚠ No se actualizaron campos")

def eliminar_empleado():
    id_empleado = input("ID del empleado a eliminar: ")
    try:
        cursor.execute("DELETE FROM empleado WHERE id_empleado=%s", (id_empleado,))
        conexion.commit()
        print("Empleado eliminado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA DISTRIBUIDOR
# ===========================
def agregar_distribuidor():
    nombre_empresa = input("Nombre de la empresa: ")
    contacto = input("Contacto: ") or None
    telefono = input("Teléfono: ") or None
    direccion = input("Dirección: ") or None
    try:
        cursor.execute("""
            INSERT INTO distribuidor (nombre_empresa, contacto, telefono, direccion)
            VALUES (%s, %s, %s, %s)
        """, (nombre_empresa, contacto, telefono, direccion))
        conexion.commit()
        print("Distribuidor agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

def buscar_distribuidor():
    nombre_empresa = input("Nombre de la empresa: ")
    cursor.execute("SELECT * FROM distribuidor WHERE nombre_empresa=%s", (nombre_empresa,))
    distribuidor = cursor.fetchone()
    print(distribuidor if distribuidor else "Distribuidor no encontrado")

def actualizar_distribuidor():
    id_distribuidor = input("ID del distribuidor a actualizar: ")
    nombre_empresa = input("Nuevo nombre: ") or None
    contacto = input("Nuevo contacto: ") or None
    telefono = input("Nuevo teléfono: ") or None
    direccion = input("Nueva dirección: ") or None

    campos = []
    valores = []
    if nombre_empresa: campos.append("nombre_empresa=%s"); valores.append(nombre_empresa)
    if contacto: campos.append("contacto=%s"); valores.append(contacto)
    if telefono: campos.append("telefono=%s"); valores.append(telefono)
    if direccion: campos.append("direccion=%s"); valores.append(direccion)
    valores.append(id_distribuidor)

    if campos:
        sql = f"UPDATE distribuidor SET {', '.join(campos)} WHERE id_distribuidor=%s"
        try:
            cursor.execute(sql, tuple(valores))
            conexion.commit()
            print("Distribuidor actualizado")
        except Exception as e:
            conexion.rollback()
            print("Error:", e)
    else:
        print("⚠ No se actualizaron campos")

def eliminar_distribuidor():
    id_distribuidor = input("ID del distribuidor a eliminar: ")
    try:
        cursor.execute("DELETE FROM distribuidor WHERE id_distribuidor=%s", (id_distribuidor,))
        conexion.commit()
        print("Distribuidor eliminado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA PRODUCTO
# ===========================
def agregar_producto():
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    id_distribuidor = int(input("ID del distribuidor: "))
    try:
        cursor.execute("""
            INSERT INTO producto (nombre, descripcion, precio, stock, id_distribuidor)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, descripcion, precio, stock, id_distribuidor))
        conexion.commit()
        print("Producto agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

def buscar_producto():
    nombre = input("Nombre del producto: ")
    cursor.execute("SELECT * FROM producto WHERE nombre=%s", (nombre,))
    producto = cursor.fetchone()
    print(producto if producto else "Producto no encontrado")

def actualizar_producto():
    id_producto = input("ID del producto a actualizar: ")
    nombre = input("Nuevo nombre: ") or None
    descripcion = input("Nueva descripción: ") or None
    precio_input = input("Nuevo precio: ") or None
    stock_input = input("Nuevo stock: ") or None
    id_distribuidor_input = input("Nuevo ID distribuidor: ") or None

    campos = []
    valores = []
    if nombre: campos.append("nombre=%s"); valores.append(nombre)
    if descripcion: campos.append("descripcion=%s"); valores.append(descripcion)
    if precio_input: campos.append("precio=%s"); valores.append(float(precio_input))
    if stock_input: campos.append("stock=%s"); valores.append(int(stock_input))
    if id_distribuidor_input: campos.append("id_distribuidor=%s"); valores.append(int(id_distribuidor_input))
    valores.append(id_producto)

    if campos:
        sql = f"UPDATE producto SET {', '.join(campos)} WHERE id_producto=%s"
        try:
            cursor.execute(sql, tuple(valores))
            conexion.commit()
            print("Producto actualizado")
        except Exception as e:
            conexion.rollback()
            print("Error:", e)
    else:
        print("⚠ No se actualizaron campos")

def eliminar_producto():
    id_producto = input("ID del producto a eliminar: ")
    try:
        cursor.execute("DELETE FROM producto WHERE id_producto=%s", (id_producto,))
        conexion.commit()
        print("Producto eliminado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA PEDIDO
# ===========================
def agregar_pedido():
    id_cliente = int(input("ID del cliente: "))
    id_empleado = int(input("ID del empleado: "))
    estado = input("Estado del pedido (Pendiente por defecto): ") or "Pendiente"
    try:
        cursor.execute("""
            INSERT INTO pedido (id_cliente, id_empleado, estado)
            VALUES (%s, %s, %s) RETURNING id_pedido
        """, (id_cliente, id_empleado, estado))
        id_pedido = cursor.fetchone()[0]
        conexion.commit()
        print("Pedido agregado con ID:", id_pedido)
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

def eliminar_pedido():
    id_pedido = int(input("ID del pedido a eliminar: "))
    try:
        cursor.execute("DELETE FROM pedido WHERE id_pedido=%s", (id_pedido,))
        conexion.commit()
        print("Pedido eliminado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA DETALLE PEDIDO
# ===========================
def agregar_detalle_pedido():
    id_pedido = int(input("ID del pedido: "))
    id_producto = int(input("ID del producto: "))
    cantidad = int(input("Cantidad: "))
    try:
        cursor.execute("""
            INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad)
            VALUES (%s, %s, %s)
        """, (id_pedido, id_producto, cantidad))
        conexion.commit()
        print("Detalle agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# FUNCIONES PARA RECIBO
# ===========================
def agregar_recibo():
    id_pedido = int(input("ID del pedido: "))
    metodo_pago = input("Método de pago: ")
    try:
        cursor.execute("""
            INSERT INTO recibo (id_pedido, metodo_pago)
            VALUES (%s, %s)
        """, (id_pedido, metodo_pago))
        conexion.commit()
        print("Recibo agregado")
    except Exception as e:
        conexion.rollback()
        print("Error:", e)

# ===========================
# MENÚS INTERACTIVOS
# ===========================
def menu_tabla(tabla):
    while True:
        print(f"\n=== {tabla.upper()} ===")
        print("1. Agregar")
        print("2. Buscar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Volver al menú principal")
        opcion = input("Seleccione opción: ")

        if tabla == "cliente":
            if opcion == "1": agregar_cliente()
            elif opcion == "2": buscar_cliente()
            elif opcion == "3": actualizar_cliente()
            elif opcion == "4": eliminar_cliente()
            elif opcion == "5": break
        elif tabla == "empleado":
            if opcion == "1": agregar_empleado()
            elif opcion == "2": buscar_empleado()
            elif opcion == "3": actualizar_empleado()
            elif opcion == "4": eliminar_empleado()
            elif opcion == "5": break
        elif tabla == "distribuidor":
            if opcion == "1": agregar_distribuidor()
            elif opcion == "2": buscar_distribuidor()
            elif opcion == "3": actualizar_distribuidor()
            elif opcion == "4": eliminar_distribuidor()
            elif opcion == "5": break
        elif tabla == "producto":
            if opcion == "1": agregar_producto()
            elif opcion == "2": buscar_producto()
            elif opcion == "3": actualizar_producto()
            elif opcion == "4": eliminar_producto()
            elif opcion == "5": break
        elif tabla == "pedido":
            if opcion == "1": agregar_pedido()
            elif opcion == "4": eliminar_pedido()
            elif opcion == "5": break
        elif tabla == "detalle":
            if opcion == "1": agregar_detalle_pedido()
            elif opcion == "5": break
        elif tabla == "recibo":
            if opcion == "1": agregar_recibo()
            elif opcion == "5": break
        else:
            print("Opción inválida")

def menu_principal():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Clientes")
        print("2. Empleados")
        print("3. Distribuidores")
        print("4. Productos")
        print("5. Pedidos")
        print("6. Detalle Pedidos")
        print("7. Recibos")
        print("0. Salir")
        opcion = input("Seleccione tabla: ")

        if opcion == "1": menu_tabla("cliente")
        elif opcion == "2": menu_tabla("empleado")
        elif opcion == "3": menu_tabla("distribuidor")
        elif opcion == "4": menu_tabla("producto")
        elif opcion == "5": menu_tabla("pedido")
        elif opcion == "6": menu_tabla("detalle")
        elif opcion == "7": menu_tabla("recibo")
        elif opcion == "0": break
        else: print("⚠ Opción inválida")

# ===========================
# INICIO DEL PROGRAMA
# ===========================
menu_principal()

cursor.close()
conexion.close()
print("Conexión cerrada")
