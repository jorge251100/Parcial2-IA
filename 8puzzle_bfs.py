from queue import Queue  # Importa la clase Queue del módulo queue

class Puzzle8:  # Define la clase Puzzle8 para resolver el problema del rompecabezas de 8 piezas
    def __init__(self, estado_inicial, estado_meta):  # Método de inicialización de la clase Puzzle8
        self.estado_inicial = estado_inicial  # Guarda el estado inicial del rompecabezas
        self.estado_meta = estado_meta  # Guarda el estado objetivo del rompecabezas
        self.cola = Queue()  # Inicializa una cola para la búsqueda en amplitud
        self.visitados = []  # Inicializa una lista para almacenar los estados visitados durante la búsqueda

    def obtener_movimientos(self, estado):  # Método para obtener los movimientos posibles desde un estado dado
        movimientos = []  # Inicializa una lista para almacenar los movimientos posibles
        espacio_vacio = estado.index(0)  # Encuentra la posición del espacio vacío en el estado actual

        # Movimiento hacia arriba
        if espacio_vacio >= 3:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 3] = nuevo_estado[espacio_vacio - 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        # Movimiento hacia abajo
        if espacio_vacio <= 5:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 3] = nuevo_estado[espacio_vacio + 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        # Movimiento hacia la izquierda
        if espacio_vacio % 3 != 0:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 1] = nuevo_estado[espacio_vacio - 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        # Movimiento hacia la derecha
        if espacio_vacio % 3 != 2:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 1] = nuevo_estado[espacio_vacio + 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        return movimientos  # Retorna la lista de movimientos posibles

    def busqueda_amplitud(self):  # Método para realizar la búsqueda en amplitud
        self.cola.put((self.estado_inicial, []))  # Agrega el estado inicial y una lista vacía al frente de la cola

        while not self.cola.empty():  # Mientras la cola no esté vacía
            estado, path = self.cola.get()  # Obtiene el estado y el camino desde el frente de la cola
            self.visitados.append(estado)  # Agrega el estado a la lista de visitados

            if estado == self.estado_meta:  # Si el estado actual es el estado objetivo
                return path  # Retorna el camino que lleva a ese estado

            for movimiento in self.obtener_movimientos(estado):  # Para cada movimiento posible desde el estado actual
                if movimiento not in self.visitados:  # Si el estado resultante no ha sido visitado
                    self.cola.put((movimiento, path + [movimiento]))  # Agrega el nuevo estado y el camino a la cola

    @staticmethod #Decorador en python, así definimos un método estatico dentro de una clase
    def dibujar_puzzle(estado):  # Método estático para dibujar el rompecabezas
        for i in range(3):  # Itera sobre las filas del rompecabezas
            for j in range(3):  # Itera sobre las columnas del rompecabezas
                if estado[i * 3 + j] == 0:  # Si la casilla está vacía
                    print("|   ", end="")  # Imprime una casilla vacía
                else:
                    print(f"| {estado[i * 3 + j]} ", end="")  # Imprime el valor de la casilla
            print("|")  # Imprime el separador de columna
            print("+---+---+---+")  # Imprime el separador de fila

estado_inicial = [0, 1, 3, 4, 2, 6, 7, 5, 8]  # Define el estado inicial del rompecabezas
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Define el estado objetivo del rompecabezas

puzzle_solver = Puzzle8(estado_inicial, estado_meta)  # Crea una instancia de Puzzle8 con los estados inicial y objetivo
solucion = puzzle_solver.busqueda_amplitud()  # Realiza la búsqueda en amplitud para encontrar la solución

if solucion:  # Si se encontró una solución
    print("Se encontró una solución:")  # Imprime un mensaje indicando que se encontró una solución
    for paso, estado in enumerate(solucion):  # Itera sobre cada paso y estado en la solución
        print(f"Paso {paso + 1}:")  # Imprime el número de paso
        Puzzle8.dibujar_puzzle(estado)  # Dibuja el rompecabezas para el estado actual
else:  # Si no se encontró una solución
    print("No se encontró una solución.")  # Imprime un mensaje indicando que no se encontró una solución
