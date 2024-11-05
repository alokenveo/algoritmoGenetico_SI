import matplotlib.pyplot as plt
from main import algoritmo_genetico

# Configuraciones específicas a probar
configuraciones = [
    (1, 1, 1, 1),
    (2, 2, 2, 2),
    (3, 1, 2, 1),
    (4, 2, 1, 2)
]

# Parámetros
pop_size = 10
generations = 100
penalizacion_alta = 10
penalizacion_media = 5

# Almacenar resultados
resultados_mejor = []
resultados_medio = []

# Probar configuraciones específicas
for metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo in configuraciones:
    # Ejecutar algoritmo genético
    datos_fitness_generacion, fitness_medio_generacion = algoritmo_genetico(
        pop_size, generations, metodo_selec, selec_cruce, selec_mutacion, selec_reemplazo, penalizacion_alta, penalizacion_media
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
