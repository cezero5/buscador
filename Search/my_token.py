import os


class my_token:
    
    def __init__(self):
        pass
    
    @classmethod
    def paths_file(self, pather: str, folder: str, file: str) -> str:
        BASE = os.path.dirname(os.path.abspath(__file__))
        RUTA = os.path.join(BASE, pather, folder, file)
        RUTA = os.path.normpath(RUTA)
        return RUTA
    
    @classmethod
    def leer_token(self, file: str) -> str:
        ruta = self.paths_file('..', 'key', file)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            token = archivo.read()
            return token
        
    @classmethod
    def google_token(self) -> str:
        token = self.leer_token('google_api.txt')
        return token
    
    @classmethod
    def google_search_engine(self) -> str:
        token = self.leer_token('google_searchengine.txt')
        return token
        
    @classmethod
    def telegram_token(self) -> str:
        token = self.leer_token('telegram_token.txt')
        return token
# if __name__ == "__main__":
#    my_token = my_token.telegram_token()
#    print(my_token)