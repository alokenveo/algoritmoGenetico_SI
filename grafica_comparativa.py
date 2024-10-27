import matplotlib.pyplot as plt

from main import reemplazo, ruleta, inicializar_poblacion, cruce, mutacion, tareas, servidores, fitness


# Algoritmo genético principal con parámetros configurables
def algoritmo_genetico(pop_size, generations, tareas, servidores, penalizacion_alta, penalizacion_media, prob_cruce, prob_mutacion):
    poblacion = inicializar_poblacion(pop_size, len(tareas), len(servidores))
    fitness_generacion = []  # Almacenar fitness promedio por generación

    for generacion in range(generations):
        fitnesses = [fitness(ind, tareas, servidores, penalizacion_alta, penalizacion_media) for ind in poblacion]
        fitness_generacion.append(sum(fitnesses) / len(fitnesses))  # Fitness promedio

        nueva_poblacion = []
        for _ in range(pop_size // 2):
            padre1 = ruleta(poblacion, fitnesses)
            padre2 = ruleta(poblacion, fitnesses)
            descendiente1, descendiente2 = cruce(padre1, padre2,prob_cruce)
            nueva_poblacion.extend([mutacion(descendiente1, prob_mutacion), mutacion(descendiente2, prob_mutacion)])

        poblacion = reemplazo(poblacion, nueva_poblacion,penalizacion_alta,penalizacion_media)

    return fitness_generacion

# Configuración de los experimentos
configuraciones = [
    {"pop_size": 10, "generations": 50, "penalizacion_alta": 20, "penalizacion_media": 10, "prob_cruce": 0.8, "prob_mutacion": 0.1, "label": "Config A - 10/50"},
    {"pop_size": 10, "generations": 50, "penalizacion_alta": 10, "penalizacion_media": 5, "prob_cruce": 0.8, "prob_mutacion": 0.1, "label": "Config B - 10/50"},
    {"pop_size": 10, "generations": 50, "penalizacion_alta": 5, "penalizacion_media": 2, "prob_cruce": 0.8, "prob_mutacion": 0.1, "label": "Config C - 10/50"},

    #Configuración predeterminada
    {"pop_size": 10, "generations": 100, "penalizacion_alta": 10, "penalizacion_media": 5, "prob_cruce": 0.8, "prob_mutacion": 0.1, "label": "Config X - 10/100"},

    {"pop_size": 20, "generations": 100, "penalizacion_alta": 20, "penalizacion_media": 10, "prob_cruce": 0.6, "prob_mutacion": 0.2, "label": "Config D - 20/100"},
    {"pop_size": 20, "generations": 100, "penalizacion_alta": 10, "penalizacion_media": 5, "prob_cruce": 0.6, "prob_mutacion": 0.2, "label": "Config E - 20/100"},
    {"pop_size": 20, "generations": 100, "penalizacion_alta": 5, "penalizacion_media": 2, "prob_cruce": 0.6, "prob_mutacion": 0.2, "label": "Config F - 20/100"}
]

# Ejecutar experimentos y almacenar resultados
resultados = {}
for config in configuraciones:
    label = config["label"]
    resultados[label] = algoritmo_genetico(
        pop_size=config["pop_size"],
        generations=config["generations"],
        tareas=tareas,
        servidores=servidores,
        penalizacion_alta=config["penalizacion_alta"],
        penalizacion_media=config["penalizacion_media"],
        prob_cruce=config["prob_cruce"],
        prob_mutacion=config["prob_mutacion"]
    )

# Graficar resultados
plt.figure(figsize=(12, 6))
for label, fitness_generacion in resultados.items():
    plt.plot(fitness_generacion, label=label)

plt.xlabel("Generación")
plt.ylabel("Fitness Promedio")
plt.title("Comparación de Fitness para Diferentes Configuraciones")
plt.legend()
plt.grid(True)
plt.show()
