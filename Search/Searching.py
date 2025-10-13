from my_token import My_Token
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
        
    def google_search(self, start= 1):
        params = {
            'key': self._token,
            'cx': self.search_engine,
            'q': self.query,
            'start': start,
            'lr': "lang_us"
        }
        response = requests.get(self.base_url, params=params)
        return response
    
    def custom_results(self, results):
        custom_results = []
        for result in results:
            cresult = {
                "title": result.get("title"),
                "description": result.get("snippet"),
                "link": result.get("link")
            }
            custom_results.append(cresult)
        return custom_results
    
    def format_info(self, number, retries= 0):
        try:
            if (number % 10 == 0 and number <= 100):
                search = Search(self.query, self._token, self.search_engine)
                response = search.google_search()
                print('\n')
                if(response.status_code == 200):
                    response = response.json()
                    items = response.get('items', [])
                    cresults = self.custom_results(items)
                    self.search_result.extend(cresults)
                    self.format_info(number + 1)
                else:
                    error_msg = f"Error obtaining page 1: HTTP {response.status_code}"
                    print(error_msg)
                    raise Exception(error_msg)
                return self.search_result
            elif number < 100:
                    self.format_info((number + 1))
        except Exception as e:
            if "HTTP 429" in str(e):
                if retries < 3:
                    print("Demasiadas peticiones, esperando 5 segundos...")
                    time.sleep(5)
                    return self.format_info(number, retries + 1)
                else:
                    raise Exception("Demasiados intentos fallidos por HTTP 429")
            
            else:
                raise
        
    def format_request(self, number):
        list_format = self.format_info
        if((len(list_format) - number) >= 0):
            print(f"📰 {list_format['title']}")
            print(f"📝 {list_format['description']}")
            print(f"🔗 {list_format['link']}\n")
            number += 1
        else:
            self.format_request(number + 1)
            
if __name__ == "__main__":
    searcher = Search('RocketLeague', My_Token.google_Token(), My_Token.google_search_engine())
    # result = searcher.format_info(1)
    print(f'------------------------------\n {searcher.format_info(number = 1)} \n--------------------------------')