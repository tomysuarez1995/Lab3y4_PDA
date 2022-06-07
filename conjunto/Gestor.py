import pandas as pd
import csv

def plan_estudio():
    """Muestra todo el plan de estudio"""
    df = pd.read_csv("Plan2021.csv")
    return df.fillna("No tiene")

class Coordinador():
    """Clase coordinador donde solamente lee las uc y examenes"""
    def __init__(self, nombreuc=None,nombreEx=None):
        self.nombreuc= nombreuc
        self.nombreEx= nombreEx

    def leer_uc(self):
        return pd.read_csv(f"matricladas/disponibles/{self.nombreuc}.csv ") 
        
    def leer_Ex(self):
        return pd.read_csv(f"examenes/disponibles/{self.nombreEx}.csv ")
        

class Estudiante():
    """Clase estudiante donde se puede matricular a los examenes y Uc determinado sus materias"""
    def __init__(self,cedula,matricEX=None, matricUC=None):
        self.matricUC= matricUC
        self.matricEx= matricEX
        self.ci= cedula
       
    def matricularEx(self):
        """Esta funcion matricula a examen al estudiante"""
        with open(f"examenes/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open(f'rol.csv', 'r', newline='') as nuevo:
                leer= csv.DictReader(nuevo)
                for i in leer:
                    for key, value in i.items():
                        if value == str(self.ci):
                            estudiante= [i["Nombres"],i["CI"]]
                            leer1.writerow(estudiante)
            nuevo.close()
        File.close()
        return "estudiante matriculado"

    def matricularUC(self):
        """Esta funcion matricula a UC al estudiante"""
        with open(f"matricladas/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open(f'rol.csv', 'r', newline='') as nuevo:
                leer= csv.DictReader(nuevo)
                for i in leer:
                    for key, value in i.items():
                        if value == str(self.ci):
                            estudiante= [i["Nombres"],i["CI"]]
                            leer1.writerow(estudiante)
            nuevo.close()
        File.close()
        return "estudiante matriculado"

class Administrador():
    """El admin puede matricular, desmatricular y leer las Uc y Examenes"""
    def __init__(self,ciest=None,matricUC=None, matricEX=None, nombreuc=None,nombreEx=None ):
        self.matricUC= matricUC
        self.matricEx= matricEX
        self.uc= nombreuc
        self.ex= nombreEx
        self.est= ciest
    
    def desmatricularEx(self):
        """Esta funcion lo que hace es abrir un archivo de copia para guardar los estudiantes que siguen
        matriculados a examenes o uc y luego deja en blanco el arhivo de la uc o examen y sobrescribe con
        el de copia de seguridad para luego blanquear el de copia de seguridad"""
        with open("examenes/disponibles/copiaseguridad.csv", "a") as y:
            data2=csv.writer(y)
            with open(f"examenes/disponibles/{self.matricEx}.csv", "r") as f:
                data = list(csv.reader(f))
                for i in data:
                    list1= i[0]
                    list2= i[1]
                    diccest= dict({list1: list2})
                    for key, value in diccest.items():
                        if value!="54311063":
                            lista=[key, value]
                            data2.writerow(lista)
            f.close()
        y.close()
        with open(f"examenes/disponibles/{self.matricEx}.csv", "w") as t:
                data3=csv.writer(t)
                t.close()
        with open(f"examenes/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open('examenes/disponibles/copiaseguridad.csv', 'r', newline='') as nuevo:
                leer= list(csv.reader(nuevo))
                for i in leer:
                    leer1.writerow(i)
            nuevo.close()
        File.close()
        with open("examenes/disponibles/copiaseguridad.csv", "w") as y:
            data2=csv.writer(y)
            y.close()
        return "Estudiante desmatriculado"

    def desmatricularUC(self):
        """Esta funcion lo que hace es abrir un archivo de copia para guardar los estudiantes que siguen
        matriculados a examenes o uc y luego deja en blanco el arhivo de la uc o examen y sobrescribe con
        el de copia de seguridad para luego blanquear el de copia de seguridad"""
        with open("examenes/disponibles/copiaseguridad.csv", "a") as y:
            data2=csv.writer(y)
            with open(f"examenes/disponibles/{self.matricUC}.csv", "r") as f:
                data = list(csv.reader(f))
                for i in data:
                    list1= i[0]
                    list2= i[1]
                    diccest= dict({list1: list2})
                    for key, value in diccest.items():
                        if value!="54311063":
                            lista=[key, value]
                            data2.writerow(lista)
            f.close()
        y.close()
        with open(f"examenes/disponibles/{self.matricUC}.csv", "w") as t:
                data3=csv.writer(t)
                t.close()
        with open(f"examenes/disponibles/{self.matricUC}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open('examenes/disponibles/copiaseguridad.csv', 'r', newline='') as nuevo:
                leer= list(csv.reader(nuevo))
                for i in leer:
                    leer1.writerow(i)
            nuevo.close()
        File.close()
        with open("examenes/disponibles/copiaseguridad.csv", "w") as y:
            data2=csv.writer(y)
            y.close()
        return "Estudiante desmatriculado"

    def leer_uc(self):
        return pd.read_csv(f"matricladas/disponibles/{self.uc}.csv ") 
        
    def leer_Ex(self):
        return pd.read_csv(f"examenes/disponibles/{self.ex}.csv ")

    def matricularEx(self):
        """Esta funcion matricula a examen al estudiante"""
        with open(f"examenes/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open(f'rol.csv', 'r', newline='') as nuevo:
                leer= csv.DictReader(nuevo)
                for i in leer:
                    for key, value in i.items():
                        if value == str(self.est):
                            estudiante= [i["Nombres"],i["CI"]]
                            leer1.writerow(estudiante)
            nuevo.close()
        File.close()
        return "estudiante matriculado"

    def matricularUC(self):
        """Esta funcion matricula a UC al estudiante"""
        with open(f"matricladas/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open(f'rol.csv', 'r', newline='') as nuevo:
                leer= csv.DictReader(nuevo)
                for i in leer:
                    for key, value in i.items():
                        if value == str(self.est):
                            estudiante= [i["Nombres"],i["CI"]]
                            leer1.writerow(estudiante)
            nuevo.close()
        File.close()
        return "estudiante matriculado"