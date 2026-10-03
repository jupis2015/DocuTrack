# DocuTrack S.A. - Árbol Binario de Búsqueda

## Actividad colaborativa I
### Taller Integrador - Árboles Binarios

Este proyecto implementa un sistema de gestión jerárquica de documentos
para la empresa ficticia DocuTrack S.A., utilizando un Árbol Binario de
Búsqueda (BST).

Cada nodo representa una carpeta o un archivo. Los nodos son organizados
alfabéticamente por su nombre, ignorando diferencias entre mayúsculas
y minúsculas.

El proyecto fue desarrollado en Python utilizando una arquitectura MVC
(Modelo - Vista - Controlador).

---

## Integrantes

| Integrante | Responsabilidad |
|---|---|
| NOMBRE INTEGRANTE 1 | Desarrollo del Model y estructura del BST |
| NOMBRE INTEGRANTE 2 | Desarrollo de View, impresión ASCII y pruebas |
| NOMBRE INTEGRANTE 3 | Controller, documentación y pruebas finales |

> Modificar esta sección con los nombres reales de los integrantes y
> las responsabilidades realizadas por cada uno.

---

## Objetivo

Desarrollar un módulo que permita administrar una estructura jerárquica
de archivos y carpetas utilizando un Árbol Binario de Búsqueda.

El sistema permite realizar operaciones CRUD, búsquedas, recorridos,
actualizaciones, eliminaciones y visualizar gráficamente la estructura
del árbol mediante caracteres ASCII.

---

## Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- Arquitectura MVC

No se requieren librerías externas.

---

## Arquitectura MVC

El proyecto utiliza el patrón Modelo - Vista - Controlador.

### Model

Ubicado en:

`model/`

Contiene la lógica y estructura del Árbol Binario de Búsqueda.

Archivos:

- `nodo.py`
- `arbol_binario.py`

El Model se encarga de:

- Crear nodos.
- Insertar nodos.
- Buscar nodos.
- Actualizar nodos.
- Eliminar nodos.
- Realizar recorridos.
- Calcular la altura del árbol.

El Model no realiza impresiones directamente en consola.

### View

Ubicada en:

`view/`

Archivo principal:

`arbol_view.py`

Se encarga exclusivamente de presentar información al usuario.

Entre sus responsabilidades se encuentran:

- Mostrar resultados de inserción.
- Mostrar búsquedas.
- Mostrar número de comparaciones.
- Mostrar actualizaciones.
- Mostrar eliminaciones.
- Mostrar recorridos.
- Mostrar métricas.
- Dibujar el árbol mediante caracteres ASCII.

### Controller

Ubicado en:

`controller/`

Archivo principal:

`arbol_controller.py`

Se encarga de coordinar los diferentes casos de uso del sistema.

El Controller ejecuta:

1. Construcción del árbol.
2. Búsquedas.
3. Actualizaciones.
4. Eliminaciones.
5. Recorridos.
6. Cálculo de la altura.

---

## Estructura del proyecto

```text
DocuTrack/
│
├── controller/
│   ├── __init__.py
│   └── arbol_controller.py
│
├── model/
│   ├── __init__.py
│   ├── nodo.py
│   └── arbol_binario.py
│
├── view/
│   ├── __init__.py
│   └── arbol_view.py
│
├── main.py
├── README.md
└── .gitignore