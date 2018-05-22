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
    Módulo para la presentación de trabajo con funciones en Python.
"""

def estructuraFuncion():
    return('''    Definir funcion:
    def nombreFuncion(parametro1, parametro2 = 'valorPorDefecto'):
        COMIENZO
            .
            .
            .
        Cuerpo de la funcion
            .
            .
            .
        FIN
    ''')

def definirFuncion():
    return('''    Definir función:
    >>> def mostrar_convenciones():
    ...     s = \'\'\'    Convenciones para nombrar funciones:
    ...         - Usar minúsculas
    ...         - Separar palabras con _
    ...         - No comenzar con número
    ...         - No sobreescribir funciones nativas de Python
    ...         - No utilizar palabras reservadas\'\'\'
    ...     return s
    ...
    ''')

def invocarFuncion():
    return('''    Invocar funcion:
    >>> print(mostrar_convenciones())
        Convenciones para nombrar funciones:
            - Usar minúsculas
            - Separar palabras con _
            - No comenzar con número
            - No sobreescribir funciones nativas de Python
            - No utilizar palabras reservadas
    ''')

def pasarArgumentosSimple():
    return('''    Pasaje de argumentos:
    >>> def saludarUsuario(nombre):
    ...     print("Hola,",nombre)
    ...
    >>> saludarUsuario("aprendices de Python")
    Hola, aprendies de Python
    ''')

def parametrosPorDefecto():
    return('''    ¿Qué pasa si no pasamos el parámetro que nos pide la funcion?
        >>> saludarUsuario()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: saludarUsuario() missing 1 required positional argument: 'nombre'

    Para evitar este error, podemos definir un valor por defecto:
        >>> def saludarUsuario(nombre = 'humano'):
        ...     print("Hola,",nombre)
        ...

        >>> saludarUsuario()
        Hola, humano
    ''')

def pasarArgumentos():
    return('''    Funcion ejemplo:
    def registrarAlumno(nombre, edad):
        print("Nombre: "+nombre+"\\nEdad: "+str(edad))

    Por posición:
       >>> registrarAlumno('Sebastian', 50)
        Nombre: Sebastian
        Edad: 50

    Por clave:
        >>> registrarAlumno(edad = 15, nombre = 'Florencia')
        Nombre: Florencia
        Edad: 15

        >>> registrarAlumno(nombre = 'Micaela', edad = 18)
        Nombre: Micaela
        Edad: 18
    ''')


