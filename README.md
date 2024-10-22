# Asignación de Tareas en Servidores con Algoritmo Genético

Este proyecto implementa un algoritmo genético para asignar tareas a una lista de servidores, optimizando el uso de recursos y minimizando el consumo energético.

## Descripción

El sistema asigna tareas a los servidores disponibles, basándose en las capacidades de CPU y memoria de los servidores. Además, calcula penalizaciones según las prioridades de las tareas y las sobrecargas de los servidores. El objetivo es minimizar el consumo energético mientras se respetan las capacidades de los servidores y las prioridades de las tareas.

## Estructura del Proyecto

- **servidores**: Lista de servidores con información de CPU, memoria, consumo bajo y alto.
- **tareas**: Lista de tareas con requerimientos de CPU, memoria, duración y prioridad.
- **algoritmo_genetico.py**: Implementa el algoritmo genético con funciones de selección por ruleta, cruce, mutación y evaluación de fitness.

## Funciones Clave

- `inicializar_poblacion(pop_size, num_tareas, num_servers)`: Crea una población inicial aleatoria de asignaciones.
- `fitness(individuo, tareas, servidores)`: Evalúa el fitness de cada asignación de servidores según el consumo energético y las penalizaciones.
- `ruleta(poblacion, fitnesses)`: Selecciona un individuo de la población basado en su fitness.
- `cruce(padre1, padre2)`: Realiza un cruce entre dos padres para generar nuevos descendientes.
- `mutacion(individuo)`: Aplica mutación a un individuo con una tasa de mutación dada.
- `reemplazo(poblacion, nueva_poblacion)`: Reemplaza un porcentaje de la población con nuevos individuos.

## Cómo Usar

1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener Python 3 instalado.
3. Ejecuta el script principal:

```bash
python main.py
