# Proyecto Urban Grocers

Automatización de pruebas para el endpoint de creación de kits de productos en la aplicación Urban Grocers, enfocada en la validación del campo `name` del cuerpo de la solicitud.

## Descripción

Este proyecto automatiza una lista de comprobación de 9 casos de prueba sobre el campo `name` al crear un kit de productos personal para un usuario o usuaria. Las pruebas cubren:

- Límites permitidos de caracteres (1 y 511 caracteres)
- Límites no permitidos de caracteres (0 y 512 caracteres)
- Caracteres especiales
- Espacios en blanco
- Números como texto
- Ausencia del parámetro `name`
- Tipo de dato incorrecto (número en vez de string)

## Documentación de la API

La documentación de los endpoints utilizados está disponible en:
https://cnt-822aef79-abc7-4197-9ff9-bcf10a04023c.containerhub.tripleten-services.com/docs/

## Flujo de prueba

1. Se crea un nuevo usuario o usuaria (`POST /api/v1/users`) y se obtiene su `authToken`.
2. Se envía una solicitud para crear un kit personal para ese usuario (`POST /api/v1/kits`), incluyendo el encabezado `Authorization`.
3. Se valida el código de respuesta y, en los casos positivos, que el campo `name` de la respuesta coincida con el de la solicitud.

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `configuration.py` | URL base del servicio y rutas (endpoints) |
| `data.py` | Datos base para las solicitudes (usuario y kit) |
| `sender_stand_request.py` | Funciones para enviar las solicitudes HTTP |
| `create_kit_name_kit_test.py` | Pruebas automatizadas del campo `name` |
| `.gitignore` | Archivos/carpetas excluidos del control de versiones |

## Tecnologías y técnicas utilizadas

**Tecnologías:**
- Python 3
- pytest — framework de pruebas
- requests — cliente HTTP para las solicitudes a la API

**Técnicas:**
- Pruebas positivas y negativas separadas en funciones reutilizables (`positive_assert`, `negative_assert`)
- Generación dinámica de datos de prueba (por ejemplo, cadenas de longitud exacta con `"Abcd" * 128`)
- Copia de diccionarios base (`.copy()`) para no modificar los datos de origen
- Autenticación mediante token Bearer obtenido dinámicamente para cada prueba

## Instalación

\`\`\`bash
pip install pytest requests
\`\`\`

## Cómo ejecutar las pruebas

\`\`\`bash
pytest create_kit_name_kit_test.py
\`\`\`
