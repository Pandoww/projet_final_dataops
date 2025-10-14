import json
import urllib.request
import pandas as pd
import numpy as np

def extraire(url: str) -> pd.DataFrame:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    records = data["result"]["records"]
    return pd.DataFrame(records)

def transformer(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et transforme les données de salaires."""
    df = df.copy()

    # Vérifie que la colonne existe bien
    if "TOTAL EARNINGS" not in df.columns:
        print("⚠️ Colonne 'TOTAL EARNINGS' introuvable !")
        print("Colonnes disponibles :", df.columns)
        return pd.DataFrame()

    # Nettoie les valeurs : enlève $, , et espaces
    df["TOTAL EARNINGS"] = (
        df["TOTAL EARNINGS"]
        .astype(str)
        .str.replace(r"[\$,]", "", regex=True)
        .str.strip()
    )

    # Convertit en nombres
    df["TOTAL EARNINGS"] = pd.to_numeric(df["TOTAL EARNINGS"], errors="coerce")

    # Supprime les lignes vides
    df = df.dropna(subset=["TOTAL EARNINGS"])

    # Convertit en float64 propre
    df["TOTAL EARNINGS"] = df["TOTAL EARNINGS"].astype("float64")

    return df

def load(df: pd.DataFrame, filename: str = "salaires_boston.csv") -> None:
    df.to_csv(filename, index=False)

def analyse(df: pd.DataFrame):
    stats = df["TOTAL EARNINGS"].describe()
    return stats.to_dict()
