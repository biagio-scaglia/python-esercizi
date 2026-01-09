# Biagio qui. Siete stanchi di copiare e incollare codice? Usiamo i CILCI (Loops)!

# 1. Il ciclo FOR (Per ogni...)
# Serve quando sapete quante volte volete fare qualcosa.

print("--- Ciclo FOR ---")
for numero in range(5):
    # 'range(5)' crea i numeri da 0 a 4.
    print(f"Sto contando: {numero}")
    print("Biagio sta lavorando...")

# 2. Il ciclo WHILE (Finché...)
# Serve quando non sapete quante volte, ma sapete quando smettere.

print("\n--- Ciclo WHILE ---")
fame = 3
while fame > 0:
    print(f"Ho ancora fame! Livello: {fame}")
    print("Mangio un panino...")
    fame = fame - 1 # Importante! Sennò Biagio mangia all'infinito (Loop Infinito)

print("Ora sono sazio!")

# Ricordate sempre l'indentazione (gli spazi) per dire cosa sta DENTRO al ciclo.
