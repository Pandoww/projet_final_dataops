import pandas as pd
 
from mon_projet.utils.helpers import extraire, transformer, analyse

URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

def test_extract_returns_dataframe():
    df = extraire(URL)
    assert isinstance(df, pd.DataFrame)

def test_transform_converts_total_earnings():
    df = pd.DataFrame({"TOTAL EARNINGS": ["100", "abc", "200"]})
    df_clean = transformer(df)
    assert df_clean["TOTAL EARNINGS"].dtype == "float64"

def test_analyse_returns_dict():
    df = pd.DataFrame({"TOTAL EARNINGS": [100, 200, 300]})
    result = analyse(df)
    assert isinstance(result, dict)