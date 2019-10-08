n = input("Numero de clientes: ")
n = int(n)

if n < 1:
    exit()

clients = []

for i in range(n):
    inp = input()
    try:
        slipted = inp.split(" ")
        clients.append([int(slipted[0]), int(slipted[1])])
    except Exception as identifier:
        clients.append([i,0])

def takeSecond(elem):
    return elem[1]

clients.sort(key=takeSecond)
print(clients)
