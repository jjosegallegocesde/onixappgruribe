import pandas as pd

from helpers.crearCSV import crearCSV
from data.ventas import ventas

#1. Crear un CSV con los datos de las ventas
crearCSV(ventas,'ventas.csv')