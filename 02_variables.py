# Biagio qui. Oggi parliamo di Scatole... ehm, Variabili!

# Una variabile è come una scatola dove ci metti dentro qualcosa per dopo.
# In Python non serve dire "che tipo di scatola è" (tipo int, string), lui capisce!

messaggio = "Ciao a tutti" # Questa è una stringa (testo)
numero_intero = 10         # Questo è un numero intero (int)
numero_virgola = 3.14      # Questo è un numero con la virgola (float)

print("Ecco cosa c'è nelle scatole:")
print(messaggio)
print(numero_intero)
print(numero_virgola)

# Possiamo anche cambiare il contenuto!
messaggio = "Ho cambiato idea!"
print(messaggio)

# E possiamo fare matematica con i numeri
somma = numero_intero + 5
print("10 + 5 fa:")
print(somma)

# Biagio trick: potete unire testo e variabili con la f-string (la f sta per... formattazione? Forse, o Fantastico)
print(f"Il mio numero preferito è {numero_intero} e mi piace il {numero_virgola}")
