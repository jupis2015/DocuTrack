# DocuTrack S.A. - Árbol Binario de Búsqueda

## Descripción del proyecto

Este proyecto implementa un **Árbol Binario de Búsqueda (BST)** para la empresa ficticia **DocuTrack S.A.**, con el propósito de representar de forma jerárquica un repositorio de documentos compuesto por carpetas y archivos.

El sistema fue desarrollado en **Python** aplicando una arquitectura **MVC (Modelo - Vista - Controlador)**, separando la lógica del árbol, la presentación de información en consola y la ejecución de los casos de prueba.

Cada nodo del árbol se identifica mediante su atributo `Nombre`, utilizando comparaciones de texto sin distinguir entre mayúsculas y minúsculas.

Las reglas principales del árbol son:

- Los nombres menores se almacenan en el subárbol izquierdo.
- Los nombres mayores se almacenan en el subárbol derecho.
- No se permiten nombres duplicados.
- Los archivos se mantienen como nodos hoja.
- Las carpetas pueden contener cero, uno o dos nodos hijos.

---

## Integrantes

| Integrante | Responsabilidad |
|---|---|
| HENRY FRANCO VELEZ | Implementación y revisión del Modelo y operaciones del BST |
| NOMBRE INTEGRANTE 2 | Implementación y revisión de la Vista, árbol ASCII y pruebas |
| NOMBRE INTEGRANTE 3 | Implementación y revisión del Controlador, documentación y pruebas finales |

> Reemplazar los nombres anteriores por los nombres completos de los integrantes del grupo.

---

## Objetivo

Desarrollar una aplicación de consola que permita administrar una estructura jerárquica de archivos y carpetas mediante un **Árbol Binario de Búsqueda**, implementando operaciones CRUD, búsquedas, recorridos, métricas e impresión visual del árbol mediante arquitectura MVC.

---

## Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub
- Programación Orientada a Objetos
- Arquitectura MVC
- Árbol Binario de Búsqueda (BST)

---

## Arquitectura MVC

El proyecto se encuentra dividido en tres componentes principales.

### Modelo

Ubicado en la carpeta:

```text
model/
```

Contiene las clases encargadas de representar los datos y realizar las operaciones estructurales del árbol.

#### `nodo.py`

Define la clase `Nodo`, cuyos principales atributos son:

```text
nombre
es_carpeta
izquierdo
derecho
```

#### `arbol_binario.py`

Contiene la implementación del Árbol Binario de Búsqueda y las operaciones:

- Insertar
- Buscar
- Actualizar
- Eliminar
- Preorden
- Inorden
- Postorden
- Recorrido por niveles
- Cálculo de altura

El Modelo no realiza impresiones directamente en consola.

---

### Vista

Ubicada en:

```text
view/
```

El archivo:

```text
arbol_view.py
```

es responsable de presentar la información al usuario.

Entre sus funciones se encuentran:

- Mostrar títulos y subtítulos.
- Mostrar resultados de inserciones.
- Mostrar resultados de búsquedas.
- Mostrar cantidad de comparaciones.
- Mostrar actualizaciones.
- Mostrar eliminaciones y el caso aplicado.
- Mostrar recorridos.
- Mostrar la altura final.
- Representar el árbol utilizando conectores ASCII.

Ejemplo:

```text
[Carpeta] Documentos
├── [Carpeta] Clientes
│   ├── [Carpeta] Archivos
│   └── [Carpeta] Contratos
└── [Carpeta] Proyectos
    ├── [Carpeta] Informes
    └── [Carpeta] Ventas
```

---

### Controlador

Ubicado en:

```text
controller/
```

El archivo:

```text
arbol_controller.py
```

coordina la ejecución de los casos de prueba.

El Controlador se encarga de:

- Construir el árbol inicial.
- Ejecutar búsquedas.
- Ejecutar actualizaciones.
- Ejecutar eliminaciones.
- Solicitar los recorridos.
- Solicitar el cálculo de la altura.
- Enviar los resultados a la Vista.

La lógica estructural del BST permanece en el Modelo.

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
│   ├── arbol_binario.py
│   └── nodo.py
│
├── view/
│   ├── __init__.py
│   └── arbol_view.py
│
├── .gitignore
├── main.py
└── README.md
```

Los directorios `__pycache__` generados automáticamente por Python están excluidos del repositorio mediante `.gitignore`.

---

# Funcionamiento del Árbol Binario de Búsqueda

La clave utilizada para ordenar el árbol es el atributo:

```text
Nombre
```

La comparación se realiza sin distinguir entre mayúsculas y minúsculas.

Para cada inserción:

```text
Nombre menor  → subárbol izquierdo
Nombre mayor  → subárbol derecho
Nombre igual  → inserción rechazada
```

El proyecto utiliza un BST simple con fines académicos, por lo que no implementa mecanismos de auto-balanceo.

---

## Construcción inicial

Para las pruebas se insertan los siguientes 14 nombres:

```text
Documentos
Clientes
Proyectos
Archivos
Contratos
Informes
Ventas
Backup
Compras
Reportes
Usuarios
Zonas
Cartas
Configuracion
```

El árbol inicial generado es:

```text
[Carpeta] Documentos
├── [Carpeta] Clientes
│   ├── [Carpeta] Archivos
│   │   └── [Carpeta] Backup
│   │       └── [Carpeta] Cartas
│   └── [Carpeta] Contratos
│       └── [Carpeta] Compras
│           └── [Archivo] Configuracion
└── [Carpeta] Proyectos
    ├── [Carpeta] Informes
    └── [Carpeta] Ventas
        ├── [Carpeta] Reportes
        │   └── [Archivo] Usuarios
        └── [Archivo] Zonas
```

De esta manera se dispone de:

- Una raíz con dos subárboles.
- Nodos hoja en ambos lados.
- Nodos con un hijo.
- Carpetas con diferentes configuraciones.
- Archivos mantenidos como nodos hoja.

---

# Operaciones CRUD

## Inserción

El método de inserción compara el nombre del nuevo nodo con los nodos existentes.

Si el nombre ya existe, la inserción es rechazada.

También se registra la cantidad de comparaciones realizadas durante la operación.

---

## Búsqueda

Se realizan seis búsquedas de prueba.

### Elementos existentes

```text
Archivos
Contratos
Informes
Ventas
```

### Elementos inexistentes

```text
Nomina
Seguridad
```

Resultados obtenidos:

```text
Archivos  → Hallado | 3 comparaciones
Contratos → Hallado | 3 comparaciones
Informes  → Hallado | 3 comparaciones
Ventas    → Hallado | 3 comparaciones
Nomina    → No hallado | 3 comparaciones
Seguridad → No hallado | 5 comparaciones
```

---

# Actualizaciones

Las actualizaciones se implementan mediante:

```text
Eliminar nodo anterior
        ↓
Insertar nodo con el nuevo nombre
```

Antes de realizar la operación se comprueba que el nuevo nombre no exista.

## 1. Actualización de archivo hoja

```text
Configuracion
      ↓
Consultas
```

Resultado:

```text
[OK] 'Configuracion' actualizado a 'Consultas'.
```

`Consultas` continúa siendo un archivo hoja.

---

## 2. Actualización de nodo con un hijo

```text
Backup
   ↓
Biblioteca
```

Resultado:

```text
[OK] 'Backup' actualizado a 'Biblioteca'.
```

---

## 3. Actualización de la raíz

La raíz inicial:

```text
Documentos
```

es actualizada a:

```text
GestionDocumental
```

La actualización se realiza utilizando la estrategia de eliminación e inserción.

Después de la operación, la estructura del BST se reorganiza correctamente y `Informes` pasa a ocupar la raíz.

---

# Eliminaciones

El proyecto demuestra los tres casos principales de eliminación de un BST.

## Caso 1 - Nodo hoja

Se elimina:

```text
Consultas
```

Resultado:

```text
Eliminación caso hoja.
```

---

## Caso 2 - Nodo con un hijo

Se elimina:

```text
Reportes
```

Este nodo tiene como hijo derecho a:

```text
Usuarios
```

Resultado:

```text
Eliminación caso nodo con un hijo derecho.
```

Después de la eliminación, `Usuarios` ocupa correctamente la posición correspondiente.

---

## Caso 3 - Nodo con dos hijos

Después de las actualizaciones, la raíz es:

```text
Informes
```

Se elimina esta raíz utilizando el **sucesor en Inorden**.

Resultado:

```text
Eliminación caso nodo con dos hijos usando sucesor.
```

La nueva raíz pasa a ser:

```text
Proyectos
```

---

# Árbol final

Después de realizar las actualizaciones y eliminaciones, el árbol queda de la siguiente manera:

```text
[Carpeta] Proyectos
├── [Carpeta] Clientes
│   ├── [Carpeta] Archivos
│   │   └── [Carpeta] Cartas
│   │       └── [Carpeta] Biblioteca
│   └── [Carpeta] Contratos
│       ├── [Carpeta] Compras
│       └── [Carpeta] GestionDocumental
└── [Carpeta] Ventas
    ├── [Archivo] Usuarios
    └── [Archivo] Zonas
```

---

# Recorridos

El sistema implementa los cuatro recorridos solicitados.

## Preorden

```text
Proyectos -> Clientes -> Archivos -> Cartas -> Biblioteca -> Contratos -> Compras -> GestionDocumental -> Ventas -> Usuarios -> Zonas
```

## Inorden

```text
Archivos -> Biblioteca -> Cartas -> Clientes -> Compras -> Contratos -> GestionDocumental -> Proyectos -> Usuarios -> Ventas -> Zonas
```

## Postorden

```text
Biblioteca -> Cartas -> Archivos -> Compras -> GestionDocumental -> Contratos -> Clientes -> Usuarios -> Zonas -> Ventas -> Proyectos
```

## Por niveles

```text
Proyectos -> Clientes -> Ventas -> Archivos -> Contratos -> Usuarios -> Zonas -> Cartas -> Compras -> GestionDocumental -> Biblioteca
```

---

## Verificación mediante Inorden

El recorrido **Inorden** de un Árbol Binario de Búsqueda visita los nodos siguiendo la secuencia:

```text
Subárbol izquierdo
        ↓
Nodo actual
        ↓
Subárbol derecho
```

Debido a que el árbol utiliza `Nombre` como clave, el recorrido Inorden permite comprobar que los nombres se encuentran ordenados de acuerdo con el criterio de comparación utilizado por el BST.

El resultado final es:

```text
Archivos
Biblioteca
Cartas
Clientes
Compras
Contratos
GestionDocumental
Proyectos
Usuarios
Ventas
Zonas
```

Esto permite verificar el correcto funcionamiento del criterio de ordenamiento del árbol.

---

# Métricas

El sistema registra la cantidad de comparaciones realizadas durante:

- Inserciones.
- Búsquedas.

La altura final obtenida después de ejecutar todos los casos de prueba es:

```text
5
```

---

# Validaciones

El sistema contempla validaciones para:

- Nombres vacíos.
- Valores inválidos.
- Nombres duplicados.
- Búsqueda de elementos inexistentes.
- Actualización de elementos inexistentes.
- Actualización hacia un nombre ya existente.
- Eliminación de elementos inexistentes.

Las comparaciones de nombres no distinguen entre mayúsculas y minúsculas.

---

# Ejecución del proyecto

## Requisitos

Tener instalado:

```text
Python 3
```

Para comprobar la instalación:

```bash
python --version
```

---

## Ejecutar

Abrir una terminal en la carpeta raíz del proyecto:

```text
DocuTrack/
```

y ejecutar:

```bash
python main.py
```

También puede utilizarse:

```bash
python3 main.py
```

dependiendo de la configuración del sistema operativo.

---

# Resultados esperados

Al ejecutar el proyecto se muestran en consola, en el siguiente orden:

1. Construcción del árbol con 14 nombres.
2. Representación ASCII del árbol inicial.
3. Seis búsquedas y sus comparaciones.
4. Tres actualizaciones.
5. Representación del árbol después de cada actualización.
6. Tres eliminaciones correspondientes a los casos solicitados.
7. Representación del árbol después de cada eliminación.
8. Recorrido Preorden.
9. Recorrido Inorden.
10. Recorrido Postorden.
11. Recorrido por niveles.
12. Altura final del árbol.

---

# Conclusión

El proyecto demuestra la implementación de un **Árbol Binario de Búsqueda en Python utilizando arquitectura MVC**.

La separación entre Modelo, Vista y Controlador permite mantener organizada la lógica del sistema: el Modelo administra la estructura y operaciones del BST, la Vista se encarga exclusivamente de presentar la información y el Controlador coordina los diferentes casos de prueba.

Las operaciones implementadas permiten demostrar inserciones, búsquedas, actualizaciones mediante eliminación e inserción, los principales casos de eliminación de un BST, recorridos y cálculo de altura.

El recorrido Inorden permite comprobar el orden establecido por la clave `Nombre`, mientras que la representación ASCII facilita visualizar los cambios producidos en la estructura durante la ejecución.

---

## Repositorio

Repositorio público del proyecto:

https://github.com/jupis2015/DocuTrack

---

## Versión final

La versión final de la actividad será identificada mediante la etiqueta:

```text
release-unidad1
```