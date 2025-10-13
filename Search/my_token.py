import os


class My_Token:
    
    def __init__(self):
        pass
    
    @classmethod
    def paths_file(self, pather: str, folder: str, file: str) -> str:
        BASE = os.path.dirname(os.path.abspath(__file__))
        RUTA = os.path.join(BASE, pather, folder, file)
        RUTA = os.path.normpath(RUTA)
        return RUTA
    
    @classmethod
    def leer_Token(self, file: str) -> str:
        ruta = self.paths_file('..', 'key', file)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            token = archivo.read()
            return token
        
    @classmethod
    def google_Token(self) -> str:
        token = self.leer_Token('google_api.txt')
        return token
    
    @classmethod
    def google_search_engine(self) -> str:
        token = self.leer_Token('google_searchengine.txt')
        return token
        
    @classmethod
    def telegram_token(self) -> str:
        token = self.leer_Token('telegram_token.txt')
        return token
# if __name__ == "__main__":
#    My_Token = My_Token.telegram_token()
#    print(My_Token)