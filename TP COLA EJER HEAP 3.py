class Operacion:
    def __init__(self, encargado, descripcion, hora, nivel, stormtroopers=0):
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.nivel = nivel
        self.stormtroopers = stormtroopers

    def __lt__(self, other):
        # Invertimos la comparación para que el heap funcione como una cola de prioridad
        return self.nivel > other.nivel  # Prioridad más alta para niveles más bajos

    def __repr__(self):
        return (f"Operacion(encargado='{self.encargado}', descripcion='{self.descripcion}', "
                f"hora='{self.hora}', nivel={self.nivel}, stormtroopers={self.stormtroopers})")


class Heap:
    def __init__(self):
        self.heap = []

    def insertar(self, operacion):
        self.heap.append(operacion)
        self._heapify_up(len(self.heap) - 1)

    def atender(self):
        if not self.heap:
            return None
        # Intercambiar el primer elemento con el último y eliminar el último
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        operacion_atendida = self.heap.pop()
        self._heapify_down(0)
        return operacion_atendida

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __len__(self):
        return len(self.heap)


# a) Definir los niveles de prioridad
nivel_tres = 3
nivel_dos = 2
nivel_uno = 1

# b) Cargar las operaciones iniciales
operaciones = [
    Operacion('Snoke', 'Solicitar refuerzos', '10:00', nivel_tres, 10),
    Operacion('Kylo Ren', 'Investigar anomalías', '10:15', nivel_tres, 15),
    Operacion('Capitán Phasma', 'Revisar armamento', '10:30', nivel_dos),
    Operacion('Capitán Phasma', 'Patrullar zona', '10:45', nivel_dos, 20),
    Operacion('General Hux', 'Analizar reportes', '11:00', nivel_uno),
    Operacion('General Hux', 'Preparar estrategia', '11:15', nivel_uno),
    Operacion('General Hux', 'Coordinar operaciones', '11:30', nivel_uno, 5),
    Operacion('General Hux', 'Inspeccionar tropas', '11:45', nivel_uno, 8),
]

# c) Crear la cola de prioridad
cola_prioridad = Heap()

for operacion in operaciones:
    cola_prioridad.insertar(operacion)

# d) Realizar la atención de las operaciones
for i in range(5):
    atendida = cola_prioridad.atender()
    print(f"Operación atendida: {atendida}")

# e) Agregar operación después de atender la quinta
nueva_operacion = Operacion('Capitán Phasma', 'Revisión de intrusos en el hangar B7', '12:00', nivel_dos, 25)
cola_prioridad.insertar(nueva_operacion)

# f) Atender la sexta operación
atendida_sexta = cola_prioridad.atender()
print(f"Operación atendida: {atendida_sexta}")

# g) Agregar operación después de atender la sexta
nueva_operacion_snoke = Operacion('Snoke', 'Destruir el planeta Takodana', '12:15', nivel_tres)
cola_prioridad.insertar(nueva_operacion_snoke)

