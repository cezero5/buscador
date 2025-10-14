class query:
    def __init__(self, chat_text):
        self.chat_text = chat_text
        
    def arguments_flag(self):
        opcion = []
        flag_map = {
            '-d=': lambda v: opcion.append(f'site:{v}'),
            '-ft=': lambda v: opcion.append(f'filetype:{v}'),   # lógica para -ft=
            '-it=': lambda v: opcion.append(f'intitle:{v}'),   # lógica para -it=
            '-ait=': lambda v: opcion.append(f'allintile{v}'),  # lógica para -ait=
            '-we=': lambda v: opcion.append(f'"{v}"'),   # lógica para -we=
            '-e=': lambda v: opcion.append(f'-{v}'),    # lógica para -e=
            '-or=': lambda v: opcion.append(f'or {v}'),   # lógica para -or=
        }
        flags = sorted(flag_map.keys(), key=len, reverse=True)

        for tok in self.chat_text:
            # detectar si el token comienza con alguna flag (solo una vez por token)
            match = next((f for f in flags if isinstance(tok, str) and tok.startswith(f)), None)

            if match:
                rest = tok[len(match):]  # lo que viene después de la flag
                # si hay valores separados por comas los procesamos
                if rest:
                    for v in rest.split(','):
                        v = v.strip()
                        if v:  # ignorar entradas vacías
                            flag_map[match](v)
                # NO añadimos el token original a `opcion` (porque ya añadimos la transformación)
                continue

            # si no es una flag, lo añadimos tal cual
            opcion.append(tok)

        return opcion

    def query_format(self, _text:str =''):
        for i in self.arguments_flag():
            _text += i + ' '
        return _text
# if __name__ == '__main__':
#     bot = query(['fdsfasdf','-d=linkedl.com,facebook.com','asfsdff','-or=felipe,mejia','-ait=','asdfsdaf'])
#     print(bot.query_format())