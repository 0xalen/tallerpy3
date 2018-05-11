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
    Módulo para la presentación de operaciones básicas con cadenas de caracteres
    en Python.
"""

import random
import string

def obtenerCadena(numeroDecaracteres):
    s = ''.join([random.choice(string.ascii_letters + string.punctuation + string.digits) for n in range(numeroDecaracteres)])
    return s

def comillas(c):
    return ('''    Instrucción:
        print('''+c+'''Un anillo para gobernarlos a todos, \\
            \\nun Anillo para encontrarlos, \\
            \\nun Anillo para atraerlos a todos \\
            \\ny atarlos en las Tinieblas.'''+c+''')

    Apariencia:
        Un anillo para gobernarlos a todos,
        un Anillo para encontrarlos,
        un Anillo para atraerlos a todos
        y atarlos en las Tinieblas.
    ''')


def comillasTriples():
    return ('''    Instrucción:
        print(\'\'\'Juro solemnemente
            que mis intenciones
            no son buenas\'\'\')

    Apariencia:
        Juro solemnemente
        que mis intenciones
        no son buenas
    ''')

def concatenacion(str1, str2):
    return ('''    Concatenación (+):
    '''+str1+''' + '''+str2+'''

    -->  '''+str1+str2)

def repeticion(str1, num1):
    return ('''    Repetición (*):
    '''+str1+''' * '''+str(num1)+'''
    -->  '''+(str1*num1))

def slicingLogica():
    return ('''    Índices en slicing:
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1

    ''')

def slicingIndice():
    return ('''    Índices:
        >>> cadena = "Python"
        >>> cadena
        'Python'
        >>> cadena[0]
        'P'
        >>> cadena[5]
        'n'
        >>> cadena[0]
        'P'
        >>> cadena[-6]
        'n'
        >>> cadena[6]
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        IndexError: string index out of range
    ''')

def slicingRango():
    return ('''Rangos:
        >>> cadena[0:3]
        'Pyt'
        >>> cadena[3:6]
        'hon'
        >>> cadena[:4]
        'Pyth'
        >>> cadena[:-2]
        'Pyth'
        >>> cadena[4:]
        'on'
        >>> cadena[-2:]
        'on'
        >>> cadena[-65431468764323254768456567:]
        'Python'
        >>> cadena[:65431468764323254768456567]
        'Python'
    ''')