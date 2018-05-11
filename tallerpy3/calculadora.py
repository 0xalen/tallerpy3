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
    Módulo para la presentación de operaciones básicas que permiten usar Python
    como una calculadora.
"""

from random import randint

def obtenerNumero(linf, lsup):
      return randint(linf, lsup)

def suma(num1, num2):
    return ('''Suma (+):
    '''+str(num1)+''' + '''+str(num2)+''' = '''+str(num1 + num2))

def resta(num1, num2):
    return ('''Resta (-):
    '''+str(num1)+''' - '''+str(num2)+''' = '''+str(num1-num2))

def producto(num1, num2):
    return ('''Producto (*):
    '''+str(num1)+''' * '''+str(num2)+''' = '''+str(num1*num2))

def division(num1, num2):
    return ('''División (/):
    '''+str(num1)+''' / '''+str(num2)+''' = '''+str(num1/num2))

def divisionPiso(num1, num2):
    return ('''División piso (//):
    '''+str(num1)+''' // '''+str(num2)+''' = '''+str(num1//num2))

def modulo(num1, num2):
    return ('''Modulo (%):
    '''+str(num1)+''' % '''+str(num2)+''' = '''+str(num1%num2))

def divisionTeorema(num1, num2):
    return ('''    DIVIDENDO = DIVISOR * COCIENTE + RESTO
    num1 = num2 * (num1 // num2) + num1 % num2
    '''+str(num1)+''' = '''+str(num2)+''' * '''+str(num1//num2)+''' +'''+str(num1%num2))

def potencia(num1, num2):
    return ('''Potencia (**):
    '''+str(num1)+''' ** '''+str(num2)+''' = '''+str(num1**num2))

def ordenDeOperaciones(num1, num2):
    return ('''PEMDAS:
    * Paréntes
    * Exponentes
    * Multiplicación
    * División
    * Adición
    * Substracción

    Ejemplo:
    '''+str(num1)+''' + '''+str(num2)+''' / '''+str(num2)+''' = '''+str(num1+num2/num2)+'''
    ('''+str(num1)+''' + '''+str(num2)+''') / '''+str(num2)+''' = '''+str((num1+num2)/num2))
