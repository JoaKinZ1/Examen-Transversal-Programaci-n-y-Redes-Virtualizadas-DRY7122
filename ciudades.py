import requests
import urllib.parse

def obtener_datos_viaje(origen, destino, transporte, api_key):
    main_api = "http://www.mapquestapi.com/directions/v2/route?"
    url = main_api + urllib.parse.urlencode({"key": api_key, "from": origen, "to": destino, "routeType": transporte})
    response = requests.get(url).json()

    if response["info"]["statuscode"] == 0:
        return response
    else:
        return None

def mostrar_detalles_viaje(datos):
    if datos is None:
        print("No se pudo obtener la información del viaje.")
        return

    print(f"Distancia: {datos['route']['distance']:.2f} millas ({datos['route']['distance'] * 1.60934:.2f} km)")
    print(f"Duración del viaje: {datos['route']['formattedTime']}")
    print("Narrativa del viaje:")
    for step in datos['route']['legs'][0]['maneuvers']:
        print(step['narrative'])
    print(f"Combustible requerido: {datos['route']['fuelUsed']:.2f} litros")

def main():
    api_key = "OEJwHauy9q8MWbW1XaUkFdC8tclJtO0l"

    while True:
        origen = input("Ingrese la Ciudad de Origen: ")
        if origen.lower() == 's':
            break

        destino = input("Ingrese la Ciudad de Destino: ")
        if destino.lower() == 's':
            break

        print("Elija el tipo de medio de transporte:")
        print("1. Coche")
        print("2. Peatón")
        print("3. Bicicleta")

        transporte_opcion = input("Ingrese el número de la opción: ")

        if transporte_opcion == '1':
            transporte = "fastest"
        elif transporte_opcion == '2':
            transporte = "pedestrian"
        elif transporte_opcion == '3':
            transporte = "bicycle"
        else:
            print("Opción no válida. Intente nuevamente.")
            continue

        datos_viaje = obtener_datos_viaje(origen, destino, transporte, api_key)
        mostrar_detalles_viaje(datos_viaje)

if __name__ == "__main__":
    main()