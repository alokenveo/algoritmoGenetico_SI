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


# Funciones auxiliares

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
    return fitness_value*10000


def ruleta(poblacion, fitnesses):
    total_fitness = sum(fitnesses)
    seleccion = random.uniform(0, total_fitness)
    actual = 0
    for i, fitness_valor in enumerate(fitnesses):
        actual += fitness_valor
        if actual >= seleccion:
            return poblacion[i]
    return poblacion[-1]  # Si no se selecciona ningún individuo, se devuelve el último

def cruce(padre1, padre2,prob_cruce, points=2):
    if random.random() < prob_cruce:  # Probabilidad de cruce del 80%
        point1 = random.randint(1, len(padre1) - 2)
        point2 = random.randint(point1 + 1, len(padre1) - 1)
        descendiente1 = padre1[:point1] + padre2[point1:point2] + padre1[point2:]
        descendiente2 = padre2[:point1] + padre1[point1:point2] + padre2[point2:]
        return descendiente1, descendiente2
    return padre1, padre2  # Si no ocurre cruce, los padres son los descendientes


def mutacion(individuo, prob_mutacion):
    for i in range(len(individuo)):
        if random.random() < prob_mutacion:  # Probabilidad de mutación del 10%
            individuo[i] = random.randint(1, len(servidores))  # Cambiar servidor asignado
    return individuo


def reemplazo(poblacion, nueva_poblacion,penalizacion_alta,penalizacion_media, tasa_reemplazo=0.2):
    # Reemplazar el 20% de la población con nuevos individuos
    num_reemplazos = int(len(poblacion) * tasa_reemplazo)
    poblacion_ordenada = sorted(poblacion, key=lambda ind: fitness(ind, tareas, servidores,penalizacion_alta,penalizacion_media), reverse=True)
    return poblacion_ordenada[:-num_reemplazos] + nueva_poblacion[:num_reemplazos]


def algoritmo_genetico(pop_size, generations, tareas, servidores,prob_cruce,prob_mutacion,penalizacion_alta,penalizacion_media):
    poblacion = inicializar_poblacion(pop_size, len(tareas), len(servidores))
    mejor_solucion = None
    mejor_fitness = float('-inf')
    mejor_generacion = 0

    for generacion in range(generations):
        fitnesses = [fitness(ind, tareas, servidores,penalizacion_alta,penalizacion_media) for ind in poblacion]
        nueva_poblacion = []

        # Crear nuevos individuos a través de cruce y mutación
        for _ in range(pop_size // 2):
            padre1 = ruleta(poblacion, fitnesses)
            padre2 = ruleta(poblacion, fitnesses)
            descendiente1, descendiente2 = cruce(padre1, padre2, prob_cruce)
            nueva_poblacion.extend([mutacion(descendiente1,prob_mutacion), mutacion(descendiente2,prob_mutacion)])

        # Reemplazar parte de la población
        poblacion = reemplazo(poblacion, nueva_poblacion,penalizacion_alta,penalizacion_media)

        # Evaluar mejor individuo de la generación actual
        mejor_individuo_generacion = max(poblacion, key=lambda ind: fitness(ind, tareas, servidores,penalizacion_alta,penalizacion_media))
        mejor_fitness_generacion = fitness(mejor_individuo_generacion, tareas, servidores, penalizacion_alta,penalizacion_media)


        print(
            f"Generación {generacion + 1}, Mejor fitness: {mejor_fitness_generacion}, Mejor solución: {mejor_individuo_generacion}")

        # Actualizar la mejor solución global si es necesario
        if mejor_fitness_generacion >= mejor_fitness:
            mejor_solucion = mejor_individuo_generacion
            mejor_fitness = mejor_fitness_generacion
            mejor_generacion = generacion + 1

    print(f"\nMejor solución encontrada, Generación {mejor_generacion}: {mejor_solucion}, Fitness: {mejor_fitness}")


# Ejecutamos el main
if __name__ == "__main__":
    population_size = 10
    generations = 100
    penalizacion_alta=10
    penalizacion_media=5
    prob_cruce=0.8
    prob_mutacion=0.1

    # Ejecutar algoritmo genético
    algoritmo_genetico(population_size, generations, tareas, servidores,prob_cruce,prob_mutacion,penalizacion_alta,penalizacion_media)
