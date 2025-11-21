# Buscador

Utilidad en Python para ejecutar busquedas OSINT rapidas tanto desde consola como desde un bot de Telegram. Usa DuckDuckGo para consultas directas y Google Custom Search para el bot, leyendo las llaves desde la carpeta `key` (ignoradas en Git).

## Estructura
- `buscador.py`: script interactivo que pide palabras clave y redes sociales, consulta texto e imagenes con `duckduckgo_search`.
- `Search/`: modulos reutilizables para el bot (`searching.py`, `query_search.py`, `my_token.py`).
- `Tegram/bot.py`: bot de Telegram con comandos `/start`, `/search` y `/help`.
- `requirements.txt`: dependencias de Python.
- `key/`: colocar llaves privadas (no se versionan).

## Requisitos
- Python 3.11+ recomendado.
- Dependencias: `pip install -r requirements.txt` (idealmente dentro de un entorno virtual).

## Configuracion de llaves (carpeta `key`)
Crea los archivos de texto plano dentro de `key/` con su valor en la primera linea:
- `google_api.txt`: API key de Google Custom Search.
- `google_searchengine.txt`: Search Engine ID (cx) de Google Custom Search.
- `telegram_token.txt`: token del bot de Telegram.

## Uso por consola (`buscador.py`)
1) Ejecuta `python buscador.py`.
2) Indica cuantas palabras clave deseas combinar; se generan consultas con `AND`.
3) Selecciona una o varias redes sociales de la lista; se genera una busqueda por cada red.
4) Decide si tambien quieres buscar imagenes; se muestran hasta 2 resultados de texto y 2 de imagenes por red.

## Uso del bot de Telegram
1) Asegura que `key/telegram_token.txt` tiene el token del bot y el API de Google esta configurado.
2) Inicia el bot con `python -m Tegram.bot`.
3) Comandos disponibles:
   - `/start`: mensaje de bienvenida.
   - `/help`: atajos disponibles.
   - `/search <consulta>`: envia la consulta; se devuelven hasta 30 resultados (en paginas de 10). Puedes combinar terminos y banderas:
     - `-d=dominio.com` limita a un dominio (o varios separados por coma).
     - `-ft=pdf` filtra por tipo de archivo.
     - `-it=palabra` busca en el titulo.
     - `-ait=palabra` busca en todos los titulos.
     - `-we=frase exacta` busca la frase exacta entre comillas.
     - `-e=termino` excluye terminos.
     - `-or=opcion1,opcion2` combina con OR.

## Notas
- La carpeta `key/` ya esta en `.gitignore` para evitar subir llaves.
- Si deseas personalizar limites de resultados del bot, ajusta `max_items` en `Search/searching.py` (metodo `format_request`).
