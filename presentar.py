#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright 2018 Alejandro Trinidad <franco.unpa@protonmail.com>
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

import tipoDeDatos as datos
import operaciones as op
import entradaSalida as io


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
    print("Operaciones en Python:")
    delimitar(1)
    num1 = op.obtenerNumero()
    num2 = op.obtenerNumero()
    print("Números: ",num1," y ",num2)
    delimitar(1)

    op.suma(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.resta(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.producto(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.division(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.divisionPiso(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.modulo(num1,num2)
    esperarRetorno()
    delimitar(1)

    op.divisionTeorema(num1,num2)
    esperarRetorno()
    delimitar(1)

def mostrarDatos():
    delimitar(0)
    print("Tipos de datos en Python:")
    delimitar(1)

    datos.entero()
    esperarRetorno()
    delimitar(1)

    datos.flotante()
    esperarRetorno()
    delimitar(1)

    datos.string()
    esperarRetorno()
    delimitar(1)

    datos.boolean()
    esperarRetorno()
    delimitar(1)

def mostrarEntrada():
    delimitar(0)
    print("Entrada en el intérprete de Python:")
    delimitar(1)

    io.entradaSinCast()
    esperarRetorno()
    delimitar(1)

    io.entradaConCast()
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
