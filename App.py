from numpy import insert
from Product import Product
from List import List



# print('- instancia lista')

produto1 = Product('Teste de produto1', 1.0)
produto2 = Product('Teste de produto2', 2.0)
produto3 = Product('Teste de produto3', 3.0)
produto4 = Product('Teste de produto4', 4.0)



lista = List(5)


# # print(produtoTeste)

print('- exibe a lista: ')
print(lista) #lista visivel
print()
print('- exibe a lista total')
print(lista.getList())
print()

print('insere o produto 1')
lista.insertElement(produto1)
print()

print('- exibe a lista: ')
print(lista) #lista visivel
print()
print('- exibe a lista total')
print(lista.getList())

print()
print(lista.getPointerIndex('start'))
print(lista.getPointerIndex('end'))

