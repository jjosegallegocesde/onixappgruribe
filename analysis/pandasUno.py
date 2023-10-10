import pandas as pd

#Uso basico de PANDAS
#1. Fuente de datos (lista)
ciudades=['Jerusalen','telabit','kiev','itagui','pitalito']
#2. Procesar y convertir una lista en DataFrame
dataframeCiudades=pd.DataFrame({'Ciudad':ciudades})
print(dataframeCiudades)

#######
#1. Fuente de datos Una lista de diccionarios(coleccion)
estudiantes=[
    {'id':1,'nombre':'Juan Discotecas','promedio':0.0},
    {'id':2,'nombre':"Santi el Bicho",'promedio':0.5},
    {'id':3,'nombre':"santi diomedez",'promedio':2.0},
    {'id':4,'nombre':"Susana no vilvi",'promedio':1.8},
    {'id':5,'nombre':"Juancho Styles", 'promedio':0.0}
]
#2. Convertir los datos de entrada en un dataFrame
dataFrameEstudiantes=pd.DataFrame(estudiantes)
print(dataFrameEstudiantes)