import random

# Definir tareas y servidores
# Lista de servidores
servidores = [
    {'id': 1, 'cpu': 10, 'memoria': 72, 'bajo_consumo': 56, 'alto_consumo': 236},
    {'id': 2, 'cpu': 16, 'memoria': 69, 'bajo_consumo': 105, 'alto_consumo': 338},
    {'id': 3, 'cpu': 7, 'memoria': 20, 'bajo_consumo': 67, 'alto_consumo': 422},
    {'id': 4, 'cpu': 19, 'memoria': 41, 'bajo_consumo': 144, 'alto_consumo': 484},
    {'id': 5, 'cpu': 7, 'memoria': 56, 'bajo_consumo': 136, 'alto_consumo': 457},
    {'id': 6, 'cpu': 21, 'memoria': 28, 'bajo_consumo': 93, 'alto_consumo': 377},
    {'id': 7, 'cpu': 27, 'memoria': 72, 'bajo_consumo': 67, 'alto_consumo': 484},
    {'id': 8, 'cpu': 18, 'memoria': 86, 'bajo_consumo': 55, 'alto_consumo': 478},
    {'id': 9, 'cpu': 9, 'memoria': 83, 'bajo_consumo': 114, 'alto_consumo': 427},
    {'id': 10, 'cpu': 7, 'memoria': 91, 'bajo_consumo': 60, 'alto_consumo': 433}
]

# Lista de tareas
tareas = [
    {'id': 1, 'cpu': 6, 'memoria': 7, 'time': 25, 'prioridad': 'Baja'},
    {'id': 2, 'cpu': 2, 'memoria': 5, 'time': 37, 'prioridad': 'Media'},
    {'id': 3, 'cpu': 6, 'memoria': 15, 'time': 44, 'prioridad': 'Media'},
    {'id': 4, 'cpu': 1, 'memoria': 11, 'time': 5, 'prioridad': 'Media'},
    {'id': 5, 'cpu': 3, 'memoria': 13, 'time': 6, 'prioridad': 'Alta'},
    {'id': 6, 'cpu': 8, 'memoria': 8, 'time': 12, 'prioridad': 'Media'},
    {'id': 7, 'cpu': 1, 'memoria': 15, 'time': 101, 'prioridad': 'Baja'},
    {'id': 8, 'cpu': 8, 'memoria': 14, 'time': 101, 'prioridad': 'Baja'},
    {'id': 9, 'cpu': 5, 'memoria': 11, 'time': 76, 'prioridad': 'Alta'},
    {'id': 10, 'cpu': 5, 'memoria': 9, 'time': 68, 'prioridad': 'Alta'},
    {'id': 11, 'cpu': 2, 'memoria': 4, 'time': 111, 'prioridad': 'Alta'},
    {'id': 12, 'cpu': 6, 'memoria': 5, 'time': 54, 'prioridad': 'Media'},
    {'id': 13, 'cpu': 3, 'memoria': 4, 'time': 31, 'prioridad': 'Media'},
    {'id': 14, 'cpu': 3, 'memoria': 8, 'time': 79, 'prioridad': 'Baja'},
    {'id': 15, 'cpu': 4, 'memoria': 9, 'time': 45, 'prioridad': 'Alta'},
    {'id': 16, 'cpu': 7, 'memoria': 6, 'time': 21, 'prioridad': 'Media'},
    {'id': 17, 'cpu': 3, 'memoria': 15, 'time': 97, 'prioridad': 'Media'},
    {'id': 18, 'cpu': 5, 'memoria': 15, 'time': 20, 'prioridad': 'Media'},
    {'id': 19, 'cpu': 8, 'memoria': 8, 'time': 68, 'prioridad': 'Alta'},
    {'id': 20, 'cpu': 6, 'memoria': 9, 'time': 61, 'prioridad': 'Baja'},
    {'id': 21, 'cpu': 5, 'memoria': 8, 'time': 74, 'prioridad': 'Baja'},
    {'id': 22, 'cpu': 7, 'memoria': 7, 'time': 110, 'prioridad': 'Media'},
    {'id': 23, 'cpu': 1, 'memoria': 4, 'time': 30, 'prioridad': 'Baja'},
    {'id': 24, 'cpu': 2, 'memoria': 9, 'time': 27, 'prioridad': 'Baja'},
    {'id': 25, 'cpu': 3, 'memoria': 12, 'time': 79, 'prioridad': 'Alta'},
    {'id': 26, 'cpu': 1, 'memoria': 13, 'time': 79, 'prioridad': 'Baja'},
    {'id': 27, 'cpu': 4, 'memoria': 3, 'time': 46, 'prioridad': 'Media'},
    {'id': 28, 'cpu': 5, 'memoria': 3, 'time': 37, 'prioridad': 'Baja'},
    {'id': 29, 'cpu': 5, 'memoria': 2, 'time': 43, 'prioridad': 'Alta'},
    {'id': 30, 'cpu': 3, 'memoria': 15, 'time': 95, 'prioridad': 'Baja'},
    {'id': 31, 'cpu': 4, 'memoria': 9, 'time': 45, 'prioridad': 'Baja'},
    {'id': 32, 'cpu': 4, 'memoria': 5, 'time': 45, 'prioridad': 'Baja'},
    {'id': 33, 'cpu': 5, 'memoria': 13, 'time': 108, 'prioridad': 'Alta'},
    {'id': 34, 'cpu': 4, 'memoria': 4, 'time': 113, 'prioridad': 'Baja'},
    {'id': 35, 'cpu': 8, 'memoria': 14, 'time': 116, 'prioridad': 'Media'},
    {'id': 36, 'cpu': 2, 'memoria': 5, 'time': 92, 'prioridad': 'Baja'},
    {'id': 37, 'cpu': 8, 'memoria': 7, 'time': 89, 'prioridad': 'Alta'},
    {'id': 38, 'cpu': 3, 'memoria': 8, 'time': 39, 'prioridad': 'Alta'},
    {'id': 39, 'cpu': 2, 'memoria': 16, 'time': 98, 'prioridad': 'Baja'},
    {'id': 40, 'cpu': 2, 'memoria': 2, 'time': 8, 'prioridad': 'Media'},
    {'id': 41, 'cpu': 3, 'memoria': 3, 'time': 65, 'prioridad': 'Media'},
    {'id': 42, 'cpu': 4, 'memoria': 12, 'time': 70, 'prioridad': 'Media'},
    {'id': 43, 'cpu': 5, 'memoria': 12, 'time': 16, 'prioridad': 'Media'},
    {'id': 44, 'cpu': 4, 'memoria': 6, 'time': 65, 'prioridad': 'Media'},
    {'id': 45, 'cpu': 2, 'memoria': 16, 'time': 30, 'prioridad': 'Baja'},
    {'id': 46, 'cpu': 5, 'memoria': 3, 'time': 98, 'prioridad': 'Media'},
    {'id': 47, 'cpu': 4, 'memoria': 5, 'time': 90, 'prioridad': 'Media'},
    {'id': 48, 'cpu': 8, 'memoria': 15, 'time': 7, 'prioridad': 'Media'},
    {'id': 49, 'cpu': 7, 'memoria': 12, 'time': 33, 'prioridad': 'Media'},
    {'id': 50, 'cpu': 1, 'memoria': 5, 'time': 73, 'prioridad': 'Baja'}
]


# Aquí se recogerán las funciones auxiliares que se han utilizado en el código principal para que este sea más legible y fácil de entender.
def inicializar_poblacion(pop_size, num_tareas, num_servers):
    poblacion = []
    for _ in range(pop_size):
        individuo = [random.randint(1, num_servers) for _ in range(num_tareas)]  # Asigna aleatoriamente servidores
        poblacion.append(individuo)
    return poblacion


def fitness(individuo, tareas, servers, penalizacion_alta, penalizacion_media):
    total_energia = 0
    total_carga = [{'cpu': 0, 'memoria': 0} for _ in servers]  # Carga por servidor
    penalizacion_prioridad = 0  # Penalización por prioridades no atendidas

    for i, tarea in enumerate(tareas):
        server_index = individuo[i] - 1  # Ajustar el índice del servidor
        server = servers[server_index]

        # Acumular carga
        total_carga[server_index]['cpu'] += tarea['cpu']
        total_carga[server_index]['memoria'] += tarea['memoria']

        # Calcular consumo energético basado en la carga
        if total_carga[server_index]['cpu'] <= server['cpu'] * 0.75:  # Baja carga
            total_energia += server['bajo_consumo']
        else:  # Alta carga
            total_energia += server['alto_consumo']

        # Penalización por prioridades
        if tarea['prioridad'] == 'Alta':
            penalizacion_prioridad += penalizacion_alta  # Penalización mayor para tareas altas
        elif tarea['prioridad'] == 'Media':
            penalizacion_prioridad += penalizacion_media  # Penalización menor para tareas medias

    # Penalización por sobrecarga de CPU o memoria
    penalizacion_sobrecarga = sum(1 for carga, server in zip(total_carga, servers) if
                                  carga['cpu'] > server['cpu'] or carga['memoria'] > server['memoria'])

    # Convertir el fitness a positivo
    fitness_value = 1 / (1 + total_energia + penalizacion_sobrecarga + penalizacion_prioridad)
    return fitness_value * 10000


# FUNCIONES DE SELECCIÓN
def ruleta(poblacion, fitnesses):
    total_fitness = sum(fitnesses)
    seleccion = random.uniform(0, total_fitness)
    actual = 0
    for i, fitness_valor in enumerate(fitnesses):
        actual += fitness_valor
        if actual >= seleccion:
            return poblacion[i]
    return poblacion[-1]  # Si no se selecciona ningún individuo, se devuelve el último


def torneo(poblacion, fitnesses, k=3):
    # Selecciona aleatoriamente 'k' individuos y elige el de mayor fitness
    participantes = random.sample(range(len(poblacion)), k)  # Índices de los participantes
    mejor = max(participantes, key=lambda idx: fitnesses[idx])
    return poblacion[mejor]


def seleccion_por_ranking(poblacion, fitnesses):
    # Ordenar la población por fitness y asignar probabilidades basadas en el ranking
    ranking = sorted(range(len(fitnesses)), key=lambda idx: fitnesses[idx], reverse=True)
    # Asignar probabilidades de selección en función de la posición en el ranking
    total_ranking = sum(range(1, len(poblacion) + 1))
    seleccion = random.uniform(0, total_ranking)
    acumulado = 0
    for i, idx in enumerate(ranking):
        acumulado += (len(poblacion) - i)  # Más probabilidad para los de mejor ranking
        if acumulado >= seleccion:
            return poblacion[idx]
    return poblacion[ranking[-1]]  # En caso de error, devolver el último


def truncamiento(poblacion, fitnesses, porcentaje=0.5):
    # Ordenar la población por fitness en orden descendente
    num_seleccionados = int(len(poblacion) * porcentaje)
    elite_indices = sorted(range(len(fitnesses)), key=lambda idx: fitnesses[idx], reverse=True)[:num_seleccionados]
    # Seleccionar al azar dentro de la elite
    elegido = random.choice(elite_indices)
    return poblacion[elegido]


# FUNCIONES DE CRUCE
def cruce_un_punto(padre1, padre2, prob_cruce):
    if random.random() < prob_cruce:  # Probabilidad de cruce
        point = random.randint(1, len(padre1) - 1)
        descendiente1 = padre1[:point] + padre2[point:]
        descendiente2 = padre2[:point] + padre1[point:]
        return descendiente1, descendiente2
    return padre1, padre2  # Si no ocurre cruce, los padres son los descendientes


def cruce_multipunto(padre1, padre2, prob_cruce, points=2):
    if random.random() < prob_cruce:  # Probabilidad de cruce del 80%
        point1 = random.randint(1, len(padre1) - 2)
        point2 = random.randint(point1 + 1, len(padre1) - 1)
        descendiente1 = padre1[:point1] + padre2[point1:point2] + padre1[point2:]
        descendiente2 = padre2[:point1] + padre1[point1:point2] + padre2[point2:]
        return descendiente1, descendiente2
    return padre1, padre2  # Si no ocurre cruce, los padres son los descendientes


# FUNCIONES DE MUTACIÓN
# Mutación 1: Cambiar el servidor asignado a una tarea
def mutacion1(individuo, prob_mutacion):
    for i in range(len(individuo)):
        if random.random() < prob_mutacion:  # Probabilidad de mutación del 10%
            individuo[i] = random.randint(1, len(servidores))  # Cambiar servidor asignado
    return individuo


# Mutación 2: Intercambiar los servidores de dos tareas
def mutacion2(individuo, prob_mutacion):
    if random.random() < prob_mutacion:
        # Seleccionar dos posiciones aleatorias para intercambiar
        pos1 = random.randint(0, len(individuo) - 1)
        pos2 = random.randint(0, len(individuo) - 1)

        # Intercambiar las asignaciones de tareas en estas posiciones
        individuo[pos1], individuo[pos2] = individuo[pos2], individuo[pos1]
    return individuo


# FUNCIONES DE REEMPLAZO
# Reemplazo 1: Reemplaza toda la población actual con la nueva población de descendientes
def reemplazo_generacional(poblacion, nueva_poblacion):
    # Reemplaza toda la población con los descendientes
    return nueva_poblacion


# Reemplazo 2:  Reemplaza un porcentaje tasa_reemplazo de la población con los individuos de la nueva población de descendientes
def reemplazo_estacionario(poblacion, nueva_poblacion, penalizacion_alta, penalizacion_media, tasa_reemplazo=0.2):
    # Reemplazar el 20% de la población con nuevos individuos
    num_reemplazos = int(len(poblacion) * tasa_reemplazo)
    poblacion_ordenada = sorted(poblacion,
                                key=lambda ind: fitness(ind, tareas, servidores, penalizacion_alta, penalizacion_media),
                                reverse=True)
    return poblacion_ordenada[:-num_reemplazos] + nueva_poblacion[:num_reemplazos]
