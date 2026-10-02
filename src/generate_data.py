import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_indonesia_sales_data(num_rows, output_path):
    print(f"Generating {num_rows} rows of data...")
    provinces = ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'Jawa Timur', 'Banten', 'Sumatera Utara', 'Sulawesi Selatan', 'Bali', 'Kalimantan Timur', 'Papua']
    categories = ['Elektronik', 'Pakaian', 'Makanan', 'Minuman', 'Perabotan', 'Kosmetik']
    
    start_date = datetime(2023, 1, 1)
    
    # Generate in chunks to save memory
    chunk_size = 100000
    
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
        
    first_chunk = True
    
    for i in range(0, num_rows, chunk_size):
        current_chunk_size = min(chunk_size, num_rows - i)
        
        dates = [start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59)) for _ in range(current_chunk_size)]
        
        data = {
            'transaction_id': range(i + 1, i + current_chunk_size + 1),
            'timestamp': dates,
            'province': np.random.choice(provinces, current_chunk_size),
            'product_category': np.random.choice(categories, current_chunk_size),
            'quantity': np.random.randint(1, 10, current_chunk_size),
            'unit_price': np.random.randint(10, 1000, current_chunk_size) * 1000,
            'discount': np.random.choice([0, 0.1, 0.2, 0.5], current_chunk_size, p=[0.7, 0.15, 0.1, 0.05])
        }
        
        df = pd.DataFrame(data)
        df['total_sales'] = df['quantity'] * df['unit_price'] * (1 - df['discount'])
        
        # Introduce some missing values for data cleaning milestone
        mask_province = np.random.rand(current_chunk_size) < 0.02 # 2% missing
        df.loc[mask_province, 'province'] = np.nan
        
        mask_category = np.random.rand(current_chunk_size) < 0.01 # 1% missing
        df.loc[mask_category, 'product_category'] = np.nan
        
        mode = 'w' if first_chunk else 'a'
        header = first_chunk
        
        df.to_csv(output_path, mode=mode, header=header, index=False)
        first_chunk = False
        print(f"Generated {i + current_chunk_size} rows")

if __name__ == '__main__':
    # Generate 1.2 million rows (satisfies > 1 juta baris requirement)
    output_file = '../data/indonesia_sales_data.csv'
    generate_indonesia_sales_data(1200000, output_file)
    print(f"Data saved to {output_file}")
