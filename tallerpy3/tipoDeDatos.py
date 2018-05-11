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
    Módulo para la presentación de tipo de datos.
"""

def entero():
    return ('''    >>> entero = 1
    >>> type(entero)
    <class 'int'> ''')

def flotante():
    return ('''    >>> flotante = 1.0
    >>> type(flotante)
    <class 'float'>''')

def string():
    return ('''    >>> string = "Taller Python"
    >>> type(string)
    <class 'str'> ''')

def boolean():
    return ('''    >>> boolean = True
    >>> type(boolean)
    <class 'bool'> ''')
