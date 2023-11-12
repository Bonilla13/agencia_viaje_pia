import pandas as pd
import random
from faker import Faker
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Lugar de guardado de los archivos CSV (ajusta la ruta según sea necesario para tu entorno)
aeropuertos_file = 'Aeropuertos.csv'
aviones_file = 'Aviones.csv'
itinerario_vuelos_file = 'ItinerarioVuelos.csv'
destinos_file = 'Destinos.csv'
reservaciones_file = 'Reservaciones.csv'

def validar_cadena(cadena):
    return cadena.isalpha() and len(cadena) > 0
def validar_entero_positivo(valor):
    try:
        entero = int(valor)
        return entero > 0
    except ValueError:
        return False
def validar_rango_pasajeros(min_pasajeros, max_pasajeros):
    return min_pasajeros <= max_pasajeros    

def buscar_por_pais(ciudades, pais):
    destinos = []
    for ciudad in ciudades:
        if ciudad['pais'] == pais:
            destinos.append(ciudad)
    return destinos

def cargar_aeropuertos():
    try:
        with open("Aeropuertos.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            aeropuertos = [dict(zip(["pais", "ciudad", "aeropuerto", "terminales"], row)) for row in reader]
        return aeropuertos
    except FileNotFoundError:
        return []
    
def cargar_destinos():
    try:
        with open("Destinos.csv", mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)  # Saltar la primera fila (encabezados)
            destinos = [dict(zip(["punto_partida", "punto_llegada"], row)) for row in reader]
        return destinos
    except FileNotFoundError:
        return []

def validar_cadena(cadena):
    return cadena.isalpha() and len(cadena) > 0

def validar_entero_positivo(valor):
    try:
        entero = int(valor)
        return entero > 0
    except ValueError:
        return False
    
def validar_hora(hora):
    try:
        # Intenta convertir la cadena a un objeto de hora
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
    
def validar_horarios(horarios):
    # Verifica si los horarios están separados por '|'
    horarios_lista = horarios.split('|')

    # Valida cada horario individualmente
    for horario in horarios_lista:
        try:
            # Intenta convertir la cadena a un objeto de tiempo
            datetime.strptime(horario, "%H:%M")
        except ValueError:
            return False

    return True

def validar_tiempo_vuelo(tiempo_vuelo):
    try:
        # Intenta convertir la cadena a un objeto timedelta
        tiempo_vuelo_timedelta = datetime.strptime(tiempo_vuelo, "%Hh").time()
        return True
    except ValueError:
        return False

def validar_si_no(valor):
    # Valida que el valor sea 'Sí' o 'No' (mayúsculas o minúsculas)
    return valor.lower() in ['sí', 'no']

def validar_fecha(fecha):
    try:
        # Intenta convertir la cadena a un objeto de fecha
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora):
    try:
        # Intenta convertir la cadena a un objeto de tiempo
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False
    
# Function to add a new airport to Aeropuertos.csv
def add_new_airport(pais, ciudad, nombre_aeropuerto, terminales):
    with open(aeropuertos_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([pais, ciudad, nombre_aeropuerto, terminales])
    return "Nuevo aeropuerto añadido con éxito."

# Function to add a new airplane to Aviones.csv
def add_new_airplane(identificador, min_pasajeros, max_pasajeros, horarios, vuelos_disponibles):
    with open(aviones_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([identificador, min_pasajeros, max_pasajeros, horarios, vuelos_disponibles])
    return "Nuevo avión añadido con éxito."

# Function to add a new flight itinerary to ItinerarioVuelos.csv
def add_new_flight_itinerary(codigo_vuelo, identificador_avion, punto_partida, destino_final, hora_abordaje, hora_despegue, hora_arribo, costo_vuelo, estado_vuelo):
    with open(itinerario_vuelos_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([codigo_vuelo, identificador_avion, punto_partida, destino_final, hora_abordaje, hora_despegue, hora_arribo, costo_vuelo, estado_vuelo])
    return "Nuevo itinerario de vuelo añadido con éxito."

# Function to add a new destination to Destinos.csv
def add_new_destination(punto_partida, destino_final, tiempo_vuelo_estimado, vuelo_directo):
    with open(destinos_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([punto_partida, destino_final, tiempo_vuelo_estimado, vuelo_directo])
    return "Nuevo destino añadido con éxito."

# Function to add a new reservation to Reservaciones.csv
def add_new_reservation(codigo_reservacion, codigo_vuelo, fecha_reservacion, hora_reservacion, nombre_pasajero, numero_pasajeros, estado_reservacion):
    with open(reservaciones_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([codigo_reservacion, codigo_vuelo, fecha_reservacion, hora_reservacion, nombre_pasajero, numero_pasajeros, estado_reservacion])
    return "Nueva reservación añadida con éxito."

# Función para gestionar el registro de aeropuertos y aviones
def Registro_Aeropuerto():
    while True:
        print("\nMenú de Registro de Aeropuerto:")
        print("1. Agregar nuevo aeropuerto")
        print("2. Agregar nuevo avión")
        print("3. Agregar nuevo itinerario de vuelo")
        print("4. Agregar nuevo destino")
        print("5. Agregar nueva reservación")
        print("6. Salir")
        
        choice = input("Elige una opción: ")

        if choice == '1':
            pais = input("País: ")
            ciudad = input("Ciudad: ")
            nombre_aeropuerto = input("Nombre del Aeropuerto: ")
            terminales = input("Terminales: ")
            if not validar_cadena(pais) or not validar_cadena(ciudad) or not validar_cadena(nombre_aeropuerto) or not validar_entero_positivo(terminales):
                print("Error: Datos de entrada no válidos. Por favor, ingrese información válida.")
            else:
                print(add_new_airport(pais, ciudad, nombre_aeropuerto, terminales))

        elif choice == '2':
            identificador = input("Identificador del Avión: ")
            min_pasajeros = input("Mínimo de Pasajeros: ")
            max_pasajeros = input("Máximo de Pasajeros: ")
            horarios = input("Horarios (separados por '|'): ")
            vuelos_disponibles = input("Vuelos Disponibles: ")
            if (
                not validar_cadena(identificador)
                or not validar_entero_positivo(min_pasajeros)
                or not validar_entero_positivo(max_pasajeros)
                or not validar_horarios(horarios)
                or not validar_entero_positivo(vuelos_disponibles)
            ):
                print("Error: Datos de entrada no válidos. Por favor, ingrese información válida.")
            else:
                print(add_new_airplane(identificador, min_pasajeros, max_pasajeros, horarios, vuelos_disponibles))
                  
        elif choice == '3':
            codigo_vuelo = input("Código de Vuelo: ")
            identificador_avion = input("Identificador del Avión: ")
            punto_partida = input("Punto de Partida: ")
            destino_final = input("Destino Final: ")
            hora_abordaje = input("Hora de Abordaje: ")
            hora_despegue = input("Hora de Despegue: ")
            hora_arribo = input("Hora de Arribo: ")
            costo_vuelo = input("Costo de Vuelo: ")
            estado_vuelo = input("Estado de Vuelo: ")
            if (
                not validar_cadena(codigo_vuelo)
                or not validar_cadena(identificador_avion)
                or not validar_cadena(punto_partida)
                or not validar_cadena(destino_final)
                or not validar_hora(hora_abordaje)
                or not validar_hora(hora_despegue)
                or not validar_hora(hora_arribo)
                or not validar_entero_positivo(costo_vuelo)
                or not validar_cadena(estado_vuelo)
            ):
                print("Error: Datos de entrada no válidos. Por favor, ingrese información válida.")
            else:
                print(
                    add_new_flight_itinerary(
                        codigo_vuelo,
                        identificador_avion,
                        punto_partida,
                        destino_final,
                        hora_abordaje,
                        hora_despegue,
                        hora_arribo,
                        costo_vuelo,
                        estado_vuelo,
                    )
                )
        elif choice == '4':
            punto_partida = input("Punto de Partida: ")
            destino_final = input("Destino Final: ")
            tiempo_vuelo_estimado = input("Tiempo de Vuelo Estimado: ")
            vuelo_directo = input("¿Vuelo Directo? (Sí/No): ")
            if (
            not validar_cadena(punto_partida)
            or not validar_cadena(destino_final)
            or not validar_tiempo_vuelo(tiempo_vuelo_estimado)
            or not validar_si_no(vuelo_directo)
            ):
                print("Error: Datos de entrada no válidos. Por favor, ingrese información válida.")
            else:
                print(add_new_destination(punto_partida, destino_final, tiempo_vuelo_estimado, vuelo_directo))
    
        elif choice == '5':
            codigo_reservacion = input("Código de Reservación: ")
            codigo_vuelo = input("Código de Vuelo: ")
            fecha_reservacion = input("Fecha de Reservación (YYYY-MM-DD): ")
            hora_reservacion = input("Hora de Reservación (HH:MM): ")
            nombre_pasajero = input("Nombre del Pasajero: ")
            numero_pasajeros = input("Número de Pasajeros: ")
            estado_reservacion = input("Estado de la Reservación: ")
            if (
                not validar_cadena(codigo_reservacion)
                or not validar_cadena(codigo_vuelo)
                or not validar_fecha(fecha_reservacion)
                or not validar_hora(hora_reservacion)
                or not validar_cadena(nombre_pasajero)
                or not validar_entero_positivo(numero_pasajeros)
                or not validar_cadena(estado_reservacion)
            ):
                print("Error: Datos de entrada no válidos. Por favor, ingrese información válida.")
            else:
                print(add_new_reservation(codigo_reservacion, codigo_vuelo, fecha_reservacion, hora_reservacion, nombre_pasajero, numero_pasajeros, estado_reservacion))

        elif choice == '6':
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida del menú.")

# Función para buscar destinos por país
def buscar_destinos_por_pais():
    ciudades = cargar_aeropuertos()
    
    if not ciudades:
        print("No hay aeropuertos registrados.")
        return
    
    while True:
        pais_buscar = input("Ingrese el país para buscar destinos: ")
        if validar_cadena(pais_buscar):
            break
        else:
            print("Nombre no válido. Por favor, ingrese solo letras y no deje el campo vacío.")

     # Verificar si el país ingresado existe en los aeropuertos registrados
    if any(ciudad['pais'] == pais_buscar for ciudad in ciudades):
        destinos = buscar_por_pais(ciudades, pais_buscar)
        if destinos:
            print(f"Destinos en {pais_buscar}:")
            for destino in destinos:
                print(f"Ciudad: {destino['ciudad']}, Aeropuerto: {destino['aeropuerto']}, Terminales: {destino['terminales']}")
        else:
            print(f"No se encontraron destinos en {pais_buscar}.")
    else:
        print(f"No hay aeropuertos registrados en {pais_buscar}.")

#Función para registrar destinos
def registrar_destino():
    aeropuertos = cargar_aeropuertos()
    
    if not aeropuertos:
        print("No hay aeropuertos registrados. Registre al menos un aeropuerto antes de agregar destinos.")
        return

    print("Aeropuertos disponibles:")
    for i, aeropuerto in enumerate(aeropuertos, start=1):
        print(f"{i}. {aeropuerto['ciudad']}, {aeropuerto['pais']}")

    try:
        punto_partida_index = int(input("Seleccione el punto de partida (número): ")) - 1
        punto_llegada_index = int(input("Seleccione el punto de llegada (número): ")) - 1

        punto_partida = aeropuertos[punto_partida_index]
        punto_llegada = aeropuertos[punto_llegada_index]

        with open("Destinos.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([f"{punto_partida['ciudad']}, {punto_partida['pais']}", f"{punto_llegada['ciudad']}, {punto_llegada['pais']}"])

        print("Destino registrado con éxito!")
    except (ValueError, IndexError):
        print("Selección no válida. Asegúrese de ingresar números válidos para los puntos de partida y llegada.")

def verificar_vuelo_directo(destinos, punto_partida, punto_llegada):
    for destino in destinos:
        if destino['punto_partida'] == f"{punto_partida['ciudad']}, {punto_partida['pais']}" and destino['punto_llegada'] == f"{punto_llegada['ciudad']}, {punto_llegada['pais']}":
            return True
    return False

def buscar_ruta():
    aeropuertos = cargar_aeropuertos()
    destinos = cargar_destinos()

    if not aeropuertos or not destinos:
        print("No hay información suficiente para buscar rutas. Registre al menos un aeropuerto y un destino.")
        return

    print("Aeropuertos disponibles:")
    for i, aeropuerto in enumerate(aeropuertos, start=1):
        print(f"{i}. {aeropuerto['ciudad']}, {aeropuerto['pais']}")

    try:
        punto_partida_index = int(input("Seleccione el punto de partida (número): ")) - 1
        punto_llegada_index = int(input("Seleccione el punto de llegada (número): ")) - 1

        punto_partida = aeropuertos[punto_partida_index]
        punto_llegada = aeropuertos[punto_llegada_index]

        if verificar_vuelo_directo(destinos, punto_partida, punto_llegada):
            print("¡Hay vuelo directo!")
        else:
            print("No hay vuelo directo. Se requiere hacer escalas.")
    except (ValueError, IndexError):
        print("Selección no válida. Asegúrese de ingresar números válidos para los puntos de partida y llegada.")

# ------------------ synthetic_data.py ------------------
def synthetic_data():
    import random

    fake = Faker()
    
    # Datos sintéticos para Aeropuertos.csv
    aeropuertos = [
        ('México', 'Ciudad de México', 'Aeropuerto Internacional Benito Juárez', 'T1,T2'),
        ('Estados Unidos', 'Nueva York', 'Aeropuerto Internacional John F. Kennedy', 'T1,T2,T3,T4'),
        ('España', 'Madrid', 'Aeropuerto Adolfo Suárez Madrid-Barajas', 'T1,T2,T3,T4')
    ]
    
    # Datos sintéticos para Aviones.csv
    aviones = [
        (f'AM{str(random.randint(100, 999))}', random.randint(100, 180), random.randint(180, 300),
         '|'.join([f"{fake.time()}" for _ in range(4)]), f"{fake.random_int(min=1000, max=9999)}")
        for _ in range(5)
    ]
    
    # Datos sintéticos para ItinerarioVuelos.csv
    itinerarios = [
        (f'AMX{fake.random_int(min=700, max=999)}', avion[0], fake.city(), fake.city(),
         fake.time(), fake.time(), fake.time(), fake.random_int(min=100, max=1000), 'En Horario')
        for avion in aviones
        for _ in range(3)
    ]
    
    # Datos sintéticos para Destinos.csv
    destinos = [
        (fake.city(), fake.city(), f"{random.randint(1,12)}h", 'Sí')
        for _ in range(10)
    ]
    
    # Datos sintéticos para Reservaciones.csv
    reservaciones = [
        (f'RES{fake.random_int(min=100, max=999)}', itinerario[0], fake.date(), fake.time(),
         fake.name(), random.randint(1, 5), 'Confirmada')
        for itinerario in itinerarios
        for _ in range(2)
    ]
    
    # Funciones para guardar datos en archivos CSV
    def save_to_csv(filename, headers, data):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)
    
    # Lugar de guardado de los archivos CSV (ajusta la ruta según sea necesario para tu entorno)
    aeropuertos_file = 'Aeropuertos.csv'
    aviones_file = 'Aviones.csv'
    itinerario_vuelos_file = 'ItinerarioVuelos.csv'
    destinos_file = 'Destinos.csv'
    reservaciones_file = 'Reservaciones.csv'
    
    # Guardar datos en los CSV correspondientes
    save_to_csv(aeropuertos_file, ['País', 'Ciudad', 'Nombre del Aeropuerto', 'Terminales'], aeropuertos)
    save_to_csv(aviones_file, ['Identificador', 'Min Pasajeros', 'Max Pasajeros', 'Horarios', 'Vuelos Disponibles'], aviones)
    save_to_csv(itinerario_vuelos_file, ['Código Vuelo', 'Identificador Avión', 'Punto de Partida', 'Destino Final', 'Hora Abordaje', 'Hora Despegue', 'Hora Arribo', 'Costo Vuelo', 'Estado Vuelo'], itinerarios)
    save_to_csv(destinos_file, ['Punto de Partida', 'Destino Final', 'Tiempo Vuelo Estimado', 'Vuelo Directo'], destinos)
    save_to_csv(reservaciones_file, ['Código Reservación', 'Código Vuelo', 'Fecha Reservación', 'Hora Reservación', 'Nombre Pasajero', 'Número Pasajeros', 'Estado Reservación'], reservaciones)

 # Function to create a CSV file with headers if it doesn't exist

def create_csv_if_not_exists(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
    
# Create the CSV files with their respective headers
def create_files():
    # Lugar de guardado de los archivos CSV (ajusta la ruta según sea necesario para tu entorno)
    aeropuertos_file = 'Aeropuertos.csv'
    aviones_file = 'Aviones.csv'
    itinerario_vuelos_file = 'ItinerarioVuelos.csv'
    destinos_file = 'Destinos.csv'
    reservaciones_file = 'Reservaciones.csv'
    create_csv_if_not_exists(aeropuertos_file, ['País', 'Ciudad', 'Nombre del Aeropuerto', 'Terminales'])
    create_csv_if_not_exists(aviones_file, ['Identificador del Avión', 'Min Pasajeros', 'Max Pasajeros', 'Horarios', 'Vuelos Disponibles'])
    create_csv_if_not_exists(itinerario_vuelos_file, ['Código de Vuelo', 'Identificador del Avión', 'Punto de Partida', 'Destino Final', 'Hora de Abordaje', 'Hora de Despegue', 'Hora de Arribo', 'Costo de Vuelo', 'Estado del Vuelo'])
    create_csv_if_not_exists(destinos_file, ['Punto de Partida', 'Destino Final', 'Distancia o Tiempo de Vuelo Estimado', 'Vuelo Directo'])
    create_csv_if_not_exists(reservaciones_file, ['Código de Reservación', 'Código de Vuelo', 'Fecha de Reservación', 'Hora de Reservación', 'Nombre del Pasajero', 'Número de Pasajeros', 'Estado de la Reservación'])      
    

# Función principal
def one():
    while True:
        print("\nMenu Principal:")
        print("1. Registro de Aeropuerto")
        print("2. Registro de Destino")
        print("3. Verificar vuelo directo")
        print("4. Generar datos sintéticos")
        print("5. Crear CSV si no existe")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            Registro_Aeropuerto()
        elif opcion == "2":
            registrar_destino()
        elif opcion == "3":
            buscar_ruta()
        elif opcion == "4":
            synthetic_data()
        elif opcion == "5":
            create_files()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

one()