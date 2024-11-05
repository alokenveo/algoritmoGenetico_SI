from auxiliares import *


def aplicar_seleccion(poblacion, fitnesses, metodo_selec):
    if metodo_selec == 1:
        return ruleta(poblacion, fitnesses)
    elif metodo_selec == 2:
        return torneo(poblacion, fitnesses)
    elif metodo_selec == 3:
        return seleccion_por_ranking(poblacion, fitnesses)
    elif metodo_selec == 4:
        return truncamiento(poblacion, fitnesses)


def aplicar_cruce(padre1, padre2, selec_cruce, prob_cruce=0.8):
    if selec_cruce == 1:
        return cruce_un_punto(padre1, padre2, prob_cruce)
    else:
        return cruce_multipunto(padre1, padre2, prob_cruce)


def aplicar_mutacion(individuo, selec_mutacion, prob_mutacion=0.1):
    if selec_mutacion == 1:
        return mutacion1(individuo, prob_mutacion)
    else:
        return mutacion2(individuo, prob_mutacion)


def aplicar_reemplazo(poblacion, nueva_poblacion, selec_reemplazo):
    if selec_reemplazo == 1:
        return reemplazo_generacional(poblacion, nueva_poblacion)
    else:
        return reemplazo_estacionario(poblacion, nueva_poblacion, penalizacion_alta, penalizacion_media)


def algoritmo_genetico(pop_size, generations,metodo_selec,selec_cruce,selec_mutacion,selec_reemplazo, penalizacion_alta, penalizacion_media):
    poblacion = inicializar_poblacion(pop_size, len(tareas), len(servidores))

    datos_fitness_generacion = []  # Almacenar mejor fitness por generación
    fitness_medio_generacion = []  # Almacenar fitness medio por generación

    mejor_solucion = None
    mejor_fitness = float('-inf')
    mejor_generacion = 0

    for generacion in range(generations):
        fitnesses = [fitness(ind, tareas, servidores, penalizacion_alta, penalizacion_media) for ind in poblacion]
        fitness_medio_generacion.append(sum(fitnesses) / len(fitnesses))  # Fitness promedio

        nueva_poblacion = []
        # Crear nuevos individuos a través de cruce y mutación
        for _ in range(pop_size // 2):
            padre1 = aplicar_seleccion(poblacion, fitnesses, metodo_selec)
            padre2 = aplicar_seleccion(poblacion, fitnesses, metodo_selec)
            descendiente1, descendiente2 = aplicar_cruce(padre1, padre2, selec_cruce)
            nueva_poblacion.extend(
                [aplicar_mutacion(descendiente1, selec_mutacion), aplicar_mutacion(descendiente2, selec_mutacion)])

        # Reemplazar parte de la población
        poblacion = aplicar_reemplazo(poblacion, nueva_poblacion, selec_reemplazo)

        # Evaluar mejor individuo de la generación actual
        mejor_individuo_generacion = max(poblacion, key=lambda ind: fitness(ind, tareas, servidores, penalizacion_alta,
                                                                            penalizacion_media))
        mejor_fitness_generacion = fitness(mejor_individuo_generacion, tareas, servidores, penalizacion_alta,
                                           penalizacion_media)

        datos_fitness_generacion.append(mejor_fitness_generacion)

        #print(f"Generación {generacion + 1}, Mejor fitness: {mejor_fitness_generacion}, Mejor solución: {mejor_individuo_generacion}")

        # Actualizar la mejor solución global si es necesario
        if mejor_fitness_generacion >= mejor_fitness:
            mejor_solucion = mejor_individuo_generacion
            mejor_fitness = mejor_fitness_generacion
            mejor_generacion = generacion + 1

    print(f"\nMejor individuo, Generación {mejor_generacion}: {mejor_solucion}, Fitness: {mejor_fitness}")

    return datos_fitness_generacion, fitness_medio_generacion


# Ejecutamos el main
if __name__ == "__main__":
    # Configuración predeterminada de parámetros
    population_size = 10
    generations = 100
    penalizacion_alta = 10
    penalizacion_media = 5

    # Configuración de selección de métodos
    metodo_selec = 1
    selec_cruce = 1
    selec_mutacion = 1
    selec_reemplazo = 1

    # Ejecutar algoritmo genético
    algoritmo_genetico(population_size, generations,metodo_selec,selec_cruce,selec_mutacion,selec_reemplazo, penalizacion_alta, penalizacion_media)
