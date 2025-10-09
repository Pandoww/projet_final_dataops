from projet_final.projet_final_dataops.mon_projet.utils.helpers import extract_boston_salary, transform, load, analyse

URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

df = extract_boston_salary(URL)
df_clean = transform(df)
load(df_clean)
resultats = analyse(df_clean)

print("Analyse des salaires de Boston (2018) :")
print(resultats)
