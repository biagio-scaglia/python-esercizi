# Biagio qui. La vita è fatta di scelte... e anche Python!

# Usiamo 'if' (se) e 'else' (altrimenti) per far prendere decisioni al programma.
# ATTENZIONE: In Python gli spazi sono IMPORTANTI. Si chiama "indentazione".
# Tutto quello che deve succedere "se" è vero, deve essere spostato a destra.

energia = 80

print(f"Livello energia: {energia}")

if energia > 50:
    # Notate lo spazio vuoto all'inizio di questa riga? È fondamentale!
    print("Sei carico! Vai a programmare!")
    print("Puoi fare grandi cose oggi.")
else:
    # Anche qui, indentazione!
    print("Forse è meglio se ti prendi un caffè...")

# Se sbagliate gli spazi, Python si arrabbia e vi dà errore (IndentationError).

print("Fine del controllo.")

# Provate a cambiare 'energia' a 20 e vedete che succede!
