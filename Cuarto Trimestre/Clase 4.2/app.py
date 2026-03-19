import flask 
from flask import Flask, request, jsonify, render_template
import psycopg2  
from psycopg2.extras import RealDictCursor  
import os  
from datetime import datetime  

# Configuración de la aplicación
app = Flask(__name__)

DB_CONFIG = {
    'host': 'localhost',
    'database': 'tienda_tech',
    'user': 'postgres',
    'password': '123456',
    'port': '5432'
}

def conectar_db():  
    try:
        os.environ.setdefault('PGCLIENTENCODING', 'utf8')

        conexion = psycopg2.connect(options='-c client_encoding=UTF8', **DB_CONFIG)
        return conexion
    except UnicodeDecodeError as e:
        raise RuntimeError(
            "UnicodeDecodeError durante la conexión a PostgreSQL. "
            "Verifique que las credenciales y variables de entorno estén en UTF-8 "
            "y pruebe a exportar PGCLIENTENCODING=utf8 antes de ejecutar la app."
        ) from e
    except psycopg2.Error as e:
        print("Error al conectar:", e) 
        return None 


def crear_tabla_productos():
    conexion = conectar_db() 
    if conexion:
        cursor = conexion.cursor() 
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS public.productos(
                        id integer NOT NULL DEFAULT nextval('productos_id_seq'::regclass),
                        nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
                        precio numeric(10,2) NOT NULL,
                        CONSTRAINT productos_pkey PRIMARY KEY (id)
                        )
        """)  
        conexion.commit()  
        cursor.close()  
        conexion.close()  

def crear_tabla_carrito():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS public.carrito(
                       id integer NOT NULL DEFAULT nextval('carrito_id_seq'::regclass),
                        fecha_creacion timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
                        CONSTRAINT carrito_pkey PRIMARY KEY (id)
                    )
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()

def crear_tabla_detalle_carrito():
    conexion=conectar_db()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS public.detalle_carrito(
                        id integer NOT NULL DEFAULT nextval('detalle_carrito_id_seq'::regclass),
                        carrito_id integer,
                        producto_id integer,
                        cantidad integer DEFAULT 1,
                        CONSTRAINT detalle_carrito_pkey PRIMARY KEY (id),
                        CONSTRAINT detalle_carrito_carrito_id_fkey FOREIGN KEY (carrito_id)
                            REFERENCES public.carrito (id) MATCH SIMPLE
                            ON UPDATE NO ACTION
                            ON DELETE NO ACTION,
                        CONSTRAINT detalle_carrito_producto_id_fkey FOREIGN KEY (producto_id)
                            REFERENCES public.productos (id) MATCH SIMPLE
                            ON UPDATE NO ACTION
                            ON DELETE NO ACTION)
""")

@app.route('/')
def inicio():
    return render_template('home.html') 

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')



# @app.route('/guardar_compras', methods=['POST'])
# def guardar_usuario():
#     try:
#         conexion = conectar_db()  #conectar a la base de datos
#         if conexion is None:
#             return jsonify({'mensaje': 'Error de conexión a la base de datos'}), 500

#         #obtiene los datos enviados en Json
#         datos = request.get_json()  #obtener datos en formato JSON
#         producto = datos.get('producto')  #obtener producto

#         #validar datos obligatorios
#         if not producto:
#             return jsonify({'mensaje': 'El nombre y el correo son obligatorios'}), 400

#         #crear cursor para ejecutar consultas
#         cursor = conexion.cursor()

#         sql_insert = """
#             INSERT INTO Usuario (producto_id)
#             VALUES (%s)
#             RETURNING id;
#         """  #consulta SQL para insertar usuario

#         cursor.execute(sql_insert, (producto))
#         carrito_id = cursor.fetchone()[0]  #obtener id generado

#         conexion.commit()  #guardar cambios
#         cursor.close()  #cerrar cursor
#         conexion.close()  #cerrar conexión

#         return jsonify({'mensaje': 'Usuario guardado exitosamente', 'usuario_id': usuario_id})

#     except Exception as e:
#         return jsonify({'mensaje': 'Error al guardar el usuario', 'error': str(e)}), 500

if __name__ == "__main__":
    crear_tabla_productos()  #crear tabla si no existe
    crear_tabla_carrito()
    crear_tabla_detalle_carrito()
    app.run(debug=True)