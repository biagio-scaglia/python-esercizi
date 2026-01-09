# Biagio qui. I dati veri sono costosi, usiamo quelli finti!
# Oggi impariamo a gestire un "dataset" (un insieme di dati) come veri Data Scientist.

# Creiamo una lista di dizionari. Ogni dizionario è una persona.
popolazione = [
    {"id": 1, "nome": "Mario", "eta": 25, "citta": "Roma"},
    {"id": 2, "nome": "Luigi", "eta": 30, "citta": "Milano"},
    {"id": 3, "nome": "Peach", "eta": 28, "citta": "Roma"},
    {"id": 4, "nome": "Toad", "eta": 15, "citta": "FungoLandia"},
    {"id": 5, "nome": "Bowser", "eta": 100, "citta": "Vulcano"}
]

print(f"Abbiamo analizzato {len(popolazione)} persone.")

# OBIETTIVO: Trovare tutte le persone che vivono a Roma.
print("\n--- Persone che vivono a Roma ---")

utenti_romani = []

for persona in popolazione:
    # Controlliamo la città
    if persona["citta"] == "Roma":
        utenti_romani.append(persona)
        print(f"Trovato: {persona['nome']}")

print(f"\nTotale Romani: {len(utenti_romani)}")

# OBIETTIVO: Calcolare l'età media (usiamo quello che abbiamo imparato prima!)
import statistics

# Creiamo una lista solo con le età (List Comprehension - Roba da Pro!)
lista_eta = [persona["eta"] for persona in popolazione] 
# (È un modo veloce per dire: prendi l'età PER ogni persona nella popolazione)

media_eta = statistics.mean(lista_eta)
print(f"\nEtà media della popolazione: {media_eta} anni")

# Biagio dice: I dati parlano, basta saperli ascoltare!
