from Persona import Persona

def mostrarPersonas(personas):
    for p in personas:
        print("%s tiene %d años" % (p.getNombre(), p.getEdad()) )
    

if __name__ == '__main__':
    p = [] 
    p.append(Persona("Ana", 27))
    p.append(Persona("María", 42))
    p.append(Persona("Macarena", 23))

    mostrarPersonas(p)
