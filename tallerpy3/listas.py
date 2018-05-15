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
    Módulo para la presentación de operaciones básicas con listas en Python.
"""

import string

def crearLista():
    return('''    Crear lista vacía:
    lista = list()
    ó
    lista = []

    Crear lista con elementos:
    infoSecEvents = [ 'Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', \
'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya',\
'EternalBlue', 'Equifax']
    ''')

def insercion():
    return('''    Con append:
    >>> infoSecEvents.append('Spectre')
    >>> infoSecEvents
    ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre']

    Con insert:
    >>> infoSecEvents.insert(13,'Meltdwn')
    >>> infoSecEvents
    ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdwn']
    ''')
def eliminacion():
    return('''    Con del:
    >>> del infoSecEvents[13]
    >>> infoSecEvents
    ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre']

    Con remove:
    >>> infoSecEvents.remove('Operation Aurora')
    >>> infoSecEvents
    ['Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
    ''')

def ordenamiento():
    return('''    Con sort:
    >>> cosas = [1, 'abc', 'Python', "2"]
    >>> cosas.sort()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: '<' not supported between instances of 'str' and 'int'
    >>> cosas.sort(key=str)
    >>> cosas
    [1, '2', 'Python', 'abc']
    ''')

def concatenacion(l1, l2):
    return ('''    Concatenación (+):
    '''+str(l1)+''' + '''+str(l2)+'''

    -->  '''+str(l1+l2))

def repeticion(l1, num1):
    return ('''    Repetición (*):
    '''+str(l1)+''' * '''+str(num1)+'''
    -->  '''+str(l1*num1))

def slicingIndice():
    return ('''    Índices:
        >>> infoSecEvents
        [ 'Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
        >>> infoSecEvents[0]
        'Operation Aurora'
        >>> infoSecEvents[5]
        'Mirai'
        >>> infoSecEvents[-6]
        'WannaCry'
        >>> infoSecEvents[-1]
        'Meltdown'
        >>> infoSecEvents[14]
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        IndexError: list index out of range
        >>>
    ''')

def slicingRango():
    return ('''Rangos:
        >>> infoSecEvents[0:3]
        ['Operation Aurora', 'Stuxnet', 'Heartbleed']
        >>>> infoSecEvents[3:9]
        ['Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry']
        >>> infoSecEvents[:7]
        ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed']
        >>> infoSecEvents[:-7]
        ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed']
        >>> infoSecEvents[6:]
        ['Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
        >>> infoSecEvents[-8:]
        ['Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
        >>> infoSecEvents[-65431468764323254768456567:]
        ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
        >>> infoSecEvents[:65431468764323254768456567]
        ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya', 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']
    ''')
