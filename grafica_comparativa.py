import matplotlib.pyplot as plt
from main import algoritmo_genetico

# Configuraciones a probar
metodos_seleccion = [1, 2, 3, 4]  # Métodos de selección
metodos_cruce = [1, 2]  # Métodos de cruce
metodos_mutacion = [1, 2]  # Métodos de mutación
metodos_reemplazo = [1, 2]  # Métodos de reemplazo

# Parámetros
pop_size = 10
generations = 100
penalizacion_alta = 10
penalizacion_media = 5

# Almacenar resultados
resultados_mejor = []
resultados_medio = []

# Probar diferentes configuraciones
for metodo_selec in metodos_seleccion:
    for selec_cruce in metodos_cruce:
        for selec_mutacion in metodos_mutacion:
            for selec_reemplazo in metodos_reemplazo:
                # Ejecutar algoritmo genético
                datos_fitness_generacion, fitness_medio_generacion = algoritmo_genetico(
                    pop_size, generations,metodo_selec,selec_cruce,selec_mutacion,selec_reemplazo, penalizacion_alta, penalizacion_media
                )

                # Almacenar los mejores fitness y medios
                resultados_mejor.append((metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo, datos_fitness_generacion))
                resultados_medio.append((metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo, fitness_medio_generacion))

# Graficar resultados para el mejor individuo
for (metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo, datos) in resultados_mejor:
    plt.plot(datos, label=f'Selección: {metodo_selec}, Cruce: {selec_cruce}, Mutación: {selec_mutacion}, Reemplazo: {selec_reemplazo}')

plt.title('Mejor Individuo por Configuración')
plt.xlabel('Generaciones')
plt.ylabel('Fitness del Mejor Individuo')
plt.legend()
plt.show()

# Graficar resultados para el fitness medio
for (metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo, datos) in resultados_medio:
    plt.plot(datos, label=f'Selección: {metodo_selec}, Cruce: {selec_cruce}, Mutación: {selec_mutacion}, Reemplazo: {selec_reemplazo}')

plt.title('Fitness Medio por Configuración')
plt.xlabel('Generaciones')
plt.ylabel('Fitness Medio')
plt.legend()
plt.show()
