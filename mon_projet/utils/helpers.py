import json
import urllib.request
import pandas as pd
import numpy as np

def extract_boston_salary(url: str) -> pd.DataFrame:
    """Extrait les données brutes depuis l'API Boston."""
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    records = data["result"]["records"]
    return pd.DataFrame(records)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et transforme les données de salaires."""
    df["TOTAL EARNINGS"] = pd.to_numeric(df["TOTAL EARNINGS"], errors="coerce")
    df = df.dropna(subset=["TOTAL EARNINGS"])
    return df

def load(df: pd.DataFrame, filename: str = "boston_salaries_clean.csv") -> None:
    """Enregistre les données nettoyées dans un fichier CSV."""
    df.to_csv(filename, index=False)

def analyse(df: pd.DataFrame):
    """Réalise des calculs statistiques sur les salaires."""
    stats = df["TOTAL EARNINGS"].describe()
    return stats.to_dict()
