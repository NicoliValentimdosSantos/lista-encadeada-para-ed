class Node:
    def __init__(self, nome):
        self.nome = nome
        self.next = None

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def checar(self, node: Node):
        if (self.head == None):
            self.head = node
            return

        node.next = self.head
        self.head = node

    def append(self, novo: Node):
        if self.head == None:
            self.head = novo
            return
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = novo

    def remove(self, indice: int):
        if (indice == 0):
            temp = self.head
            self.head = self.head.next
            return temp
        lugar = 1
        previous = self.head
        current = self.head.next
        while (lugar < indice):
            previous = current
            current = current.next
            lugar = lugar + 1
        previous.next = current.next
        return current

    def mostrar(self):
        current = self.head
        while (current != None):
            print(current.nome)
            current = current.next


obra1 = Node('1984')
obra2 = Node('O Jardineiro Noturno')
obra3 = Node('Blade Runner')
obra4 = Node('O Hobbit')
obra5 = Node('Fundação')
obra6 = Node('O Pequeno Príncipe')
lista_de_leitura = SimpleLinkedList()
lista_de_leitura.append(obra1)
lista_de_leitura.append(obra2)
lista_de_leitura.append(obra3)
lista_de_leitura.append(obra4)
lista_de_leitura.append(obra5)
lista_de_leitura.append(obra6)
continuar = 's'
while continuar == 's':
    if lista_de_leitura.head == None:
        print('este livro já pode ter sido finalizado')
        break

    print('Sua lista de leituras pendentes:\n')
    lista_de_leitura.mostrar()
    print('Qual leitura foi terminada ?')
    print('Digite a posição de seu livro :')
    codigo = int(input())

    if codigo == 1:
        finalizado = lista_de_leitura.remove(0)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    elif codigo == 2:
        finalizado = lista_de_leitura.remove(1)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    elif codigo == 3:
        finalizado = lista_de_leitura.remove(2)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    elif codigo == 4:
        finalizado = lista_de_leitura.remove(3)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    elif codigo == 5:
        finalizado = lista_de_leitura.remove(4)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    elif codigo == 6:
        finalizado = lista_de_leitura.remove(5)
        print('Você finalizou a obra', finalizado.nome)
        print('Leitura finalizada com sucesso!\nContinue lendo!')
        print('Continuar?, DIGITE s para SIM ou n para NÃO ')
        continuar = str(input())

    else:
        print('Posição desejada não disponível no momento')
        print('Deseja continuar?')
        continuar = str(input())
print('Boa Leitura.')