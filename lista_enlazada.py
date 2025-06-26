class Nodo:
    """Clase Nodo para la lista simplemente enlazada"""

    def __init__(self, dato):
        self._dato = dato
        self._sig = None

    def set_dato(self, dato):
        self._dato = dato

    def get_dato(self):
        return self._dato

    def get_sig(self):
        return self._sig

    def set_sig(self, sig):
        if not isinstance(sig, Nodo):
            raise TypeError("El siguiente nodo debe ser de tipo Nodo")
        self._sig = sig

    def __repr__(self):
        return str(self._dato)

    def __str__(self):
        return f"Nodo: {self._dato}"


class ListaEnlazada:
    """Clase ListaEnlazada para la lista simplemente enlazada"""

    def __init__(self):
        """Todos los atributos de la clase son privados"""
        self._cabeza = None
        self._longitud = 0
        self._actual = None

    ##################################################
    """ Metodos publicos de la clase ListaEnlazada """
    ##################################################

    def agregar_al_final(self, dato):
        if self._esta_vacia():
            self._set_cabeza(Nodo(dato))
        else:
            aux = self._get_cabeza()
            while aux.get_sig() is not None:
                aux = aux.get_sig()
            aux.set_sig(Nodo(dato))
        self._incrementar_longitud()    
   

    ##################################################
    """ Metodos privados de la clase ListaEnlazada """

    ##################################################
    def _esta_vacia(self):
        return self._get_cabeza() is None

    def _get_cabeza(self):
        return self._cabeza

    def _set_cabeza(self, cabeza):
        if not isinstance(cabeza, Nodo):
            raise TypeError("La cabeza debe ser de tipo Nodo")
        self._cabeza = cabeza

    def _incrementar_longitud(self):
        self._longitud += 1

    def _decrementar_longitud(self):
        self._longitud -= 1

    def _validar_posicion(self, pos):
        # La posicion excede  la long de la lista
        if pos < 0 or pos >= self._longitud:  # Cambiado de > a >= No puedo asignar a la longitud (emulando la lista de python)
            raise IndexError

    def _recorrer_lista(self, pos):
        self._validar_posicion(pos)
        aux = self._get_cabeza()
        ant = None
        for _ in range(pos):
            ant = aux
            aux = aux.get_sig()
        return ant, aux
    
    def __repr__(self):
        resultado = "["
        aux = self._get_cabeza()
        if not aux:
            return "[]"
        while aux.get_sig() is not None:
            resultado += aux.__repr__()
            resultado += " -> "
            aux = aux.get_sig()
        resultado += aux.__repr__() + "]"
        return resultado

class ListaEdp(ListaEnlazada):

    def __init__(self):
        super().__init__()

    def agregar_en_posicion(self, pos, dato):
        self._validar_posicion(pos)
        # Inserto a la cabeza
        if pos == 0:
            aux = self._get_cabeza()
            nuevo = Nodo(dato)
            nuevo.set_sig(aux)
            self._incrementar_longitud()
            return
        # Inserto en el medio
        ant, aux = self._recorrer_lista(pos)
        nuevo = Nodo(dato)
        ant.set_sig(nuevo)
        nuevo.set_sig(aux)
        self._incrementar_longitud()

    def sacar_en_posicion(self, pos):
        self._validar_posicion(pos)
        # Quito a la cabeza
        if pos == 0:
            return self.desencolar()
        # Quito en el medio
        self._decrementar_longitud()
        ant, aux = self._recorrer_lista(pos)
        ant.set_sig(aux.get_sig())
        return aux
    
class Cola(ListaEnlazada):
    def __init__(self):
        super().__init__()
    
    def encolar(self, dato):
        super().agregar_al_final(dato)

    def desencolar(self):
        if not self._esta_vacia():
          self._decrementar_longitud()
          primero = self._get_cabeza()
          self._set_cabeza(primero.get_sig())
          return primero
        return None

lista = ListaEdp()
lista.agregar_al_final(4)
lista.agregar_al_final(5)
lista.agregar_al_final(6)
print(lista)

lista.agregar_en_posicion(1, "pos1")
print(lista)

pos1 = lista.sacar_en_posicion(1)
print(pos1)
print(lista)

cola = Cola()
cola.encolar(1)
cola.encolar(2)
print(cola)

primero = cola.desencolar()
print(primero)
print(cola)