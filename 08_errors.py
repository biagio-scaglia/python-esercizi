# Biagio qui. A volte le cose vanno male... ma Python ci salva!

# Immaginate di dover dividere un numero per... zero!
# In matematica esplode tutto. In Python possiamo "provare" (try) a farlo.

print("Proviamo a fare una divisione pericolosa...")

try:
    # Qui mettiamo il codice "rischioso"
    numero = 10
    divisore = 0
    risultato = numero / divisore
    print(f"Il risultato è: {risultato}")

except ZeroDivisionError:
    # Qui mettiamo cosa fare se succede il disastro (l'errore specifico)
    print("ERRORE! Non puoi dividere per zero, Biagio!")

except Exception as e:
    # Questo cattura qualsiasi altro errore
    print(f"È successo un altro errore: {e}")

# Il programma continua lo stesso! Non si blocca.
print("Il programma è finito sano e salvo.")

# Biagio dice: Meglio prevenire che curare, ma 'try-except' è come un airbag!
