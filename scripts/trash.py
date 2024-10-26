import pickle
import pandas as pd

# Carrega l'objecte Counts des del fitxer .p
file_path = './data/counts/counts_test.p'
with open(file_path, 'rb') as file:
    counts = pickle.load(file)

# Mostra informació general de l'objecte
print("Objecte carregat:", type(counts))

# Accedeix als termes de les dimensions A i B
print("Terms (dim A):", counts.terms['A'].labels)  # Mostra els termes de la dimensió A
print("Terms (dim B):", counts.terms['B'].labels)  # Mostra els termes de la dimensió B

# Obtenim la matriu de comptes directament amb l'atribut counts
data = counts.counts

# Converteix les dades en un DataFrame per a visualitzar-les
data_df = pd.DataFrame(data, index=counts.terms['A'].labels, columns=counts.terms['B'].labels)
print("\nPrimeres files del DataFrame:")
print(data_df.head())