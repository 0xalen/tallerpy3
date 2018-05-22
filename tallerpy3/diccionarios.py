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
    Módulo para la presentación de operaciones básicas con diccionarios en Python.
"""

import string

def crearDiccionario():
    return('''    Crear diccionario vacía:
    dic1 = {}
    ó
    dic2 = dict()

    Crear diccionario con elementos:
    >>> dic3 = {'Laura' : 25 , 'Emilia' : 27}
    >>> dic4 = dict(Juan = 32, Martin = 22)
    ''')
def mostrarDiccionario():
    return('''
    Mostrar elementos
    >>> dic1
    {}
    >>> dic2
    {}
    >>> dic3
    {'Laura': 25, 'Emilia': 27}

    >>> dic4
    {'Juan': 32, 'Martin': 22}
    ''')

def agregarElementos():
    return('''    Agregar elementos:
    dic3['Julieta'] = 19
    dic4['Lucas'] = 24
    ''')

def obtenerElementos():
    return('''    Obtener elementos:
    >>> dic3['Emilia']
    27

    >>> dic4.get('Juan')
    32

    >>> dic3[Emilia]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'Emilia' is not defined

    >>> dic3['Emili']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Emili'
    ''')

def modificarElementos():
    return('''    Modificar elementos:
    >>> dic3
    {'Laura': 25, 'Emilia': 27, 'Julieta': 19}

    dic3['Julieta'] = 20

    >>> dic3
    {'Laura': 25, 'Emilia': 27, 'Julieta': 20}
    ''')

def eliminarElementos():
    return('''     Eliminar elementos:
    >>> dic4
    {'Juan': 32, 'Martin': 22, 'Lucas': 24}

    del dic4['Lucas']

    >>> dic4
    {'Juan': 32, 'Martin': 22}
    ''')

def recorrerDiccionario():
    return('''    Recorrer diccionarios:
    Por items:
        >>> for nombre, edad in dic3.items():
        ...     print(nombre,":",edad)
        ...
        Laura : 25
        Emilia : 27
        Julieta : 19

    Por claves:
        >>> for nombre in dic4.keys():
        ...     print(nombre)
        ...
        Juan
        Martin
        Lucas

    Por valores:
        >>> for edad in dic3.values():
        ...     print(edad)
        ...
        25
        27
        19

    Ordenada por clave:
    >>> for nombre, edad in sorted(dic3.items()):
    ...     print(nombre,":",edad)
    ...
    Emilia : 27
    Julieta : 19
    Laura : 25

    ''')

def mostrarFuncionesDic():
    return('''    Mostrar funciones:
    len(): mostrar cantidad de elementos en el diccionario
        >>> len(dic4)
        3

    sorted(): ordenar elementos del diccionario según items, claves o valores
        >>> sorted(dic3)
        ['Emilia', 'Julieta', 'Laura']
        >>> sorted(dic3.items())
        [('Emilia', 27), ('Julieta', 19), ('Laura', 25)]
        >>> sorted(dic3.values())
        [19, 25, 27]
        >>> sorted(dic3.keys())
        ['Emilia', 'Julieta', 'Laura']
    ''')
