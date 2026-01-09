# Biagio qui. Benvenuti nel laboratorio di DATA SCIENCE!
# Data Science = Usare i dati per capire il mondo (o per vincere al fantacalcio).

# Python ha uno strumento molto utile già pronto: 'statistics'.
import statistics

# Immaginiamo i voti di un esame di Python (speriamo siano alti!)
voti = [6, 7, 8, 9, 6, 10, 5, 7, 8, 9, 9]

print(f"Ecco i voti della classe: {voti}")

# 1. La MEDIA (Mean): la somma diviso il numero totali.
media = statistics.mean(voti)
print(f"La media dei voti è: {media}")

# 2. La MEDIANA (Median): il valore che sta esattamente nel mezzo.
mediana = statistics.median(voti)
print(f"La mediana è: {mediana}")

# 3. La MODA (Mode): il valore che compare più volte.
moda = statistics.mode(voti)
print(f"Il voto più comune (Moda) è: {moda}")

# Biagio dice: Con queste tre cose potete già fare bella figura nelle riunioni!
