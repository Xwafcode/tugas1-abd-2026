import os
import pandas as pd
from datasets import load_dataset

def download_dataset():
    print("Downloading dataset from HuggingFace...")
    # Using the indonesia-affordable-housing dataset
    ds = load_dataset('web3hungry/indonesia-affordable-housing', split='train')
    
    df = ds.to_pandas()
    
    # Save to data directory
    output_path = '../data/indonesia_housing_data.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"Dataset downloaded successfully. Total rows: {len(df)}")
    print(f"Saved to: {output_path}")

if __name__ == '__main__':
    download_dataset()
