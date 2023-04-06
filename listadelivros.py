class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def adicionar_no_final(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev =  self.tail
            self.tail.next = new_node
            self.tail = new_node


    def adicionar_no_começo(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def adicionar_apos_no(self, node,value):
        if Node is None:
            return
        new_node = Node(value)
        new_node.prev = node 
        new_node.next = node.next
        if node.next is not None:
            node.next.prev = new_node
        else:
            self.tail = new_node
        node.next = new_node 


    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value , end= ' ')
            current_node = current_node.next
        print()

    def bubble_sort(self):
        if self.head is None:
            return
        end_node = None
        while end_node != self.head:
            current_node = self.head
            while current_node.next != end_node:
                next_node = current_node.next
                if current_node.value > next_node.value:
                    current_node.value, next_node.value = next_node.value, current_node.value
                current_node = current_node.next
            end_node = current_node


class ListaLivros:
    def __init__(self):
        self.items = DoublyLinkedList()
    
    def add_item(self, item):
        self.items.adicionar_no_final(item)
        self.items.bubble_sort()

    def remove_item(self, item):
        node = self.items.head
        while node is not None and node.value != item:
            node = node.next
        if node is not None:
            if node == self.items.head:
                self.items.head = node.next
                if node.next is not None:
                    node.next.prev = None
                else:
                    self.items.tail = None
            elif node == self.items.tail:
                self.items.tail = node.prev
                if node.prev is not None:
                    node.prev.next = None
                else:
                    self.items.head = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
        else:
            print('O livro {} não está na lista.'.format(item))


    def print_list(self):
        self.items.print_list()

def main():
    lista_livro = ListaLivros()
    while True:
        print('\nO que você dejeja fazer hoje?') 
        print('1 Quero adicionar outro livro para a lista')
        print('2 Quero remover um livro da lista')
        print('3 Quero ver a lista atual')
        print('4 Não desejo fazer nada')
        choice = int(input("ESCOLHA UMA OPÇÂO:"))
        if choice == 1:
            item = input("Escreva a obra que deseja adicionar\n")
            lista_livro.add_item(item)
            print("o livro {} foi adicionado.".format(item))
        elif choice == 2:
            item = input("Escreva a obra que deseja remover\n")
            lista_livro.remove_item(item)
            print("o livro {} foi removido.".format(item))

        elif choice == 3:
            print('Mostrando lista:')
            lista_livro.print_list()

        elif choice == 4:
            print("tchau tchau")
            break
        else:
            print(" Ops! Essa opção não existe, por que não tenta mais uma vez.")
if __name__ == '__main__':
    main()          

            