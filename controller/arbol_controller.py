from model.arbol_binario import ArbolBinario
from view.arbol_view import ArbolView


class ArbolController:
    def __init__(self):
        self.arbol = ArbolBinario()
        self.view = ArbolView()

    def ejecutar(self):
        self.view.mostrar_titulo(
            "DOCUTRACK S.A. - ÁRBOL BINARIO DE BÚSQUEDA"
        )

        self.construir_arbol()
        self.realizar_busquedas()
        self.realizar_actualizaciones()
        self.realizar_eliminaciones()
        self.mostrar_recorridos()
        self.mostrar_altura()

        self.view.mostrar_titulo("FIN DE LAS PRUEBAS")

    # ==========================================================
    # 1. CONSTRUCCIÓN DEL ÁRBOL
    # ==========================================================

    def construir_arbol(self):
        self.view.mostrar_titulo("1. CONSTRUCCIÓN DEL ÁRBOL")

        # True  = Carpeta
        # False = Archivo
        #
        # Los nodos que tendrán hijos se definen como carpetas.
        # Los archivos se mantienen como nodos hoja.
        datos = [
            ("Documentos", True),
            ("Clientes", True),
            ("Proyectos", True),
            ("Archivos", True),
            ("Contratos", True),
            ("Informes", True),
            ("Ventas", True),
            ("Backup", True),
            ("Compras", True),
            ("Reportes", True),
            ("Usuarios", False),
            ("Zonas", False),
            ("Cartas", True),
            ("Configuracion", False)
        ]

        for nombre, es_carpeta in datos:
            insertado, comparaciones = self.arbol.insertar(
                nombre,
                es_carpeta
            )

            self.view.mostrar_insercion(
                nombre,
                insertado,
                comparaciones
            )

        self.view.mostrar_arbol(self.arbol.raiz)

    # ==========================================================
    # 2. BÚSQUEDAS
    # ==========================================================

    def realizar_busquedas(self):
        self.view.mostrar_titulo("2. BÚSQUEDAS RÁPIDAS")

        # Dos búsquedas hacia el subárbol izquierdo.
        # Dos hacia el subárbol derecho.
        # Dos elementos inexistentes.
        busquedas = [
            "Archivos",
            "Contratos",
            "Informes",
            "Ventas",
            "Nomina",
            "Seguridad"
        ]

        for nombre in busquedas:
            nodo, comparaciones = self.arbol.buscar(nombre)

            self.view.mostrar_busqueda(
                nombre,
                nodo,
                comparaciones
            )

    # ==========================================================
    # 3. ACTUALIZACIONES
    # ==========================================================

    def realizar_actualizaciones(self):
        self.view.mostrar_titulo(
            "3. ACTUALIZACIONES SELECTIVAS"
        )

        # ------------------------------------------------------
        # Actualización de un archivo hoja
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Actualización de archivo hoja"
        )

        exito, mensaje = self.arbol.actualizar(
            "Configuracion",
            "Consultas"
        )

        self.view.mostrar_actualizacion(
            exito,
            mensaje
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # ------------------------------------------------------
        # Actualización de nodo con un hijo
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Actualización de nodo con un hijo"
        )

        exito, mensaje = self.arbol.actualizar(
            "Backup",
            "Biblioteca"
        )

        self.view.mostrar_actualizacion(
            exito,
            mensaje
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # ------------------------------------------------------
        # Actualización de la raíz
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Actualización de la raíz"
        )

        nombre_raiz = self.arbol.raiz.nombre

        exito, mensaje = self.arbol.actualizar(
            nombre_raiz,
            "GestionDocumental"
        )

        self.view.mostrar_actualizacion(
            exito,
            mensaje
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

    # ==========================================================
    # 4. ELIMINACIONES
    # ==========================================================

    def realizar_eliminaciones(self):
        self.view.mostrar_titulo(
            "4. ELIMINACIONES SELECTIVAS"
        )

        # ------------------------------------------------------
        # Eliminación de nodo hoja
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Eliminación de nodo hoja"
        )

        exito, caso = self.arbol.eliminar(
            "Consultas"
        )

        self.view.mostrar_eliminacion(
            "Consultas",
            exito,
            caso
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # ------------------------------------------------------
        # Eliminación de nodo con un hijo
        # Reportes tiene como hijo a Usuarios.
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Eliminación de nodo con un hijo"
        )

        exito, caso = self.arbol.eliminar(
            "Reportes"
        )

        self.view.mostrar_eliminacion(
            "Reportes",
            exito,
            caso
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # ------------------------------------------------------
        # Eliminación de la raíz con dos hijos
        # ------------------------------------------------------
        self.view.mostrar_subtitulo(
            "Eliminación de la raíz con dos hijos"
        )

        nombre_raiz = self.arbol.raiz.nombre

        exito, caso = self.arbol.eliminar(
            nombre_raiz
        )

        self.view.mostrar_eliminacion(
            nombre_raiz,
            exito,
            caso
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

    # ==========================================================
    # 5. RECORRIDOS
    # ==========================================================

    def mostrar_recorridos(self):
        self.view.mostrar_titulo(
            "5. RECORRIDOS DE VERIFICACIÓN"
        )

        self.view.mostrar_recorrido(
            "Preorden",
            self.arbol.preorden()
        )

        self.view.mostrar_recorrido(
            "Inorden",
            self.arbol.inorden()
        )

        self.view.mostrar_recorrido(
            "Postorden",
            self.arbol.postorden()
        )

        self.view.mostrar_recorrido(
            "Por niveles",
            self.arbol.por_niveles()
        )

    # ==========================================================
    # 6. ALTURA
    # ==========================================================

    def mostrar_altura(self):
        self.view.mostrar_titulo(
            "6. MÉTRICAS FINALES"
        )

        altura = self.arbol.altura()

        self.view.mostrar_altura(
            altura
        )