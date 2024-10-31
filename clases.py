# clases.py

class Detector:
    """
    Clase encargada de detectar mutantes en una matriz de ADN.
    
    Atributos:
    - adn: La secuencia de ADN representada como una lista de cadenas de 6 caracteres.
    - dimension: Tamaño de la matriz (6x6).
    """
    def __init__(self, adn: list[str]):
        # El constructor recibe una lista de strings que representa la matriz de ADN.
        self.adn = adn
        self.dimension = 6  # La matriz es de tamaño fijo 6x6

    def detectar_mutantes(self) -> bool:
        """
        Detecta si hay mutantes en el ADN en direcciones horizontal, vertical o diagonal.

        Returns:
        - True si se detecta un mutante, False en caso contrario.
        """
        # Llama a los tres métodos que revisan las posibles mutaciones en las tres direcciones.
        return self.detectar_horizontal() or self.detectar_vertical() or self.detectar_diagonal()

    def detectar_horizontal(self) -> bool:
        """Detecta mutantes en las filas de la matriz (horizontal)."""
        # Recorre cada fila y verifica si hay una secuencia repetida en ella.
        for fila in self.adn:
            if self.hay_secuencia_repetida(fila):
                return True
        return False

    def detectar_vertical(self) -> bool:
        """Detecta mutantes en las columnas de la matriz (vertical)."""
        # Para cada columna, crea una cadena con los caracteres verticales y verifica si hay una secuencia repetida.
        for col in range(self.dimension):
            columna = ''.join([self.adn[fila][col] for fila in range(self.dimension)])
            if self.hay_secuencia_repetida(columna):
                return True
        return False

    def detectar_diagonal(self) -> bool:
        """Detecta mutantes en las diagonales de la matriz."""
        # Obtiene las diagonales de la matriz y verifica si alguna tiene una secuencia repetida.
        diagonales = self.obtener_diagonales()
        for diag in diagonales:
            if self.hay_secuencia_repetida(diag):
                return True
        return False

    def obtener_diagonales(self) -> list[str]:
        """
        Obtiene todas las diagonales posibles de la matriz.

        Returns:
        - Lista con las diagonales principales y secundarias.
        """
        diagonales = []
        # Diagonales de izquierda a derecha (↘)
        for i in range(self.dimension - 3):
            # Diagonales que comienzan desde la primera fila
            diagonales.append(''.join([self.adn[i + k][k] for k in range(self.dimension - i)]))
            # Diagonales que comienzan desde la primera columna
            diagonales.append(''.join([self.adn[k][i + k] for k in range(self.dimension - i)]))
        # Diagonales de derecha a izquierda (↙)
        for i in range(3, self.dimension):
            # Diagonales que empiezan desde la última fila
            diagonales.append(''.join([self.adn[i - k][k] for k in range(i + 1)]))
            # Diagonales que empiezan desde la última columna
            diagonales.append(''.join([self.adn[self.dimension - 1 - k][i - k] for k in range(i + 1)]))
        return diagonales

    def hay_secuencia_repetida(self, secuencia: str) -> bool:
        """
        Verifica si hay 4 letras consecutivas repetidas en una secuencia.

        Args:
        - secuencia: Cadena que representa una fila, columna o diagonal.

        Returns:
        - True si hay una secuencia repetida, False en caso contrario.
        """
        # Recorre la secuencia y verifica si 4 caracteres consecutivos son iguales.
        for i in range(len(secuencia) - 3):
            if secuencia[i:i + 4] == secuencia[i] * 4:
                return True
        return False


class Mutador:
    """
    Superclase que representa un mutador genérico.

    Atributos:
    - base_nitrogenada: La base nitrogenada que se mutará.
    """
    def __init__(self, base_nitrogenada: str):
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self):
        """Método abstracto que será sobrescrito por las subclases."""
        pass


class Radiacion(Mutador):
    """
    Clase que crea mutantes horizontales y verticales.

    Hereda de Mutador.
    """
    def __init__(self, base_nitrogenada: str):
        # Inicializa la clase padre Mutador
        super().__init__(base_nitrogenada)

    def crear_mutante(self, adn: list[str], posicion_inicial: tuple[int, int], orientacion_de_la_mutacion: str) -> list[str]:
        """
        Crea un mutante en la matriz de ADN.

        Args:
        - adn: La matriz de ADN original.
        - posicion_inicial: Tupla (fila, columna) que indica la posición inicial de la mutación.
        - orientacion_de_la_mutacion: 'H' para horizontal o 'V' para vertical.

        Returns:
        - Matriz de ADN mutada.
        """
        try:
            if orientacion_de_la_mutacion == 'H':
                fila, col = posicion_inicial
                # Mutar horizontalmente: reemplaza 4 bases nitrogenadas a partir de la columna dada
                adn[fila] = adn[fila][:col] + self.base_nitrogenada * 4 + adn[fila][col + 4:]
            elif orientacion_de_la_mutacion == 'V':
                fila, col = posicion_inicial
                # Mutar verticalmente: reemplaza una base en cada fila empezando en la posición dada
                for i in range(4):
                    adn[fila + i] = adn[fila + i][:col] + self.base_nitrogenada + adn[fila + i][col + 1:]
            return adn
        except IndexError:
            # Manejo de errores si la posición está fuera de los límites de la matriz
            print("Error: Posición fuera de rango.")
            return adn


class Virus(Mutador):
    """
    Clase que crea mutantes diagonales.

    Hereda de Mutador.
    """
    def __init__(self, base_nitrogenada: str):
        # Inicializa la clase padre Mutador
        super().__init__(base_nitrogenada)

    def crear_mutante(self, adn: list[str], posicion_inicial: tuple[int, int]) -> list[str]:
        """
        Crea un mutante diagonal en la matriz de ADN.

        Args:
        - adn: La matriz de ADN original.
        - posicion_inicial: Tupla (fila, columna) que indica la posición inicial de la mutación.

        Returns:
        - Matriz de ADN mutada.
        """
        try:
            fila, col = posicion_inicial
            # Mutar diagonalmente: reemplaza una base en diagonal, de arriba a abajo y de izquierda a derecha
            for i in range(4):
                adn[fila + i] = adn[fila + i][:col + i] + self.base_nitrogenada + adn[fila + i][col + i + 1:]
            return adn
        except IndexError:
            # Manejo de errores si la posición está fuera de los límites de la matriz
            print("Error: Posición fuera de rango.")
            return adn


class Sanador:
    """
    Clase encargada de sanar mutantes, generando una nueva secuencia de ADN si es necesario.
    """
    def __init__(self, detector: Detector): 
        # El sanador recibe un detector de mutantes para verificar si hay mutaciones en el ADN.
        self.detector = detector

    def sanar_mutantes(self, adn: list[str]) -> list[str]:
        """
        Sana mutantes generando una nueva secuencia de ADN si se detectan mutaciones.

        Args:
        - adn: La matriz de ADN original.

        Returns:
        - Matriz de ADN nueva si había mutaciones, o la misma matriz si no había mutaciones.
        """
        # Si se detectan mutantes, genera una nueva secuencia de ADN.
        if self.detector.detectar_mutantes():
            print("Mutaciones detectadas. Generando ADN sano...")
            return self.generar_adn_sano()
        # Si no hay mutantes, regresa la misma matriz de ADN.
        print("No se detectaron mutaciones.")
        return adn

    def generar_adn_sano(self) -> list[str]:
        """
        Genera una nueva matriz de ADN aleatoria sin mutaciones.

        Returns:
        - Una nueva matriz de ADN generada aleatoriamente.
        """
        import random
        # Genera una nueva matriz 6x6 de bases nitrogenadas aleatorias.
        bases = ['A', 'T', 'C', 'G']
        nuevo_adn = [''.join(random.choices(bases, k=6)) for _ in range(6)]
        return nuevo_adn
