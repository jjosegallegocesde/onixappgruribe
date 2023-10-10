import random
empleado1={
    "id":1,
    "nombre":"Juan Jose",
    "apellidos":"Gallego Mesa",
    "salariomensual":15000000,
    "deudas":True,
    "retencionFuente":0.1,
    "correo":"jjme@grupouribe.com",
    "telefono":"3225962363",
    "cargo":"Arquitecto"
}

empleado2={
    "id":2,
    "nombre":"Johan",
    "apellidos":"Valderrama",
    "salariomensual":450000,
    "deudas":False,
    "retencionFuente":0.0,
    "correo":"jhv@grupouribe.com",
    "telefono":"3208795623",
    "cargo":"Jr"
}

# desarrollador junior 
# desarrollador intermedio 
# desarrollador avanzado  
# arquitecto

#SOLO si se ganan mas de 6 millones se aplica retencion en la fuente del 10%

empleados = []
for _ in range(50):
    nombre = random.choice(['Andres', 'Ana', 'Isabel', 'Pablo'])
    cargo = random.choice(['Gerente', 'Desarrollador', 'Diseñador', 'Analista'])
    edad = random.randint(22, 60)
    salario = random.randint(1160000, 18000000)
    empleado = [nombre, cargo, edad, salario]
    empleados.append(empleado)
print(empleados)
