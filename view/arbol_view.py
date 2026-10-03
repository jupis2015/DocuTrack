class ArbolView:

    # ==================================================
    # ENCABEZADOS
    # ==================================================

    def mostrar_titulo(self, titulo):
        print("\n" + "=" * 65)
        print(titulo.center(65))
        print("=" * 65)

    def mostrar_subtitulo(self, subtitulo):
        print("\n" + "-" * 65)
        print(subtitulo)
        print("-" * 65)

    # ==================================================
    # MENSAJES GENERALES
    # ==================================================

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

    # ==================================================
    # RESULTADO DE INSERCIÓN
    # ==================================================

    def mostrar_insercion(self, nombre, insertado, comparaciones):

        if insertado:
            print(
                f"[OK] '{nombre}' insertado correctamente "
                f"| Comparaciones: {comparaciones}"
            )
        else:
            print(
                f"[ERROR] No se pudo insertar '{nombre}'. "
                f"Puede estar duplicado o ser inválido "
                f"| Comparaciones: {comparaciones}"
            )

    # ==================================================
    # RESULTADO DE BÚSQUEDA
    # ==================================================

    def mostrar_busqueda(self, nombre, nodo, comparaciones):

        if nodo is not None:

            tipo = (
                "Carpeta"
                if nodo.es_carpeta
                else "Archivo"
            )

            print(
                f"[HALLADO] '{nombre}' "
                f"-> {tipo} "
                f"| Comparaciones: {comparaciones}"
            )

        else:

            print(
                f"[NO HALLADO] '{nombre}' "
                f"| Comparaciones: {comparaciones}"
            )

    # ==================================================
    # RESULTADO DE ACTUALIZACIÓN
    # ==================================================

    def mostrar_actualizacion(self, exito, mensaje):

        if exito:
            print(f"[OK] {mensaje}")
        else:
            print(f"[ERROR] {mensaje}")

    # ==================================================
    # RESULTADO DE ELIMINACIÓN
    # ==================================================

    def mostrar_eliminacion(self, nombre, exito, caso):

        if exito:

            print(
                f"[OK] '{nombre}' eliminado."
            )

            print(
                f"     {caso}"
            )

        else:

            print(
                f"[ERROR] No se encontró '{nombre}'."
            )

    # ==================================================
    # RECORRIDOS
    # ==================================================

    def mostrar_recorrido(self, nombre, recorrido):

        print(
            f"{nombre}: "
            + " -> ".join(recorrido)
        )

    # ==================================================
    # ALTURA
    # ==================================================

    def mostrar_altura(self, altura):

        print(
            f"\nAltura final del árbol: {altura}"
        )

    # ==================================================
    # IMPRESIÓN DEL ÁRBOL
    # ==================================================

    def mostrar_arbol(self, raiz):

        print("\nEstructura actual del árbol:\n")

        if raiz is None:
            print("(Árbol vacío)")
            return

        tipo = (
            "Carpeta"
            if raiz.es_carpeta
            else "Archivo"
        )

        print(
            f"[{tipo}] {raiz.nombre}"
        )

        hijos = []

        if raiz.izquierdo is not None:
            hijos.append(raiz.izquierdo)

        if raiz.derecho is not None:
            hijos.append(raiz.derecho)

        for indice, hijo in enumerate(hijos):

            es_ultimo = (
                indice == len(hijos) - 1
            )

            self._imprimir_nodo(
                hijo,
                "",
                es_ultimo
            )

    def _imprimir_nodo(
        self,
        nodo,
        prefijo,
        es_ultimo
    ):

        conector = (
            "└── "
            if es_ultimo
            else "├── "
        )

        tipo = (
            "Carpeta"
            if nodo.es_carpeta
            else "Archivo"
        )

        print(
            prefijo
            + conector
            + f"[{tipo}] {nodo.nombre}"
        )

        nuevo_prefijo = (
            prefijo
            + (
                "    "
                if es_ultimo
                else "│   "
            )
        )

        hijos = []

        if nodo.izquierdo is not None:
            hijos.append(nodo.izquierdo)

        if nodo.derecho is not None:
            hijos.append(nodo.derecho)

        for indice, hijo in enumerate(hijos):

            ultimo_hijo = (
                indice == len(hijos) - 1
            )

            self._imprimir_nodo(
                hijo,
                nuevo_prefijo,
                ultimo_hijo
            )