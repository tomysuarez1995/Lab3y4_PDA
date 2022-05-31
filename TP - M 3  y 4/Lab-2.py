class Persona():
    '''Clase persona. A ella pertenecen estudiantes, docentes, no docentes'''

    def _init_(self, nombreApellido, cedula):
        self.nombreApellido = nombreApellido
        self._cedula = cedula

    def __str__(self):
        return (f"({self.nombreApellido}; {self._cedula})")

import csv

with open('Plan2021.csv', 'r', encoding="utf-8") as csvPlan2021:

    plan2021 = csv.reader(csvPlan2021)

    listaPlan2021 = list(plan2021)
    
#print (listaPlan2021)

listaUCs2021 = []
for x in listaPlan2021:
    lista = x
    listaUCs2021.append(lista[1])

class Secretaria(Persona):
    '''Clase Secretaria. Hereda atributos de la clase Persona y ademas tiene otros atributos y metodos de acuerdo a la responsabilidad del cargo.'''

    def __init__(self, nombreApellido, cedula):
        self.nombreApellido = nombreApellido
        self._cedula = cedula    
        pass

    def matricularUC():
        pass
    def desmatricularUC():
        pass
    def UCsaprobadas():
        pass
    def UCscursando():
        pass
    def matricularexamen():
        pass
    def desmatricularexamen():
        pass

class Coordinadora(Persona):
    '''Clase Coordinadora. Hereda atributos de la clase Persona. Tiene metodos determinados acordes a la responsabilidad del cargo'''
    def __init__(self, nombreApellido, cedula):
        self.nombreApellido = nombreApellido
        self._cedula = cedula
        pass
    def UCsaprobadas():
        pass
    def UCscursando():
        pass

class Docente():
    '''Clase Docente. Hereda atributos de la clase Persona y ademas tiene otros atributos y metodos de acuerdo a la responsabilidad del car.'''

    def __init__(self, nombreApellido, cedula, UC):
        self.nombreApellido = nombreApellido
        self._cedula = cedula
        self.UC = UC
        
    def estudiantesInscriptos():
        pass

class Estudiante():

    '''Clase Estudiante. Hereda atributos de la clase Persona y ademas tiene otros atributos y metodos.'''
    def __init__(self, nombreApellido, cedula, añoIngreso, planEstudio, UCsAprobadas = [], UCsCursando = []):
        self.nombreApellido = nombreApellido
        self._cedula = cedula
        self.añoIngreso = añoIngreso
        self.planEstudio = planEstudio
        self.UCsAprobadas = UCsAprobadas 
        self.UCsCursando = UCsCursando

    def __str__(self):
        return (f"punto({self.añoIngreso}; {self.planEstudio}; {self.UCsAprobadas})")
        
    def consultaMatriculables(self):
        for x in listaPlan2021:
            lista = x
            if lista[2] in self.UCsAprobadas and lista[3]  in self.UCsAprobadas and lista[4]  in self.UCsAprobadas and lista[5]  in self.UCsAprobadas and lista[5] in self.UCsAprobadas:
                UCsmatriculables.append(lista[1])
                UCsmatriculables = [j for j in UCsmatriculables if j not in self.UCsAprobadas]
            #print (f"Te puedes matricular a las siguientes UCS:", UCsmatriculables)
        return UCsmatriculables
  
    def autoMatricula(self, consultaMatriculables,listaMatricular):
        hola = consultaMatriculables()

hola = [ingles1, ingles2]
estudiante1.automatricula()


        
        pass

    def UCsaprobadas():
        pass
    def UCscursando():
        pass
    def automatriculaexamen():
        pass



