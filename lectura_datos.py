import csv

def leer_servidores(ruta_csv):
    servidores = []
    with open(ruta_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            servidores.append({
                'id': int(row['id']),
                'cpu': float(row['cpu']),
                'memoria': float(row['memoria']),
                'bajo_consumo': float(row['bajo_consumo']),
                'alto_consumo': float(row['alto_consumo'])
            })
    return servidores

def leer_tareas(ruta_csv):
    tareas = []
    with open(ruta_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tareas.append({
                'id': int(row['id']),
                'cpu': float(row['cpu']),
                'memoria': float(row['memoria']),
                'tiempo': float(row['tiempo']),
                'prioridad': int(row['prioridad'])
            })
    return tareas

def leer_configuracion(ruta_csv):
    configuracion = {}
    with open(ruta_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, value = row
            configuracion[key] = float(value) if '.' in value else int(value)
    return configuracion


if __name__ == "__main__":
    ruta_servidores = "ficheros/servidores.csv"
    ruta_tareas = "ficheros/tareas.csv"
    ruta_configuracion = "ficheros/config.csv"

    servidores = leer_servidores(ruta_servidores)
    #tareas = leer_tareas(ruta_tareas)
    configuracion = leer_configuracion(ruta_configuracion)

    print("Servidores:", servidores)
    #print("Tareas:", tareas)
    print("Configuración:", configuracion)