# Edgar Moises Hernandez-Gonzalez
# 24/06/21
# crear lista de un diccionario con map y lambda
# todo es igual a todo_2

# crear listas de diccionarios
stock_refrescos_1 = {'Coca Cola': 10, 'Fresca': 15, 'Fanta': 13, 'Sprite': 12, 'Mundet': 14}
stock_refrescos_2 = {'Coca Cola': 20, 'Fresca': 25, 'Fanta': 23, 'Sprite': 22, 'Mundet': 24}
stock_refrescos_3 = {'Coca Cola': 30, 'Fresca': 35, 'Fanta': 33, 'Sprite': 32, 'Mundet': 34}
stock_refrescos_4 = {'Coca Cola': 40, 'Fresca': 45, 'Fanta': 43, 'Sprite': 42, 'Mundet': 44}
stock_refrescos_5 = {'Coca Cola': 50, 'Fresca': 55, 'Fanta': 53, 'Sprite': 52, 'Mundet': 54}
lista_1 = [stock_refrescos_1, stock_refrescos_2, stock_refrescos_3]
lista_2 = [stock_refrescos_4, stock_refrescos_5]
print('primera parte:', lista_1)
print('segunda parte:', lista_2)

# lista que tiene todo
todo = []
for item in lista_1:
    todo.append(item)
for item in lista_2:
    todo.append(item)
print('todo:', todo)

# lista 2 que tiene todo
todo_2 = []
todo_2 += list(map(lambda item: item, lista_1))
todo_2 += list(map(lambda item: item, lista_2))
print('todo 2:', todo)

for i in range(len(todo_2)):
    todo_2[i]['Ciel'] = 1000

for item in todo_2:
    item['Powerade'] = 2000

print('todo 2:', todo)