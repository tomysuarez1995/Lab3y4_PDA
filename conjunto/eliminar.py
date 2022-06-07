print ("hola")
data = [["Lucas Baldezzari",324435235],["culito", 8520]]
data2=[]
for i in data:
    list1= i[0]
    list2= i[1]
    diccest= dict({list1: list2})
    for key, value in diccest.items():
        if value!=324435235:
            lista=[key, value]
            data2.append(lista)

print(data2)

print ("hola2")
