"""Adaptar el codigo a .csv"""
import csv
import pandas as pd
class Ingreso():
    """En esta clase se asigna el rol y se agregan a la base de datos a los estudiantes, docentes, coordinadores
    y administrativa"""
    def __init__(self, nombre:str, CI:int, tipoRol:str, AñoIngreso:int):
        """constructor"""
        if tipoRol == "A" or tipoRol == "E" or tipoRol == "C" or tipoRol == "a" or tipoRol == "e" or tipoRol == "c":
            self.nomb=nombre
            self.ci= CI
            self.tipo= tipoRol
            self.ingreso = AñoIngreso
            if self.tipo=="E" or self.tipo=="e":  
                print("Estudiante Ingresado")
            elif self.tipo=="A"or self.tipo=="a":
                print("Administrador/a Ingresado")
            else:
                print("Coordinador/a Ingresado")
        else:
            raise ValueError("el rol debe de ser E(Estudiante), A(Administrativa), C(Coordinador)")
        
    def asignar_mail(self):
        """Simplemente esta funcion le agrega la extencion al mail segun si es estudiante o no"""
        if self.tipo=="E" or self.tipo=="e":
            correo = self.nomb.replace(" ", ".")
            return f"{correo.lower()}@estudiantes.utec.edu.uy"
        else:
            correo = self.nomb.replace(" ", ".")
            return f"{correo.lower()}@utec.edu.uy"

    def mostrar_datos(self):
        """en esta funcion se muestran los datos del agregado"""
        return f"{self.nomb} con cedula {self.ci} tiene los datos: \nrol: {self.tipo} \ncorreo: {self.asignar_mail()}"

    def guardar_datos(self):
        """Esta funcion guarda los datos de los ingresados en el archivo designado, simplemente guarda todos los
        ingresados en un archivo, puede ser en archivos distintos pero no cambia tanto el codigo ni aqui ni a 
        futuro"""
        with open('rol.csv', 'a', newline='') as nuevo:
            if self.tipo == "A" or self.tipo=="a":
                dato= [self.nomb,self.ci,"Administrativa/o",self.ingreso,self.asignar_mail()]
                df= csv.writer(nuevo)
                df.writerow(dato)
                nuevo.close()
                return "Administrativa/o guardado"

            if self.tipo=="C" or self.tipo=="c":
                dato= [self.nomb,self.ci,"Coordinador/a",self.ingreso,self.asignar_mail()]
                df= csv.writer(nuevo)
                df.writerow(dato)
                nuevo.close()
                return "Coordinador/a Guardado"

            else:
                dato= [self.nomb,self.ci,"Estudiante",self.ingreso,self.asignar_mail()]
                df= csv.writer(nuevo)
                df.writerow(dato)
                nuevo.close()
                return "Estudiante Guardado"

    def mostrar_archivo(self):
        """muestra mediante tabla los ingresados"""
        return pd.read_csv("rol.csv")
