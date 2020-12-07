#!/usr/bin/python

import os
from time import sleep

class color:
    verde="\033[92m"
    rojo="\033[91m"
    amarillo="\033[93m"
    azul="\033[96m"
    blanco="\033[97m"

logo="""
        ¶¶¶¶¶¶  ¶¶¶¶¶¶  ¶       ¶¶¶¶¶¶  ¶    ¶  ¶       ¶¶¶¶¶¶  ¶¶¶¶¶¶¶
        ¶       ¶    ¶  ¶       ¶       ¶    ¶  ¶       ¶    ¶   ¶    ¶
        ¶       ¶¶¶¶¶¶  ¶       ¶       ¶    ¶  ¶       ¶¶¶¶¶¶   ¶    ¶
        ¶¶¶¶¶¶  ¶    ¶  ¶¶¶¶¶¶  ¶¶¶¶¶¶  ¶¶¶¶¶¶  ¶¶¶¶¶¶  ¶    ¶  ¶¶¶¶¶¶¶ ORA.
"""

opciones="""
    1.Sumar          |     5.Area Trapecio       |     9.Salir  
    2.Restar         |     6.Area Triangulo      |    10.Creador
    3.Multiplicar    |     7.Volumen Piramide    |    
    4.Dividir        |     8.Area Radio          |    
"""

creador="""
    Nombre  : Ridiman Mejia Vasquez
    Correo  : ridimanmejiavasquez@gmail.com 

        Fecha Creacion : 02/12/2020
"""
def Logo():
    print (color.azul + logo)
    print (color.amarillo + opciones)
def clear():
    os.system("clear")

class Operaciones_basicas:
    def __init__(self,n1,n2):
        self.suma=n1 + n2 
        self.resta=n1 - n2
        self.multiplicacion=n1 * n2
        self.divicion=n1 // n2 
class Operaciones_areas():
    def __init__(self,n1,n2,n3):
        self.area_trapecio=(n2 + n3) //2 * n1 
        self.area_triangulo=n1 * n2 // 2
        self.volumen_piramide=n1 * n2 // 3
class Operaciones_radio:
    def __init__(self,n1):
        self.area_radio=3.14 * (n1 ** 2)

iniciar=True

while(iniciar):
    clear()
    Logo()
    opc=int(input(color.blanco + "» "))
    if (opc==1):
        clear()
        a=int(input("Numero 1 : "))
        b=int(input("Numero 2 : "))
        suma=Operaciones_basicas(a,b)
        print(color.verde +f" \n{a} + {b} = {suma.suma}")
        input()
    elif (opc==2):
        clear()
        a=int(input("Numero 1 : "))
        b=int(input("Numero 2 : "))
        resta=Operaciones_basicas(a,b)
        print(color.verde + f"\n{a} - {b} = {resta.resta}")
        input()
    elif (opc==3):
        clear()
        a=int(input("Numero 1 : "))
        b=int(input("Numero 2 : "))
        multiplicacion=Operaciones_basicas(a,b)
        print(color.verde + f"\n{a} * {b} = {multiplicacion.multiplicacion}")
        input()
    elif (opc==4):
        clear()
        a=int(input("Numero 1 : "))
        b=int(input("Numero 2 : "))
        divicion=Operaciones_basicas(a,b)
        print(color.verde + f"\n{a} - {b} = {divicion.divicion}")
        input()
    elif (opc==5):
        clear()
        a=int(input("Altura : "))
        b=int(input("Base 1 : "))
        c=int(input("Base 2 : "))
        trapecio=Operaciones_areas(a,b,c)
        print(color.verde + f"\nEl area es = {trapecio.area_trapecio}")
        input()
    elif (opc==6):
        clear()
        a=int(input("Base   : "))
        b=int(input("Altura : "))
        triangulo=Operaciones_areas(a,b,0)
        print(color.verde + f"\nEl area es = {triangulo.area_triangulo}")
        input()
    elif (opc==7):
        clear()
        a=int(input("Altura : "))
        b=int(input("Base   : "))
        volumen=Operaciones_areas(a,b,0)
        print (color.verde + f"\nEl volumen de la piramide es = {volumen.volumen_piramide}")
        input()
    elif (opc==8):
        clear()
        a=int(input("Radio : "))
        area=Operaciones_radio(a)
        print(color.verde + f"\nEl area de {a} es = {area.area_radio}")
        input()
    elif (opc==9):
        print (color.azul + "SAliendo")
        sleep(1)
        exit()
    elif (opc==10):
        clear()
        print (color.azul + creador)
        input()
