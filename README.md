# Pruebas Unitarias para la API de Rick and Morty

## Descripción
Este proyecto implementa un conjunto de pruebas unitarias utilizando `pytest` para verificar el correcto funcionamiento de la API pública de Rick and Morty.

## Tecnologías Utilizadas
- Python
- pytest
- requests

## Instalación y Configuración
Para ejecutar las pruebas, sigue estos pasos:

1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Casos de Prueba

| #  | Caso de Prueba                        | Descripción |
|----|-------------------------------------|-------------|
| 1  | `test_api_status`                   | Verifica que el endpoint de `character` responde con código 200. |
| 2  | `test_character_name`               | Comprueba que el personaje con ID `1` es "Rick Sanchez". |
| 3  | `test_character_not_found`          | Valida que un personaje con un ID inexistente devuelva un código 404. |
| 4  | `test_episode_characters`           | Asegura que el episodio con ID `1` contiene al menos un personaje. |
| 5  | `test_location`                      | Verifica que la ubicación con ID `1` sea "Earth (C-137)". |
| 6  | `test_character_response_structure` | Comprueba que la respuesta del personaje con ID `1` contenga todas las claves esperadas. |

## Ejecución de las Pruebas
Para ejecutar las pruebas, usa el siguiente comando:
```bash
pytest test_api.py
```

Si deseas obtener un informe más detallado, puedes usar:
```bash
pytest -v
```

## Contribuciones
Si deseas contribuir a este proyecto, por favor, abre un issue o un pull request con tus mejoras.

## Licencia
Este proyecto está bajo la licencia MIT.
