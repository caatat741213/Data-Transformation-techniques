import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs

# Centralized seed control
GLOBAL_SEED = 888 

def generate_dtt_dataset(n_samples=1000, random_state=GLOBAL_SEED):
    """
    Generates a comprehensive dataset for practicing 10 Data Transformation Techniques.
    """
    # Use the passed random_state to ensure reproducibility
    np.random.seed(random_state)
    
    # 1. Numerical data for Normalization (Min-Max, Z-Score)
    salary = np.random.normal(50000, 15000, n_samples)
    age = np.random.randint(20, 65, n_samples)
    
    # 2. Highly skewed data for Distribution Fitting (Box-Cox)
    # Adding +1 to ensure all values are positive for Box-Cox
    household_size = np.random.exponential(scale=2, size=n_samples) + 1
    
    # 3. Categorical data for Encoding and Concept Hierarchies
    education_levels = ['High School', 'Bachelor', 'Master', 'PhD']
    regions = ['North', 'South', 'East', 'West']
    edu_data = np.random.choice(education_levels, n_samples)
    region_data = np.random.choice(regions, n_samples)
    
    # 4. Clustered data for Clustering & Visualization
    X_clusters, _ = make_blobs(n_samples=n_samples, 
                               centers=3, 
                               n_features=2, 
                               random_state=random_state)
    
    df = pd.DataFrame({
        'Age': age,
        'Annual_Salary': salary,
        'Household_Size': household_size,
        'Education_Level': edu_data,
        'Region': region_data,
        'Cluster_Feature_1': X_clusters[:, 0],
        'Cluster_Feature_2': X_clusters[:, 1],
        'Transaction_Amount': np.random.lognormal(mean=3, sigma=1, size=n_samples)
    })
    
    # Add outliers for EDA testing
    df.loc[0:5, 'Annual_Salary'] = df['Annual_Salary'].max() * 3
    
    return df

if __name__ == "__main__":
    data = generate_dtt_dataset()
    print(f"Dataset generated with GLOBAL_SEED={GLOBAL_SEED}")
    print(data.head())