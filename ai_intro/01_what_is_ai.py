# Biagio qui. Benvenuti nel futuro... L'INTELLIGENZA ARTIFICIALE!
# Ma cos'è l'IA? Non è magia, è matematica.

# 1. Programmazione Classica (Come il cane addestrato)
# TU devi dare le regole.
def cane_robot_classico(ordine):
    if ordine == "seduto":
        return "Mi siedo"
    else:
        return "Non capisco"

print("--- Robot Classico ---")
print(cane_robot_classico("seduto")) # Funziona perché l'ho programmato io.
print(cane_robot_classico("salta"))  # Non sa cosa fare!

# 2. Intelligenza Artificiale (Come il bambino che impara)
# TU dai gli ESEMPI, lui impara le REGOLE.
# (Ovviamente qui simuliamo, non è una vera rete neurale complessa!)

esempi = {
    "seduto": "Mi siedo",
    "basso": "Mi siedo", # Impara che parole simili vogliono dire la stessa cosa
    "giù": "Mi siedo"
}

def cane_robot_ai(ordine):
    # Cerca se conosce l'ordine o qualcosa di simile dei suoi esempi
    if ordine in esempi:
        return esempi[ordine]
    else:
        return "Devo imparare questo nuovo comando..."

print("\n--- Robot AI (Simulato) ---")
print(cane_robot_ai("giù")) # Capisce anche "giù" perché l'ha "imparato" dai dati.

# Biagio dice: L'IA non è intelligente come noi, ma è molto brava a copiare dagli esempi!
