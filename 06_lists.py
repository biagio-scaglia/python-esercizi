# Biagio qui. Oggi facciamo la spesa con le LISTE!

# Una lista è un contenitore ordinato di cose.
# Si usano le parentesi quadre [] e si separano gli elementi con la virgola.

spesa = ["Pane", "Latte", "Uova", "Biscotti (per Biagio)"]

print("Ecco la mia lista della spesa:")
print(spesa)

# Possiamo prendere un elemento specifico dicendo la sua posizione (indice).
# ATTENZIONE: In informatica si inizia a contare da 0!

print(f"La prima cosa da comprare è: {spesa[0]}")  # Pane
print(f"L'ultima cosa (la più buona) è: {spesa[3]}") # Piscotti

# Possiamo aggiungere cose alla lista con .append()
print("\nHo dimenticato la pasta! Aggiungiamola.")
spesa.append("Pasta")

print("Nuova lista:")
for prodotto in spesa:
    print(f"- {prodotto}")

# Biagio consiglia: le liste sono utilissime per raggruppare dati simili.
