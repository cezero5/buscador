from Search.my_token import My_Token
import os
import requests
import time;
#import pandas 

class Search:
    
    def __init__(self, query, _token, search_engine):
        self.query = query
        self._token = _token
        self.search_engine = search_engine
        self.search_result = []
        self.base_url = 'https://www.googleapis.com/customsearch/v1'
        
    def google_search(self, start=1, num=10, lr="lang_es"):
        params = {
            'key': self._token,
            'cx': self.search_engine,
            'q': self.query,
            'start': start,      # 1, 11, 21, ...
            'num': num,          # max 10
            'lr': lr
        }
        return requests.get(self.base_url, params=params, timeout=20)
    
    def custom_results(self, results):
        out = []
        for r in results or []:
            out.append({
                "title": r.get("title", ""),
                "description": r.get("snippet", ""),
                "link": r.get("link", "")
            })
        return out
    
    def format_info(self, start=1, max_items=30, retries=0):
        # condición base: ya pedimos lo necesario
        if start > max_items:
            return self.search_result

        resp = self.google_search(start=start)
        if resp.status_code == 200:
            data = resp.json()
            items = data.get('items', []) or []
            # si ya no hay más items, corta
            if not items:
                return self.search_result

            self.search_result.extend(self.custom_results(items))
            # siguiente página
            return self.format_info(start=start + 10, max_items=max_items, retries=0)

        # backoff para 429
        if resp.status_code == 429 and retries < 3:
            wait = 5 * (retries + 1)
            time.sleep(wait)
            return self.format_info(start=start, max_items=max_items, retries=retries + 1)

        # otros errores: levanta con detalle
        try:
            err = resp.json().get("error", {})
            reasons = ", ".join([e.get("reason", "") for e in err.get("errors", [])])
            message = err.get("message", "")
        except Exception:
            reasons, message = "", resp.text
        raise Exception(f"HTTP {resp.status_code} – {reasons} – {message}")
        
    def safe_ascii(self, text):
        return ''.join(ch if ord(ch) < 128 else '' for ch in str(text or ""))
    
    def format_request(self, pages=1):
        """
        Devuelve un string listo para enviar por Telegram.
        pages=1 -> 10 resultados; pages=3 -> 30 resultados.
        """
        max_items = max(10, min(10 * pages, 100))  # tope 100
        if not self.search_result:
            self.format_info(start=1, max_items=max_items)

        if not self.search_result:
            return f"No encontré resultados para: {self.query}"

        lines = []
        for it in self.search_result:
            lines.append(
                "Titulo: " + self.safe_ascii(it.get('title')) + "\n"
                "Descripcion: " + self.safe_ascii(it.get('description')) + "\n"
                "Link: " + self.safe_ascii(it.get('link')) + "\n"
            )
        text = "\n".join(lines).strip()
        return text or f"No encontré resultados para: {self.query}"
        
# if __name__ == "__main__":
#     searcher = Search('Cesar Eduardo Mejia', My_Token.google_Token(), My_Token.google_search_engine())
#     # result = searcher.format_info(1)
#     print(f'------------------------------\n {searcher.format_request()} \n--------------------------------')