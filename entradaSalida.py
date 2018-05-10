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

def entradaSinCast():
	print('''   >>> edad= input("Ingrese su edad: ")
	Ingrese su edad: 18 ''', end='')
	print('''   >>> edad + 1 ''', end='')
	print('''   Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: must be str, not int''', end='')

def entradaConCast():
	print('''   >>> edad= int(input("Ingrese su edad: "))''')
	print('''   Ingrese su edad: 18''')
	print('''   >>> type(edad)''')
	print('''   <class 'int'>''')
	print('''   >>> edad + 1''')
	print('   19')