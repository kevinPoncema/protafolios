from fastapi import FastAPI
import mysql.connector
#uvicorn dbb:app --reload
app = FastAPI()
conexion = None  

def connect():
    global conexion
  
    conexion = mysql.connector.connect(user="root", password="1234", host="localhost", database="DBB_empliados", port="3306")

    


@app.get("/getAll",description="obtiene todos los empleados")
async def getAll():
    connect()
    cursor = conexion.cursor()
    query = "select * from empleados"
    cursor.execute(query)
    registros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return registros


@app.delete("/deleteUSer",description="borra un usuario  a partir de su id")
def delete_user(id: str):
     connect()
     query = "DELETE FROM empleados WHERE id = %s"
     cursor = conexion.cursor()
    # Asegúrate de pasar el parámetro como una tupla
     parametro = (id, )  # Aquí se añade la coma para crear una tupla de un solo elemento
     cursor.execute(query, parametro)  # Utiliza 'parametro' en lugar de 'id'
     conexion.commit()  # ¡No olvides hacer commit para aplicar los cambios!
     cursor.close()
     conexion.close()

@app.post("/createEmpleado",description="crea un nuevo empleado")
async def insert(id:str,nom:str,ape:str,sal:str,tel:str):
    connect()
    cursor = conexion.cursor()
    query = "INSERT INTO empleados (id, nom, ape, salario, telefono) VALUES (%s, %s, %s, %s, %s)"
    parametros = (id,nom,ape,sal,tel,)
    cursor.execute(query,parametros)
    conexion.commit()
    cursor.close()
    conexion.close()

@app.patch("/updateName",description="actualiza el nombre de un empelado")
async def upadateName(name,id):
    connect()
    query = "update empleados set nom =%s where id =%s"
    params = (name,id,)
    cursor = conexion.cursor()
    cursor.execute(query,params)
    conexion.commit()
    cursor.close()
    conexion.close()

@app.patch("/updateApellido",description="actualiza el apellido de un empelado")
async def upadateName(apellido,id):
    connect()
    query = "update empleados set ape =%s where id =%s"
    params = (apellido,id,)
    cursor = conexion.cursor()
    cursor.execute(query,params)
    conexion.commit()
    cursor.close()
    conexion.close()

@app.patch("/updateSalario",description="actualiza el salario de un empelado")
async def upadateSalario(salario,id):
    connect()
    query = "update empleados set salario =%s where id =%s"
    params = (salario,id,)
    cursor = conexion.cursor()
    cursor.execute(query,params)
    conexion.commit()
    cursor.close()
    conexion.close()

@app.patch("/updateTelefono",description="actualiza el telefono de un empelado")
async def upadateSalario(Telefono,id):
    connect()
    query = "update empleados set telefono =%s where id =%s"
    params = (Telefono,id,)
    cursor = conexion.cursor()
    cursor.execute(query,params)
    conexion.commit()
    cursor.close()
    conexion.close()

def listar(res):
    dic = dict({})
    for i in range(0, len(res)):
         object = {
         "id":res[i][0],
         "nombre":res[i][1],
         "apellido":res[i][2],
         "salario":res[i][3],
         "telefono":res[i][4]
        }
         dic[f"elemento {i}"]=object 
    print(dic)
    return dic

@app.get("/getxName",description="obtiene los empleados filtrando por nombre")
async def getName(name):
     connect()
     query = "select *from empleados where nom =  %s"
     cursor = conexion.cursor()
     parametro = (name, )  # Aquí se añade la coma para crear una tupla de un solo elemento
     cursor.execute(query, parametro)  
     res = cursor.fetchall()
     cursor.close()
     conexion.close()
    
     return  listar(res)

@app.get("/getxId",description="obtiene los empleados filtrando por id")
async def getId(id):
     connect()
     query = "select *from empleados where id =  %s"
     cursor = conexion.cursor()
     parametro = (id, )  # Aquí se añade la coma para crear una tupla de un solo elemento
     cursor.execute(query, parametro)  
     res = cursor.fetchall()
     cursor.close()
     conexion.close()
     return listar(res)


@app.get("/getxApellido",description="obtiene los empleados filtrando por Apellido")
async def getName(name):
     connect()
     query = "select *from empleados where ape =  %s"
     cursor = conexion.cursor()
     parametro = (name, )  # Aquí se añade la coma para crear una tupla de un solo elemento
     cursor.execute(query, parametro)  
     res = cursor.fetchall()
     cursor.close()
     conexion.close()
     return listar(res)


@app.get("/getxSalario",description="obtiene los empleados filtrando por salario")
async def getName(salario):
     connect()
     query = "select *from empleados where salario =  %s"
     cursor = conexion.cursor()
     parametro = (salario, )  # Aquí se añade la coma para crear una tupla de un solo elemento
     cursor.execute(query, parametro)  
     res = cursor.fetchall()
     cursor.close()
     conexion.close()
     return listar(res)

@app.get("/rangos",description="obtiene los empleados cuyo sueldo se encuntra entre cierto rango")
async def rango(rangoInicial: str, rangoFinal: str):
    connect()
    query = "SELECT * FROM empleados WHERE salario BETWEEN %s AND %s"
    cursor = conexion.cursor()
    parametros = (rangoInicial, rangoFinal)
    cursor.execute(query, parametros)
    res = cursor.fetchall()
    cursor.close()
    conexion.close()
    return listar(res)
