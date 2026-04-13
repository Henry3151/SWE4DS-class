# dataloader.py
import pandas as pd

# URL do dataset
DATASET_URL = "https://exemplo.com/dados.csv"

def carregar_dados():
    DATASET_URL = "https://exemplo.com/dados.zip"
    df = pd.read_csv(DATASET_URL)
    return df