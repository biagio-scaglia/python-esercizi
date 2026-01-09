# Biagio qui. Oggi apriamo la CASSETTA DEGLI ATTREZZI!
# Ci sono alcuni strumenti che userete il 90% del tempo. Vediamoli.

oggetti = ["Martello", "Cacciavite", "Trapano"]

# 1. LEN (Length/Lunghezza)
# Serve per sapere "quanta roba c'è".
numero_oggetti = len(oggetti)
print(f"Nella cassetta ci sono {numero_oggetti} oggetti.")

nome = "Biagio"
lunghezza_nome = len(nome)
print(f"Il nome '{nome}' ha {lunghezza_nome} lettere.")

# 2. APPEND (Aggiungi in coda)
# Lo abbiamo visto con le liste, mette una cosa alla fine.
oggetti.append("Nastro adesivo")
print(f"Ora abbiamo: {oggetti}")

# 3. TYPE (Che cos'è?)
# Se non sapete cosa avete in mano, chiedete a Python.
print(f"Che tipo è 'oggetti'? {type(oggetti)}")
print(f"Che tipo è 'numero_oggetti'? {type(numero_oggetti)}")

# 4. CASTING (Trasformazione)
# A volte volete trattare un numero come testo o viceversa.
numero_testo = "50"
# calcolo = numero_testo + 10 # ERRORE! Non puoi sommare testo e numeri.

# Trasformiamo il testo in numero (int)
numero_vero = int(numero_testo)
risultato = numero_vero + 10
print(f"50 + 10 fa: {risultato}")

# Trasformiamo un numero in testo (str)
prezzo = 9.99
messaggio = "Il prezzo è " + str(prezzo) # Ora possiamo unirli
print(messaggio)

# Biagio dice: Questi attrezzi vi salveranno la vita ogni giorno!
