import os


class my_token:

    def __init__(self):
        pass

    @classmethod
    def paths_file(cls, pather: str, folder: str, file: str) -> str:
        BASE = os.path.dirname(os.path.abspath(__file__))
        RUTA = os.path.join(BASE, pather, folder, file)
        RUTA = os.path.normpath(RUTA)
        return RUTA

    @classmethod
    def leer_token(cls, file: str) -> str:
        ruta = cls.paths_file('..', 'key', file)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            token = archivo.read().strip()
            return token

    @classmethod
    def _obtener(cls, env_var: str, archivo: str) -> str:
        """
        Primero intenta leer la variable de entorno (útil en Railway/producción).
        Si no existe, cae al archivo .txt local (útil en tu máquina).
        """
        valor = os.getenv(env_var)
        if valor:
            return valor.strip()
        return cls.leer_token(archivo)

    @classmethod
    def google_token(cls) -> str:
        return cls._obtener('GOOGLE_API_KEY', 'google_api.txt')

    @classmethod
    def google_search_engine(cls) -> str:
        return cls._obtener('GOOGLE_SEARCH_ENGINE', 'google_searchengine.txt')

    @classmethod
    def telegram_token(cls) -> str:
        return cls._obtener('TELEGRAM_TOKEN', 'telegram_token.txt')

# if __name__ == "__main__":
#    print(my_token.telegram_token())