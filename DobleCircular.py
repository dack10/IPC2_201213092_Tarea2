
from Nodo import Nodo

class ListaDobleCircular:
    def __init__(self):
        self.inicio=None
        self.ultimo=self.inicio
    def append(self,dato):
        nuevo=Nodo(dato)
        if self.inicio is None:
            self.inicio=nuevo
            nuevo.siguiente=self.inicio
            nuevo.anterior=self.inicio
            self.ultimo=nuevo

        elif self.inicio.siguiente is None:
            self.inicio.siguiente=nuevo
            nuevo.anterior=self.inicio
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
            self.ultimo=nuevo
        else:
            self.ultimo.siguiente=nuevo
            nuevo.anterior=self.ultimo
            nuevo.siguiente=self.inicio
            self.inicio.anterior=nuevo
            self.ultimo=nuevo
    def print(self):
        aux=self.inicio
        if aux!=None:
            while aux!=None:
                print(aux.numero)
                aux=aux.siguiente
                if aux==self.inicio:
                    break
    
    def buscarAnterior(self,numero):
        aux=self.inicio
        if aux!=None:
            while aux!=None:
                if aux.numero==numero:
                    print("ANTERIOR: ",aux.anterior.numero)
                    break
                aux=aux.siguiente
    
    def buscarSiguiente(self,numero):
        aux=self.inicio
        if aux!=None:
            while aux!=None:
                if aux.numero==numero:
                    print("SIGUIENTE: ",aux.siguiente.numero)
                    break
                aux=aux.siguiente

                

lista=ListaDobleCircular()
lista.append(2)
lista.append(7)
lista.append(5)
lista.append(11)
lista.append(4)
print("ELEMENTOS DE LA LISTA CIRCULAR")
lista.print()
num=int(input("INGRESE UN NUMERO DE LA LISTA: "))
lista.buscarAnterior(num)
print("ACTUAL: ",num)
lista.buscarSiguiente(num)
