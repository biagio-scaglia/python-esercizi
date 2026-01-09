# Biagio qui. Excel è bello, ma Pandas è SUPERPOTENTE!
# Pandas serve per manipolare dati in tabelle chiamate "DataFrame".

# ATTENZIONE: Per usare questo file dovete installare pandas:
# pip install pandas

import pandas as pd # "pd" è il soprannome che diamo a pandas.

# Creiamo una tabella (DataFrame) dai nostri dati
dati = {
    "Nome": ["Biagio", "Anna", "Luca", "Giulia"],
    "Ruolo": ["Insegnante", "Studente", "Studente", "Esperta"],
    "Voto": [10, 8, 4, 9]
}

df = pd.DataFrame(dati)

print("--- Ecco la nostra tabella (DataFrame) ---")
print(df)

# Possiamo fare analisi velocissime!
print("\n--- Statistiche veloci (describe) ---")
print(df.describe()) # Ci dà media, minimo, massimo dei numeri

# Filtrare è facilissimo
print("\n--- Chi ha preso più di 6? ---")
promossi = df[df["Voto"] > 6]
print(promossi)

# Biagio dice: Con Pandas potete gestire milioni di righe in un secondo!
