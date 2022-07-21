#!/usr/bin/env python
# coding: utf-8
# importaciones de librerias
from administrador import menu_admi, limpiarPantalla
from vendedor import validarAcceso
import getpass
import time

def inicio():
    while True:
        print("╔════════════════════════════════╗")
        print("║ GRIFO GRUPO INCAPACARITA S.A.C ║")
        print("╠════════════════════════════════╣")
        print("║[1] Vendedor                    ║")
        print("║[2] Administrador               ║")
        print("║[3] salir                       ║")
        print("╚════════════════════════════════╝")

        op = input("Eliga una opcion: ")
        match (op):
            case "1": 
                dni = input("Ingrese DNI: ")
                password = getpass.getpass("Ingrese password: ")
                validarAcceso(dni,password)
                limpiarPantalla()
            case "2":
                acumulador = 0
                while True and acumulador != 3:
                    usser = input("ingrese usuario: ") 
                    passwd = getpass.getpass("Ingrese password: ")

                    if usser == "incapacarita" and passwd == "102030":
                        limpiarPantalla()
                        menu_admi()
                    else:
                        print("Contraseña incorrecta")
                        acumulador += 1
                        time.sleep(2)
                        
            case "3": 
                break
            case _ : print("ERROR!! no existe esa opcion")
            
if __name__ == "__main__":
    # la funcion que queremos que se ejecute
    inicio()
