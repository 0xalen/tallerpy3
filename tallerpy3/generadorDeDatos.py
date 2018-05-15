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
    Módulo para la generación de datos para pruebas.
"""

import random
import string

interpretados = ['Python', 'R', 'Julia', 'OTcl', 'Lua', 'AWK', 'Lisp']
compilados = ['C', 'C++', 'Pascal', 'Java', 'Ruby', 'Perl']
infoSecEvents = ['Operation Aurora', 'Stuxnet', 'Heartbleed', 'Sony Hack', \
                 'Ashley Madison', 'Mirai', 'Cloudbleed', 'Dirty COW', 'WannaCry', 'Petya',\
                 'EternalBlue', 'Equifax', 'Spectre', 'Meltdown']

def obtenerNumero(linf, lsup):
      return random.randint(linf, lsup)

def obtenerCadena(numeroDecaracteres):
    s = ''.join([random.choice(string.ascii_letters + string.punctuation + string.digits) for n in range(numeroDecaracteres)])
    return s

def obtenerListas():
    return [interpretados, compilados, infoSecEvents]

def obtenerTuplas():
    return [tuple(interpretados), tuple(compilados), tuple(infoSecEvents)]


