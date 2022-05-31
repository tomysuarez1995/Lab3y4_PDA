import csv

# def listauc():
#     with open('Plan2021.csv', 'r', encoding="utf-8") as csvPlan2021:
#         plan2021= list(csv.reader(csvPlan2021))
#         listaUCs2021 = []
#         for x in plan2021:
#             lista = x
#             listaUCs2021.append(lista[1])#imprime solamente el nombre de la materia
#     return listaUCs2021
alum= ["Algebra"]
alum2= "S1M1"
escribir= open("personas.csv", "w", newline="")
with escribir:
    nuevoalumn= csv.writer(escribir)
    nuevoalumn.writerow(alum)
    nuevoalumn.writerow(alum2)

