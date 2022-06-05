import pandas as pd
import csv
def plan_estudio():
    df = pd.read_csv("Plan2021.csv")
    return df.fillna("No tiene")

class Coordinador():
    def __init__(self, nombreuc=None,nombreEx=None):
        self.nombreuc= nombreuc
        self.nombreEx= nombreEx

    def leer_uc(self):
        return pd.read_csv(f"matriculadas/disponibles/{self.nombreuc}.csv ") 
        
    def leer_Ex(self):
        return pd.read_csv(f"examenes/disponibles/{self.nombreEx}.csv ")
        

class Estudiante():
    def __init__(self, cedula,matricEX=None, matricUC=None):
        self.matricUC= matricUC
        self.matricEx= matricEX
        self.ci= cedula
       
    def matricularEx(self):
        with open(f"examenes/disponibles/{nuevoss}.csv",'a', newline='') as File:
            leer1= csv.writer(File)
            with open(f'rol.csv', 'r', newline='') as nuevo:
                leer= csv.DictReader(nuevo)
                for i in leer:
                    for key, value in i.items():
                        if value == "54311063":
                            estudiante= [i["Nombres"],i["CI"]]
            leer1.writerow(estudiante)
            nuevo.close()
        File.close()
        return estudiante

        
    def matricularUC(self):
        pass

class Administrador():
    def __init__(self, cedula,nombrEst=None,matricUC=None, matricEX=None, DesmUC=None, DesmEX=None, nombreuc=None,nombreEx=None ):
        self.matricUC= matricUC
        self.matricEx= matricEX
        self.uc= nombreuc
        self.ex= nombreEx
        self.est= nombrEst
    
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


matricular=Estudiante(54311063,"S6UC2")
print(matricular.matricularEx())