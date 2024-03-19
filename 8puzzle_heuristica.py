from queue import PriorityQueue  # Utilizamos PriorityQueue para ordenar los nodos según la heurística

class Puzzle8:
    def __init__(self, estado_inicial, estado_meta):
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta
        self.cola_prioridad = PriorityQueue()  # Cambiamos a una cola de prioridad
        self.visitados = []

    def obtener_movimientos(self, estado):
        movimientos = []
        espacio_vacio = estado.index(0)

        if espacio_vacio >= 3:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 3] = nuevo_estado[espacio_vacio - 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio <= 5:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 3] = nuevo_estado[espacio_vacio + 3], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio % 3 != 0:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio - 1] = nuevo_estado[espacio_vacio - 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        if espacio_vacio % 3 != 2:
            nuevo_estado = estado[:]
            nuevo_estado[espacio_vacio], nuevo_estado[espacio_vacio + 1] = nuevo_estado[espacio_vacio + 1], nuevo_estado[espacio_vacio]
            movimientos.append(nuevo_estado)

        return movimientos

    def heuristica(self, estado):
        # La heurística cuenta cuántos nodos están en la posición correcta en relación con el estado objetivo
        return sum(1 for i, j in zip(estado, self.estado_meta) if i == j)

    def busqueda_heuristica(self):
        self.cola_prioridad.put((self.heuristica(self.estado_inicial), self.estado_inicial, []))

        while not self.cola_prioridad.empty():
            _, estado, path = self.cola_prioridad.get()
            self.visitados.append(estado)

            if estado == self.estado_meta:
                return path

            for movimiento in self.obtener_movimientos(estado):
                if movimiento not in self.visitados:
                    self.cola_prioridad.put((self.heuristica(movimiento), movimiento, path + [movimiento]))

    @staticmethod
    def dibujar_puzzle(estado):
        for i in range(3):
            for j in range(3):
                if estado[i * 3 + j] == 0:
                    print("|   ", end="")
                else:
                    print(f"| {estado[i * 3 + j]} ", end="")
            print("|")
            print("+---+---+---+")

estado_inicial = [0, 1, 3, 4, 2, 6, 7, 5, 8]
estado_meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle_solver = Puzzle8(estado_inicial, estado_meta)
solucion = puzzle_solver.busqueda_heuristica()

if solucion:
    print("Se encontró una solución:")
    for paso, estado in enumerate(solucion):
        print(f"Paso {paso + 1}:")
        Puzzle8.dibujar_puzzle(estado)
else:
    print("No se encontró una solución.")
