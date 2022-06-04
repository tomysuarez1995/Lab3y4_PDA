import pandas as pd
import csv
def plan_estudio():
    df = pd.read_csv("Plan2021.csv")
    return df.fillna("No tiene")

class Coordinador():
    def __init__(self, cedula, nombreuc=None,nombreEx=None):
        if self.existencia(self, cedula)==1:
            self.nombreuc= nombreuc
            self.nombreEx= nombreEx
            print("Bienvenido")
        elif self.existencia(self, cedula)==2:
            raise ValueError("Usted no existe en la base de datos")
        else:
            raise ValueError("Usted no es un coordinador/a")
    
    def existencia(self, cedula):
        with open('rol.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                for keys, values in row.items():
                    if values == str(cedula) in values:
                        results=list(row.values())
                        if results[2]=="Coordinador/a":
                            return 1
                        else:
                            return 0
                    else:
                        return 2
    def leer_uc(self):
        return pd.read_csv(f"matriculadas/disponibles/{self.nombreuc}.csv ") 
        
    def leer_Ex(self):
        return pd.read_csv(f"examenes/disponibles/{self.nombreEx}.csv ")
        

class Estudiante():
    def __init__(self, cedula,matricEX=None, matricUC=None):
        if self.existencia(self, cedula)==1:
            self.matricUC= matricUC
            self.matricEx= matricEX
            self.ci= cedula
            print("Bienvenido")
        elif self.existencia(self, cedula)==2:
            raise ValueError("Usted no existe en la base de datos")
        else:
            raise ValueError("Usted no es Estudiante")
    
    def existencia(self, cedula):
        with open('rol.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                for keys, values in row.items():
                    if values == str(cedula) in values:
                        results=list(row.values())
                        if results[2]=="Estudiante":
                            return 1
                        else:
                            return 0
                    else:
                        return 2
    def matricularEx(self):
        with open(f"examenes/disponibles/{self.matricEx}.csv",'a', newline='') as File:
            leer= csv.DictReader(File)
            for row in leer:
                for keys, values in row.items():
                    if values == str(self.ci) in values:
                        with open('rol.csv', 'a', newline='') as nuevo:
                        dato= [self.nomb,self.ci,"Administrativa/o",self.ingreso,self.asignar_mail()]
                        df= csv.writer(nuevo)
                        df.writerow(dato)
                        nuevo.close()
                        return "Administrativa/o guardado"


        pass
    def matricularUC(self):
        pass

class Administrador():
    def __init__(self, cedula,matricUC=None, matricEX=None, DesmUC=None, DesmEX=None, nombreuc=None,nombreEx=None ):
        if self.existencia(self, cedula)==1:
            self.matricUC= matricUC
            self.matricEx= matricEX
            self.uc= nombreuc
            self.ex= nombreEx
            print("Bienvenido")
        elif self.existencia(self, cedula)==2:
            raise ValueError("Usted no existe en la base de datos")
        else:
            raise ValueError("Usted no es Administrativa/o")
    
    def existencia(self, cedula):
        with open('rol.csv') as File:
            reader = csv.DictReader(File)
            for row in reader:
                for keys, values in row.items():
                    if values == str(cedula) in values:
                        results=list(row.values())
                        if results[2]=="Administrativa/o":
                            return 1
                        else:
                            return 0
                    else:
                        return 2
    def matricularEx(self):
        pass
    def desmatricularEx(self):
        pass
    def matricularUC(self):
        pass
    def desmatricularUC(self):
        pass

    def leer_uc(self):
        return pd.read_csv(f"matriculadas/disponibles/{self.uc}.csv ") 
        
    def leer_Ex(self):
        return pd.read_csv(f"examenes/disponibles/{self.ex}.csv ")