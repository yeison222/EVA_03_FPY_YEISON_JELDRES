#Funciones 
lista = ["Ver listado de pinturas",
         "Buscar pintura"
         "Agregar pinturas",
         "Eliminar pinturas",
         "Exportar pinturas"]
import json
import csv
import os

def pantalla():
    os.system("cls")

def listar(lista):
    for ind, opt in enumerate(lista):
        print(f"{ind + 1}. {opt}")

def respuesta():
    resp = input("Que quires hacer?")
    return resp








while True:
    ans = lista
    if ans == "1":
        pass
    elif ans == "2":
        pass
    elif ans == "3":
        pass
    elif ans == "4":
        pass
    elif ans == "5":
        pass
    elif ans == "6":
        exit("Adioh!")
    else:
       break