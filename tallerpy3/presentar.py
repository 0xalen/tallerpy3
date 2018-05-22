#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright 2018 Alejandro Trinidad <franco.unpa@protonmail.com>
#                Franco Herrera <fherrera@uarg.unpa.edu.ar>
#
# TallerPy3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# These scripts are distributed in the hope that they will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TallerPy3 . If not, see <http://www.gnu.org/licenses/>.
#

"""
    Módulo para estructurar la presentación de cada contenido temático.
"""

import generadorDeDatos as gen
import tipoDeDatos as datos
import calculadora as calc
import entradaSalida as io
import cadenasDeCaracteres as cad
import listas as li
import tuplas as tup
import condicionales as con
import bucles as bu
import diccionarios as dic
import funciones as f

def mostrarInterprete():
    delimitar(0)
    print("Intérprete de Python:")
    delimitar(1)
    print('''   ~$ python3
    Python 3.6.5 (default, Apr  4 2018, 15:01:18)
    [GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux
    Type "help", "copyright", "credits" or "license" for more information.''')
    esperarRetorno()
    delimitar(1)

def mostrarOperaciones():
    delimitar(0)
    print("Operaciones matemáticas en Python:")
    delimitar(1)
    num1 = gen.obtenerNumero(1, 50)
    num2 = gen.obtenerNumero(1, 50)
    print("Números aleatoriosle: ",num1," y ",num2)
    delimitar(1)

    print(calc.suma(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.resta(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.producto(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.division(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.divisionPiso(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.modulo(num1,num2))
    esperarRetorno()
    delimitar(1)

    print(calc.divisionTeorema(num1,num2))
    esperarRetorno()
    delimitar(1)

def mostrarDatos():
    delimitar(0)
    print("Tipos de datos en Python:")
    delimitar(1)

    print(datos.entero())
    esperarRetorno()
    delimitar(1)

    print(datos.flotante())
    esperarRetorno()
    delimitar(1)

    print(datos.string())
    esperarRetorno()
    delimitar(1)

    print(datos.boolean())
    esperarRetorno()
    delimitar(1)

def mostrarEntrada():
    delimitar(0)
    print("Entradas en el intérprete de Python:")
    delimitar(1)

    print(io.entradaSinCast())
    esperarRetorno()
    delimitar(1)

    print(io.entradaConCast())
    esperarRetorno()
    delimitar(1)

def mostrarSalida():
    delimitar(0)
    print("Salidas en el intérprete de Python:")
    delimitar(1)

    print(io.salidaConFormato())
    esperarRetorno()
    delimitar(1)

    print(io.salidaSinFormato())
    esperarRetorno()
    delimitar(1)

def mostrarCadenas():
    delimitar(0)
    print("Cadenas de caracteres (strings) en Python:")
    delimitar(1)
    str1 = gen.obtenerCadena(gen.obtenerNumero(5,10))
    str2 = gen.obtenerCadena(gen.obtenerNumero(5,10))
    num3 = gen.obtenerNumero(2,7)
    print("Cadenas aleatorias: ",str1," y ",str2,"\nNúmero auxiliar: ",num3)
    delimitar(1)

    print("Comillas simples: ")
    delimitar(1)
    print(cad.comillas("'"))
    esperarRetorno()
    delimitar(1)

    print("Comillas dobles: ")
    delimitar(1)
    print(cad.comillas('"'))
    esperarRetorno()
    delimitar(1)

    print("Comillas triples: ")
    delimitar(1)
    print(cad.comillasTriples())
    esperarRetorno()
    delimitar(1)

    print("Operaciones con cadenas de caracteres: ")
    delimitar(1)

    print(cad.concatenacion(str1, str2))
    esperarRetorno()
    delimitar(1)

    print(cad.repeticion(str1, num3))
    esperarRetorno()
    delimitar(1)

    print("Slicing: ")
    delimitar(1)

    print(cad.slicingLogica())
    esperarRetorno()
    delimitar(1)

    print(cad.slicingIndice())
    esperarRetorno()
    delimitar(1)

    print(cad.slicingRango())
    esperarRetorno()
    delimitar(1)

    print()
    esperarRetorno()
    delimitar(1)

def mostrarListas():
    delimitar(0)
    print("Listas en Python:")
    delimitar(1)

    l1 = gen.obtenerListas()[0]
    l2 = gen.obtenerListas()[1]
    l3 = gen.obtenerListas()[2]
    num4 = gen.obtenerNumero(2,7)

    print("Listas: \nl1: ",l1,"\nl2 = ",l2,"\nl3 = ",l3,"\nNúmero auxiliar: ",num4)
    delimitar(1)

    print(li.crearLista())
    esperarRetorno()
    delimitar(1)

    print(li.insercion())
    esperarRetorno()
    delimitar(1)

    print(li.eliminacion())
    esperarRetorno()
    delimitar(1)

    print(li.ordenamiento())
    esperarRetorno()
    delimitar(1)

    print("Operaciones con listas: ")
    delimitar(1)

    print(li.concatenacion(l1, l2))
    esperarRetorno()
    delimitar(1)

    print(li.repeticion(l1, num4))
    esperarRetorno()
    delimitar(1)

    print("Slicing: ")
    delimitar(1)

    print(li.slicingIndice())
    esperarRetorno()
    delimitar(1)

    print(li.slicingRango())
    esperarRetorno()
    delimitar(1)

def mostrarTuplas():
    delimitar(0)
    print("Tuplas en Python:")
    delimitar(1)

    t1 = gen.obtenerTuplas()[0]
    t2 = gen.obtenerTuplas()[1]
    t3 = gen.obtenerTuplas()[2]
    num5 = gen.obtenerNumero(2,7)

    # CREAR MÓDULO PARA GENERAR COSAS
    print("Tuplas: \nt1: ",t1,"\nt2 = ",t2,"\nt3 = ",t3,"\nNúmero auxiliar: ",num5)
    delimitar(1)

    print(tup.crearTupla())
    esperarRetorno()
    delimitar(1)

    print("Operaciones con tuplas: ")
    delimitar(1)

    print(tup.concatenacion(t1, t2))
    esperarRetorno()
    delimitar(1)

    print(tup.repeticion(t1, num5))
    esperarRetorno()
    delimitar(1)

    print("Slicing: ")
    delimitar(1)

    print(tup.slicingIndice())
    esperarRetorno()
    delimitar(1)

    print(tup.slicingRango())
    esperarRetorno()
    delimitar(1)

def mostrarCondicionales():
    delimitar(0)
    print("Condicionales en Python: ")
    delimitar(1)

    print(con.expresiones())
    esperarRetorno()
    delimitar(1)
	
    print(con.sentenciaIf())
    esperarRetorno()
    delimitar(1)
	
    print(con.sentenciaIfElifElse())
    esperarRetorno()
    delimitar(1)

def mostrarBucles():
    delimitar(0)
    print("Iteración en Python:")
    delimitar(1)

    print(bu.estructuraWhile())
    esperarRetorno()
    delimitar(1)

    print(bu.ejemploWhile())
    esperarRetorno()
    delimitar(1)

    print(bu.estructuraFor())
    esperarRetorno()
    delimitar(1)

    print(bu.ejemploFor())
    esperarRetorno()
    delimitar(1)

def mostrarDiccionarios():
    delimitar(0)
    print("Diccionarios en Python:")
    delimitar(1)

    print(dic.crearDiccionario())
    esperarRetorno()
    delimitar(1)

    print(dic.mostrarDiccionario())
    esperarRetorno()
    delimitar(1)

    print(dic.agregarElementos())
    esperarRetorno()
    delimitar(1)

    print(dic.obtenerElementos())
    esperarRetorno()
    delimitar(1)

    print(dic.modificarElementos())
    esperarRetorno()
    delimitar(1)

    print(dic.eliminarElementos())
    esperarRetorno()
    delimitar(1)

    print(dic.recorrerDiccionario())
    esperarRetorno()
    delimitar(1)

    print(dic.mostrarFuncionesDic())
    esperarRetorno()
    delimitar(1)

def mostrarFunciones():
    delimitar(0)
    print("Funciones en Python:")
    delimitar(1)

    print(f.estructuraFuncion())
    esperarRetorno()
    delimitar(1)

    print(f.definirFuncion())
    esperarRetorno()
    delimitar(1)

    print(f.invocarFuncion())
    esperarRetorno()
    delimitar(1)

    print(f.pasarArgumentosSimple())
    esperarRetorno()
    delimitar(1)

    print(f.parametrosPorDefecto())
    esperarRetorno()
    delimitar(1)

    print(f.pasarArgumentos())
    esperarRetorno()
    delimitar(1)


def mostrarExcepcioneS():
    print()
    esperarRetorno()
    delimitar(1)

    print()
    esperarRetorno()
    delimitar(1)

def delimitar(t):
    if t == 0:
        print("#====================================================#")
    elif t == 1:
        print("#----------------------------------------------------#")
    else:
        print("\\____________________________________________________/")

def esperarRetorno():
    try:
        input()
    except SyntaxError:
        pass
