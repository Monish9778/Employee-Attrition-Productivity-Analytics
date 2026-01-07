import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # Convert Attrition to binary
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
    
    # Check missing values
    df = df.dropna()
    
    return df
