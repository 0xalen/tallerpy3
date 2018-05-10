# entradaSalida.py
#!/usr/bin/python3

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