# Biagio qui. Oggi impariamo a mettere ordine con le FUNZIONI!

# Immaginate di dover pulire la stanza ogni giorno.
# Invece di dirvi ogni volta: "alza le calze", "fai il letto", "apri la finestra"...
# Dico solo: "pulisci_stanza()".

# Ecco come si crea una funzione "magica":
def saluta_biagio(nome):
    # Tutto quello che è indentato fa parte della funzione.
    print(f"Ciao {nome}! Benvenuto nel corso di Biagio.")
    print("Spero che ti stia piacendo Python.")

# Abbiamo creato la funzione, ma non succede niente finché non la chiamiamo!
# Eccola in azione:

print("--- Inizio del programma ---")

saluta_biagio("Luigi")
saluta_biagio("Mario")
saluta_biagio("Tutti voi")

print("--- Fine del programma ---")

# Le funzioni sono utilissime per non riscrivere lo stesso codice mille volte.
# Ricordate: define (def) una volta, usate (call) quante volte volete!
