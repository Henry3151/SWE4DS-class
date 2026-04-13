# dataloader.py
import pandas as pd

# URL primária do dataset
DATASET_URL_PRIMARY = "https://exemplo.com/dados.zip"

# URL de fallback do dataset
DATASET_URL_FALLBACK = "https://exemplo.com/dados.csv"

# URL em uso
DATASET_URL = DATASET_URL_PRIMARY

def carregar_dados():
    df = pd.read_csv(DATASET_URL)
    return df