# Algoritmo Genético para Asignación de Tareas en Servidores

Este proyecto implementa un **algoritmo genético** para optimizar la asignación de tareas en un grupo de servidores heterogéneos, buscando minimizar el consumo energético y gestionar las prioridades de las tareas.

## Estructura del Proyecto

El proyecto está organizado en tres archivos principales:

- **main.py**: Contiene la función principal `algoritmo_genetico`, que ejecuta el ciclo del algoritmo genético con diferentes métodos de selección, cruce, mutación y reemplazo. Este archivo define la lógica de ejecución, incluidos los operadores evolutivos y el flujo del algoritmo.
  
- **auxiliares.py**: Define las funciones auxiliares que implementan:
  - La inicialización de la población.
  - La función de `fitness` para evaluar individuos, tomando en cuenta consumo energético y penalizaciones por prioridades y sobrecargas.
  - Diferentes métodos de selección, cruce, mutación y reemplazo.
  - También incluye las definiciones de `servidores` y `tareas`, con sus características específicas de CPU, memoria y prioridad.

- **grafica_comparativa.py**: Ejecuta el algoritmo genético con diferentes configuraciones de operadores evolutivos y genera **gráficas comparativas** usando `matplotlib`. Muestra cómo el `fitness` del mejor individuo y el `fitness` medio evolucionan a lo largo de las generaciones para cada configuración.

## Características del Algoritmo

El algoritmo genético permite configurar los siguientes aspectos:

1. **Métodos de Selección**:
   - 1: Ruleta
   - 2: Torneo
   - 3: Selección por Ranking
   - 4: Truncamiento

2. **Métodos de Cruce**:
   - 1: Cruce de un punto
   - 2: Cruce multipunto

3. **Métodos de Mutación**:
   - 1: Reasignación aleatoria
   - 2: Intercambio de genes entre tareas

4. **Métodos de Reemplazo**:
   - 1: Reemplazo Generacional
   - 2: Reemplazo Estacionario (Steady-State)

Estos métodos pueden combinarse para generar distintas configuraciones que se comparan en el archivo `grafica_comparativa.py`.

## Requisitos

Para ejecutar este proyecto, necesitarás instalar `matplotlib` para generar las gráficas comparativas. Puedes instalarlo con:
```bash
pip install matplotlib
