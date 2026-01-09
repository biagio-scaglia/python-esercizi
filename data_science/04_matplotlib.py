# Biagio qui. Diamo un po' di COLORE ai numeri!
# Matplotlib serve per fare grafici (plotting).

# ATTENZIONE: Per usare questo file dovete installare matplotlib:
# pip install matplotlib

import matplotlib.pyplot as plt # "plt" è il pennello di Biagio

# Dati da disegnare
mesi = ["Gen", "Feb", "Mar", "Apr", "Mag"]
vendite = [10, 20, 15, 30, 45]

print("Sto disegnando il grafico...")

# 1. Grafico a LINEA (Line Plot)
plt.figure() # Foglio nuovo
plt.plot(mesi, vendite, marker='o', color='red', linestyle='--')
plt.title("Vendite del Negozio di Biagio")
plt.xlabel("Mesi")
plt.ylabel("Soldi (€)")
plt.grid(True) # Mettiamo la griglia per capire meglio

# Per salvare il grafico in un'immagine:
plt.savefig('grafico_vendite.png')
print("Grafico salvato come 'grafico_vendite.png'!")

# 2. Grafico a BARRE (Bar Chart)
nomi = ["Biagio", "Anna", "Luca"]
punteggi = [100, 85, 90]

plt.figure() # Altro foglio nuovo
plt.bar(nomi, punteggi, color=['blue', 'pink', 'green'])
plt.title("Gara di Programmazione")
plt.savefig('grafico_barre.png')
print("Grafico a barre salvato come 'grafico_barre.png'!")

# Se state usando il computer di casa, potete anche usare plt.show() per vederlo subito.
# plt.show()

# Biagio dice: Un bel grafico vale più di mille print!
