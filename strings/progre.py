import spacy

# Carga el modelo de lenguaje en español de spacy
nlp = spacy.load("es_core_news_sm")

# Función que cambia del lenguaje hetero-patriarcal a lenguaje progresista
def traducir_a_progre(cadena):
    # Separa la cadena en palabras
    palabras = cadena.split()

    # Lista para almacenar las palabras modificadas
    palabras_modificadas = []

    # Reemplaza la ultima vocal de cada palabra y la agrega a la lista
    for palabra in palabras:
        token = nlp(palabra)

        print({"pos":token[0].pos_, "tag_": token[0].tag_, "text": token[0].text})

        if token[0].pos_ == "ADJ":
            palabras_modificadas.append(reemplazar_vocal(palabra))
        else:
            palabras_modificadas.append(palabra)

    # Une las palabras modificadas en una nueva cadena
    return ' '.join(palabras_modificadas)

# Función para encontrar la ultima vocal en una palabra y reemplazarla por e
def reemplazar_vocal(word):
    for i in range(len(word) - 1, -1, -1):
        if word[i] in "aeiouáéíóúüAEIOUÁÉÍÓÚÜ":
            return f"{word[:i]}e{word[i+1:]}"
    return word

cadena = input("Inresa una cadena de texto: ")
print(traducir_a_progre(cadena))