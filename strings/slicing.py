word = input("Ingresa una palabra: ")
start = input("¿Desde que letra deceas cortar la palabra? ") #Al principio start es de tipo string
start = word.find(start) # despues start se convierte en int

end = input("¿Hasta que letra deceas cortar la palabra? ")
end = word.find(end) + 1

print(f"Resultado: {word[start:end]}")
print(f"Resultado alreves: {word[start:end][::-1]}")


word.replace()