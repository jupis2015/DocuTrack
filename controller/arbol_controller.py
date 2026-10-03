from model.arbol_binario import ArbolBinario
from view.arbol_view import ArbolView


class ArbolController:

    def __init__(self):
        self.arbol = ArbolBinario()
        self.view = ArbolView()

    # ==================================================
    # EJECUCIÓN PRINCIPAL
    # ==================================================

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

        self.view.mostrar_titulo(
            "FIN DE LAS PRUEBAS"
        )

    # ==================================================
    # 1. CONSTRUCCIÓN DEL ÁRBOL
    # ==================================================

    def construir_arbol(self):

        self.view.mostrar_titulo(
            "1. CONSTRUCCIÓN DEL ÁRBOL"
        )

        # 14 nodos: mezcla de carpetas y archivos.
        # Fueron seleccionados para generar:
        # - raíz con dos subárboles
        # - nodos hoja
        # - nodos con un solo hijo
        # - nodos con dos hijos
        datos = [
            ("Documentos", True),
            ("Clientes", True),
            ("Proyectos", True),
            ("Archivos", True),
            ("Contratos", False),
            ("Informes", False),
            ("Ventas", True),
            ("Backup", True),
            ("Compras", False),
            ("Reportes", False),
            ("Usuarios", True),
            ("Zonas", True),
            ("Cartas", False),
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

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

    # ==================================================
    # 2. BÚSQUEDAS RÁPIDAS
    # ==================================================

    def realizar_busquedas(self):

        self.view.mostrar_titulo(
            "2. BÚSQUEDAS RÁPIDAS"
        )

        # 2 existentes del subárbol izquierdo:
        # Archivos y Contratos
        #
        # 2 existentes del subárbol derecho:
        # Informes y Ventas
        #
        # 2 inexistentes:
        # Nomina y Seguridad
        busquedas = [
            "Archivos",
            "Contratos",
            "Informes",
            "Ventas",
            "Nomina",
            "Seguridad"
        ]

        for nombre in busquedas:

            nodo, comparaciones = self.arbol.buscar(
                nombre
            )

            self.view.mostrar_busqueda(
                nombre,
                nodo,
                comparaciones
            )

    # ==================================================
    # 3. ACTUALIZACIONES SELECTIVAS
    # ==================================================

    def realizar_actualizaciones(self):

        self.view.mostrar_titulo(
            "3. ACTUALIZACIONES SELECTIVAS"
        )

        # --------------------------------------------------
        # ACTUALIZACIÓN 1:
        # Nodo hoja
        # Cartas -> Certificados
        # --------------------------------------------------

        self.view.mostrar_subtitulo(
            "Actualización de nodo hoja"
        )

        exito, mensaje = self.arbol.actualizar(
            "Cartas",
            "Certificados"
        )

        self.view.mostrar_actualizacion(
            exito,
            mensaje
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # --------------------------------------------------
        # ACTUALIZACIÓN 2:
        # Nodo con un único hijo
        # Backup -> Biblioteca
        # --------------------------------------------------

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

        # --------------------------------------------------
        # ACTUALIZACIÓN 3:
        # Actualización de la raíz.
        #
        # IMPORTANTE:
        # Se obtiene el nombre actual de la raíz y se
        # actualiza mediante Eliminar + Insertar.
        # --------------------------------------------------

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

    # ==================================================
    # 4. ELIMINACIONES SELECTIVAS
    # ==================================================

    def realizar_eliminaciones(self):

        self.view.mostrar_titulo(
            "4. ELIMINACIONES SELECTIVAS"
        )

        # --------------------------------------------------
        # ELIMINACIÓN 1:
        # Nodo hoja
        #
        # Configuracion no tiene hijos.
        # --------------------------------------------------

        self.view.mostrar_subtitulo(
            "Eliminación de nodo hoja"
        )

        exito, caso = self.arbol.eliminar(
            "Configuracion"
        )

        self.view.mostrar_eliminacion(
            "Configuracion",
            exito,
            caso
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # --------------------------------------------------
        # ELIMINACIÓN 2:
        # Nodo con UN hijo
        #
        # Después de las actualizaciones:
        #
        # Archivos
        #     └── Certificados
        #             └── Biblioteca
        #
        # Por lo tanto, Certificados tiene exactamente
        # un hijo: Biblioteca.
        #
        # Al eliminar Certificados, Biblioteca debe quedar
        # conectado directamente con Archivos.
        # --------------------------------------------------

        self.view.mostrar_subtitulo(
            "Eliminación de nodo con un hijo"
        )

        exito, caso = self.arbol.eliminar(
            "Certificados"
        )

        self.view.mostrar_eliminacion(
            "Certificados",
            exito,
            caso
        )

        self.view.mostrar_arbol(
            self.arbol.raiz
        )

        # --------------------------------------------------
        # ELIMINACIÓN 3:
        # Eliminación de la raíz
        #
        # Se obtiene dinámicamente el nombre de la raíz
        # porque después de las actualizaciones puede
        # haber cambiado.
        #
        # La raíz tiene dos hijos, por lo que el Model
        # utilizará el sucesor.
        # --------------------------------------------------

        self.view.mostrar_subtitulo(
            "Eliminación de la raíz"
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

    # ==================================================
    # 5. RECORRIDOS DE VERIFICACIÓN
    # ==================================================

    def mostrar_recorridos(self):

        self.view.mostrar_titulo(
            "5. RECORRIDOS DE VERIFICACIÓN"
        )

        # PREORDEN
        self.view.mostrar_recorrido(
            "Preorden",
            self.arbol.preorden()
        )

        # INORDEN
        # Este recorrido permite verificar que el BST
        # continúa correctamente ordenado.
        self.view.mostrar_recorrido(
            "Inorden",
            self.arbol.inorden()
        )

        # POSTORDEN
        self.view.mostrar_recorrido(
            "Postorden",
            self.arbol.postorden()
        )

        # POR NIVELES
        self.view.mostrar_recorrido(
            "Por niveles",
            self.arbol.por_niveles()
        )

    # ==================================================
    # 6. ALTURA FINAL
    # ==================================================

    def mostrar_altura(self):

        self.view.mostrar_titulo(
            "6. MÉTRICAS FINALES"
        )

        altura = self.arbol.altura()

        self.view.mostrar_altura(
            altura
        )