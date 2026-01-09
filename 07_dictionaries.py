# Biagio qui. Oggi impariamo il vocabolario... i DIZIONARI!

# Se le liste sono ordinate (0, 1, 2...), i dizionari usano le ETICHETTE (Chiavi).
# Si usano le parentesi graffe {} e i due punti :

profilo_biagio = {
    "nome": "Biagio",
    "cognome": "Scaglia",
    "eta": 28,  # (non ditelo a nessuno)
    "hobby": "Insegnare Python"
}

print("Ecco la scheda di Biagio:")
print(profilo_biagio)

# Per leggere qualcosa, non usiamo numeri, ma la CHIAVE (l'etichetta).

print(f"Nome: {profilo_biagio['nome']}")
print(f"Hobby: {profilo_biagio['hobby']}")

# Possiamo aggiungere nuove informazioni facilmente:
print("\nAggiungo il cibo preferito...")
profilo_biagio["cibo"] = "Pizza"

print(f"Ora Biagio mangia: {profilo_biagio['cibo']}")

# I dizionari sono perfetti per descrivere oggetti con tante proprietà diverse.
