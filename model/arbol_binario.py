from collections import deque
from model.nodo import Nodo


class ArbolBinario:

    def __init__(self):
        self.raiz = None

    # ==================================================
    # INSERTAR
    # ==================================================

    def insertar(self, nombre, es_carpeta):
        """
        Inserta un nuevo nodo respetando las reglas del BST.

        Retorna:
            (True, comparaciones)  -> inserción correcta
            (False, comparaciones) -> nombre duplicado o inválido
        """

        comparaciones = 0

        if nombre is None or nombre.strip() == "":
            return False, comparaciones

        nombre = nombre.strip()

        nuevo_nodo = Nodo(nombre, es_carpeta)

        # Si el árbol está vacío, el nuevo nodo será la raíz.
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return True, comparaciones

        actual = self.raiz

        while True:

            comparaciones += 1

            nombre_nuevo = nombre.casefold()
            nombre_actual = actual.nombre.casefold()

            # No permitir duplicados
            if nombre_nuevo == nombre_actual:
                return False, comparaciones

            # Menor -> izquierda
            if nombre_nuevo < nombre_actual:

                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    return True, comparaciones

                actual = actual.izquierdo

            # Mayor -> derecha
            else:

                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    return True, comparaciones

                actual = actual.derecho

    # ==================================================
    # BUSCAR
    # ==================================================

    def buscar(self, nombre):
        """
        Busca un nodo por su nombre.

        Retorna:
            (nodo, comparaciones)

        Si no existe:
            (None, comparaciones)
        """

        comparaciones = 0

        if nombre is None or nombre.strip() == "":
            return None, comparaciones

        nombre = nombre.strip()

        actual = self.raiz

        while actual is not None:

            comparaciones += 1

            nombre_buscar = nombre.casefold()
            nombre_actual = actual.nombre.casefold()

            if nombre_buscar == nombre_actual:
                return actual, comparaciones

            if nombre_buscar < nombre_actual:
                actual = actual.izquierdo

            else:
                actual = actual.derecho

        return None, comparaciones

    # ==================================================
    # ACTUALIZAR
    # ==================================================

    def actualizar(self, nombre_antiguo, nombre_nuevo):
        """
        Actualiza el nombre de un nodo mediante:
        Eliminar + Insertar.
        """

        nodo_antiguo, _ = self.buscar(nombre_antiguo)

        if nodo_antiguo is None:
            return False, "El nodo que desea actualizar no existe."

        nodo_existente, _ = self.buscar(nombre_nuevo)

        if nodo_existente is not None:
            return False, "El nuevo nombre ya existe."

        if nombre_nuevo is None or nombre_nuevo.strip() == "":
            return False, "El nuevo nombre no puede estar vacío."

        # Guardamos el tipo antes de eliminar.
        es_carpeta = nodo_antiguo.es_carpeta

        eliminado, _ = self.eliminar(nombre_antiguo)

        if not eliminado:
            return False, "No fue posible eliminar el nodo anterior."

        insertado, _ = self.insertar(
            nombre_nuevo,
            es_carpeta
        )

        if not insertado:
            return False, "No fue posible insertar el nuevo nombre."

        return (
            True,
            f"'{nombre_antiguo}' actualizado a '{nombre_nuevo}'."
        )

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, nombre):
        """
        Elimina un nodo del árbol.

        Casos:
        1. Nodo hoja.
        2. Nodo con un hijo.
        3. Nodo con dos hijos.
        """

        self.raiz, eliminado, caso = self._eliminar_recursivo(
            self.raiz,
            nombre
        )

        if not eliminado:
            return False, "Nodo no encontrado."

        return True, caso

    def _eliminar_recursivo(self, nodo, nombre):

        if nodo is None:
            return None, False, "Nodo no encontrado."

        nombre_buscar = nombre.casefold()
        nombre_actual = nodo.nombre.casefold()

        if nombre_buscar < nombre_actual:

            nodo.izquierdo, eliminado, caso = \
                self._eliminar_recursivo(
                    nodo.izquierdo,
                    nombre
                )

            return nodo, eliminado, caso

        if nombre_buscar > nombre_actual:

            nodo.derecho, eliminado, caso = \
                self._eliminar_recursivo(
                    nodo.derecho,
                    nombre
                )

            return nodo, eliminado, caso

        # ----------------------------------------------
        # CASO 1: NODO HOJA
        # ----------------------------------------------

        if nodo.izquierdo is None and nodo.derecho is None:

            return (
                None,
                True,
                "Eliminación caso hoja."
            )

        # ----------------------------------------------
        # CASO 2: UN SOLO HIJO DERECHO
        # ----------------------------------------------

        if nodo.izquierdo is None:

            return (
                nodo.derecho,
                True,
                "Eliminación caso nodo con un hijo derecho."
            )

        # ----------------------------------------------
        # CASO 2: UN SOLO HIJO IZQUIERDO
        # ----------------------------------------------

        if nodo.derecho is None:

            return (
                nodo.izquierdo,
                True,
                "Eliminación caso nodo con un hijo izquierdo."
            )

        # ----------------------------------------------
        # CASO 3: DOS HIJOS
        # ----------------------------------------------

        sucesor = self._encontrar_minimo(
            nodo.derecho
        )

        nodo.nombre = sucesor.nombre
        nodo.es_carpeta = sucesor.es_carpeta

        nodo.derecho, _, _ = self._eliminar_recursivo(
            nodo.derecho,
            sucesor.nombre
        )

        return (
            nodo,
            True,
            "Eliminación caso nodo con dos hijos usando sucesor."
        )

    def _encontrar_minimo(self, nodo):

        actual = nodo

        while actual.izquierdo is not None:
            actual = actual.izquierdo

        return actual

    # ==================================================
    # RECORRIDO PREORDEN
    # ==================================================

    def preorden(self):

        resultado = []

        self._preorden_recursivo(
            self.raiz,
            resultado
        )

        return resultado

    def _preorden_recursivo(self, nodo, resultado):

        if nodo is None:
            return

        resultado.append(nodo.nombre)

        self._preorden_recursivo(
            nodo.izquierdo,
            resultado
        )

        self._preorden_recursivo(
            nodo.derecho,
            resultado
        )

    # ==================================================
    # RECORRIDO INORDEN
    # ==================================================

    def inorden(self):

        resultado = []

        self._inorden_recursivo(
            self.raiz,
            resultado
        )

        return resultado

    def _inorden_recursivo(self, nodo, resultado):

        if nodo is None:
            return

        self._inorden_recursivo(
            nodo.izquierdo,
            resultado
        )

        resultado.append(nodo.nombre)

        self._inorden_recursivo(
            nodo.derecho,
            resultado
        )

    # ==================================================
    # RECORRIDO POSTORDEN
    # ==================================================

    def postorden(self):

        resultado = []

        self._postorden_recursivo(
            self.raiz,
            resultado
        )

        return resultado

    def _postorden_recursivo(self, nodo, resultado):

        if nodo is None:
            return

        self._postorden_recursivo(
            nodo.izquierdo,
            resultado
        )

        self._postorden_recursivo(
            nodo.derecho,
            resultado
        )

        resultado.append(nodo.nombre)

    # ==================================================
    # RECORRIDO POR NIVELES
    # ==================================================

    def por_niveles(self):

        resultado = []

        if self.raiz is None:
            return resultado

        cola = deque()

        cola.append(self.raiz)

        while cola:

            actual = cola.popleft()

            resultado.append(actual.nombre)

            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)

            if actual.derecho is not None:
                cola.append(actual.derecho)

        return resultado

    # ==================================================
    # ALTURA
    # ==================================================

    def altura(self):

        return self._calcular_altura(
            self.raiz
        )

    def _calcular_altura(self, nodo):

        if nodo is None:
            return 0

        altura_izquierda = self._calcular_altura(
            nodo.izquierdo
        )

        altura_derecha = self._calcular_altura(
            nodo.derecho
        )

        return 1 + max(
            altura_izquierda,
            altura_derecha
        )