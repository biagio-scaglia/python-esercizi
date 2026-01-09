# Biagio qui. Non reinventiamo la ruota, usiamo la FERRARI!
# Nel mondo reale, nessuno scrive neuroni a mano. Usiamo le LIBRERIE.

# Le "Big Three" dell'AI:
# 1. Scikit-Learn (Sklearn): Perfetta per iniziare, Matematica e Statistica. (Quella che usiamo oggi)
# 2. TensorFlow (Google): Potente, usata nelle aziende giganti.
# 3. PyTorch (Facebook): Flessibile, amata dai ricercatori.

# ATTENZIONE: Installate scikit-learn con: pip install scikit-learn

print("--- Esempio con Scikit-Learn ---")
print("Immaginiamo di voler prevedere il prezzo di una pizza in base al diametro.")

# Importiamo il modello di "Regressione Lineare" (Tira una linea dritta tra i punti)
from sklearn.linear_model import LinearRegression
import numpy as np

# DATI DI ESEMPIO (Diametro in cm -> Prezzo in €)
# Scikit-learn vuole i dati in colonna, quindi usiamo [[...], [...]]
X_diametro = [[20], [30], [40], [50]] 
y_prezzo =   [5,    8,    11,   14]  # I prezzi veri

# Creiamo il "Cervello" (Modello)
modello = LinearRegression()

# Lo ADDESTRIAMO (Fit)
print("Addestramento in corso...")
modello.fit(X_diametro, y_prezzo)
print("Fatto!")

# ORA FACCIAMO PREVISIONI (Predict)
pizza_gigante = [[60]]
prezzo_previsto = modello.predict(pizza_gigante)

print(f"Se una pizza è grande 60cm, secondo l'AI dovrebbe costare: {prezzo_previsto[0]:.2f} €")

# Biagio dice: Avete appena creato un modello predittivo. Siete ufficialmente pericolosi!
