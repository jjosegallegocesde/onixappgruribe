import pandas as pd
import matplotlib.pyplot as plt

from helpers.crearCSV import crearCSV
from helpers.crearTablaHTML import crearTabla

from data.ventas import ventas

#1. Crear un CSV con los datos de las ventas
crearCSV(ventas,'ventas.csv')

#2. Cargo la fuente datos y con PANDAS creo un DATAFRAME
ventasDataFrame=pd.read_csv('data/ventas.csv', encoding='')

crearTabla(ventasDataFrame,'tablaventas')

#print(ventasDataFrame)

#3. Explorar los datos
'''examen1=ventasDataFrame.head()
examen2=ventasDataFrame.tail()
examen3=ventasDataFrame.head(20)
examen4=ventasDataFrame.info()
examen5=ventasDataFrame.describe()
examen6=ventasDataFrame.tail(50)'''


#4. Filtrar y ordenar(limpiar)
filtroUno=ventasDataFrame.query("(Costo>=290000) and (Costo<=300000)")
totalventas=filtroUno[['Costo','Cliente']]

#generando html con resultados del filtro
crearTabla(filtroUno,'ventasBajoCosto')



#6. Presentar y exportar los datos
ventasAltas=ventasDataFrame.nlargest(5,"Costo")
ventasBajas=ventasDataFrame.nsmallest(5,"Costo")
print(ventasBajas)

#Graficando un DATAFRAME CON MATPLOTLIB
ventasAltas["NumeroOrden"]=ventasAltas["NumeroOrden"].astype(str)
colores=['blue','green','#EFEC1B','orange','purple']
plt.figure(figsize=(10,10))
plt.bar(ventasAltas["NumeroOrden"],ventasAltas["Costo"], color=colores)

#Personalizando la gráfica

plt.xlabel("Cliente")
plt.ylabel("Costo")
plt.title("Ventas mas altas en ultimo mes")
plt.xticks(rotation=45)

rutaGrafica="figuras/barrasventa.png"
plt.savefig(rutaGrafica)
