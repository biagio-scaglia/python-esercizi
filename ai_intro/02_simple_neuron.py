# Biagio qui. Costruiamo un CERVELLO (partendo da un neurone)!

# Un neurone artificiale fa una cosa semplice:
# Input (Ingredienti) * Pesi (Importanza) -> Somma -> Decisione

# Immaginiamo un neurone che deve decidere: "Biagio mangia la pizza?"
# Input:
fame = 1      # 1 = Sì, 0 = No
soldi = 1     # 1 = Sì, 0 = No
dieta = 0     # 1 = A dieta, 0 = No

# Pesi (Quanto contano questi fattori per Biagio?)
peso_fame = 5     # La fame conta tanto!
peso_soldi = 2    # I soldi contano, ma meno.
peso_dieta = -5   # La dieta è negativa per la pizza!

print("--- Il Neurone di Biagio sta pensando... ---")

# Calcolo "attivazione" (Somma pesata)
attivazione = (fame * peso_fame) + (soldi * peso_soldi) + (dieta * peso_dieta)

print(f"Livello di voglia di pizza: {attivazione}")

# Soglia di attivazione (Quanto basta per dire SI?)
soglia = 4

if attivazione > soglia:
    print("OUTPUT: 1 (SI! Biagio mangia la pizza!)")
else:
    print("OUTPUT: 0 (No... niente pizza oggi.)")

# Biagio dice: Le Reti Neurali sono milioni di questi calcoli tutti insieme!
