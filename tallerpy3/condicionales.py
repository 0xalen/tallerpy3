#!/usr/bin/python3
# -*- coding:utf-8 -*-
#
# Copyright 2018 Franco Herrera <fherrera@uarg.unpa.edu.ar>
#				 Alejandro Trinidad <franco.unpa@protonmail.com>
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
    Módulo para la presentación de operaciones de condicionales e identación.
"""

def expresiones():
    return('''    Check        Significado
    ------------------------------------
    >            Mayor que      x > 35
    <            Meno que       x < 35
    >=           Mayor o igual a x >= 35
    <=           Menor o igual a x <= 35
    ==           Igual a x == 35
    !=           Disntinto a x != 35
    and          x and y
    or           x or y
    not          not x
    is           objeto igual a
    is not       objeto no igual a''')

def sentenciaIf():
    return('''    Intrucción:
    if expresiones :
        Hacer algo
    
    Ejemplo:    
    if age >= 16:
        print("Podes Votar!, pero no ir preso!")''')

def sentenciaIfElifElse():
    return('''    if expresiones:
		hacer algo
    elif condiciones:
        hacer otra cosa
    else:
        bueno hacer esto''')
