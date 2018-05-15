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
    Módulo para la presentación de estructuras de control, en particular las
    que permiten iteración.
"""

def estructuraWhile():
    return('''    Estructura:
    while condiciones:
        repetir algo
    ''')

def ejemploWhile():
    return('''    Ejemplo 1: Contador
    	contador = 0
    	while contador =< 5:
    	    print(contador)
    	    contador += 1 		# Equivalente a "contador = contador + 1"
    Salida:
    0
    1
    2
    3
    4
    5

    # <COMPLETAR>
    # break
    # continue

    Ejemplo 2: Fibonacci
    num1, num2 = 0, 1

    while b < 100:
        print("b", end=", ")
        a, b = a, a + b

    Salida:
        1,1,2,3,5,8,13,21,34,55,89
    ''')

def estructuraFor():
    return('''    Estructura
    for i in range(comienzo, final, paso):
    	repetir algo
    ''')

def ejemploFor():
    return('''

    >>> for i in range(10):
    ...    print(i)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

    >>> for i in range(1, 11):
    ...    print(i)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

    >>> for i in range(5, 55, 5):
    ...    print(i)
    5
    10
    15
    20
    25
    30
    35
    40
    45
    50

    >>> laBamba = ['Para', 'bailar', 'la', 'Bamba']

    >>> for b in laBamba:
    ...    print(b, end=" ")
    Para bailar la Bamba

    >>> for n in range(len(laBamba):
    ...    print(laBamba[n], end=" ")
    Para bailar la Bamba

    ''')
