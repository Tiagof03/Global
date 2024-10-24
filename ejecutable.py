# ejecutable.py

# Importamos las clases desde el archivo clases.py
from clases import Detector, Radiacion, Virus, Sanador

def main():
    # ADN de ejemplo: una matriz de 6x6 representada como una lista de strings
    adn = [
        "AGATCA", 
        "GATTCA", 
        "CAACAT", 
        "GAGCTA", 
        "ATTGCG", 
        "CTGTTC"
    ]
    
    # Creamos una instancia de la clase Detector, pasándole la matriz de ADN
    detector = Detector(adn)

    while True:
        # Mostramos las opciones al usuario
        print("Seleccione una opción:")
        print("1: Detectar mutaciones")
        print("2: Mutar ADN")
        print("3: Sanar ADN")
        print("4: Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            # Opción 1: Detectar mutaciones
            if detector.detectar_mutantes():
                print("El ADN contiene mutaciones.")
            else:
                print("El ADN no contiene mutaciones.")
        
        elif opcion == '2':
            # Opción 2: Mutar ADN (Radiación o Virus)
            tipo_mutacion = input("Ingrese el tipo de mutación (R: Radiación, V: Virus): ").upper()
            base_nitrogenada = input("Ingrese la base nitrogenada (A, T, C, G): ").upper()
            
            if tipo_mutacion == 'R':
                # Mutación por Radiación: solicitar posición y orientación
                fila = int(input("Ingrese la fila inicial: "))
                col = int(input("Ingrese la columna inicial: "))
                orientacion = input("Ingrese la orientación (H: Horizontal, V: Vertical): ").upper()
                mutador = Radiacion(base_nitrogenada)
                adn = mutador.crear_mutante(adn, (fila, col), orientacion)
            elif tipo_mutacion == 'V':
                # Mutación por Virus: solicitar posición inicial
                fila = int(input("Ingrese la fila inicial: "))
                col = int(input("Ingrese la columna inicial: "))
                mutador = Virus(base_nitrogenada)
                adn = mutador.crear_mutante(adn, (fila, col))
            
            # Mostramos el ADN después de la mutación
            print("ADN después de la mutación:", adn)

        elif opcion == '3':
            # Opción 3: Sanar ADN
            sanador = Sanador(detector)
            adn = sanador.sanar_mutantes(adn)
            # Mostramos el ADN después de sanarlo
            print("ADN después de sanación:", adn)

        elif opcion == '4':
            # Opción 4: Salir del programa
            print("Saliendo del programa.")
            break

        else:
            # Si elige una opción inválida, mostramos un mensaje
            print("Opción inválida. Intente nuevamente.")

# Ejecutamos el main solo si este archivo es ejecutado directamente
if __name__ == "__main__":
    main()
