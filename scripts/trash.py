import pickle
import pandas as pd

# Configure Pandas to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Carrega l'objecte Counts des del fitxer .p
file_path = './data/counts/counts_violence.p'
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
print("\nDataFrame complet:")
print(data_df)
