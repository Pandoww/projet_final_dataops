from mon_projet.utils.helpers import extraire, transformer, load, analyse

URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"


df = extraire(URL)
print("Nombre de lignes extraites :", len(df))

df_clean = transformer(df)
print("Nombre de lignes après nettoyage :", len(df_clean))
    
load(df_clean)
print("Fichier CSV créé : salaires_boston.csv")

resultats = analyse(df_clean)
print("Analyse des salaires de Boston (2018) :")
print(resultats)

