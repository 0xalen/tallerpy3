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

"""
    Módulo para la presentación de operaciones de entrada y salida básicas.
"""

def entradaSinCast():
	return('''    >>> edad = input("Ingrese su edad: ")
    Ingrese su edad: 18
    >>> edad + 1
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: must be str, not int ''')

def entradaConCast():
	return('''    >>> edad= int(input("Ingrese su edad: "))
    Ingrese su edad: 18
    >>> type(edad)
    <class 'int'>
    >>> edad + 1
    19''')

def salidaSinFormato():
    return('''    >>> numDeAmigos=1000000
    >>> accion="cantar"
    >>> print("Yo quiero tener",numDeAmigos,"de amigos")
    >>> print("y así más fuerte poder",accion)
    Yo quiero tener 1000000 de amigos
    y así más fuerte poder cantar
     ''')

def salidaConFormato():
    return('''    >>> numDeAmigos=1000000
    >>> accion="cantar"
    >>> print("Yo quiero tener %d de amigos \\
    ... \\ny así más fuerte poder %s" % (numDeAmigos, accion))
    Yo quiero tener 1000000 de amigos
    y así más fuerte poder cantar
     ''')
