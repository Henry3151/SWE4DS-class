# dataloader.py
import pandas as pd

# URL do dataset
DATASET_URL = "https://exemplo.com/dados.xls"

def carregar_dados():
    df = pd.read_csv(DATASET_URL)
    return df