from collections import Counter
import math

text = "Python me gusta para empezar. Iniciemos:"
documentos = [
    ['python', 'es', 'genial'],
    ['python', 'para', 'principiantes'],
    ['javascript', 'para', 'principiantes']
]
out_text = '.,;:!?"()[]'
tokens = list()
def tokenizar(text) -> list[str]:
    result = text.lower()
    tabla = str.maketrans("", "", out_text)
    change_chrt = result.translate(tabla)
    lista = change_chrt.split(" ")
    return lista

def calcular_tf(tokens) -> dict:
    total = len(tokens)
    conteo = Counter(tokens) 
    return {x: y / total for x,y in conteo.items()}

def calcular_idf(documentos: list[list[str]]) -> dict:
    doc_total = len(documentos)
    documentos_unicos = list()
    for x in range(doc_total):
        documentos_unicos += set(documentos[x])
    conteo_df = Counter(documentos_unicos)
    return{ x: math.log((doc_total + 1) / (df + 1)) + 1 for x,df in conteo_df.items() }

def rankear(query: str, documentos: list[list[str]]) -> list:
    query_tokens = tokenizar(query)
    idf = calcular_idf(documentos)
    scores = []
    for doc in documentos:
        tf = calcular_tf(doc)
        score = 0
        for palabra in query_tokens:
            score += tf.get(palabra, 0) * idf.get(palabra, 0)
        scores.append((score, doc))
    return sorted(scores, key=lambda x: x[0], reverse=True)

#output
print(rankear("python principiantes", documentos))