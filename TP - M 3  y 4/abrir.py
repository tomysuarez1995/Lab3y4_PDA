import csv

# def listauc():
#     with open('Plan2021.csv', 'r', encoding="utf-8") as csvPlan2021:
#         plan2021= list(csv.reader(csvPlan2021))
#         listaUCs2021 = []
#         for x in plan2021:
#             lista = x
#             listaUCs2021.append(lista[1])#imprime solamente el nombre de la materia
#     return listaUCs2021
alum= input("ingrese nombre de alumno: ")
escribir= open("personas.csv", "w")
nuevoalumn= csv.writer(alum)

print(nuevoalumn)