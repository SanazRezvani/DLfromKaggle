import os
import zipfile
import pandas as pd

# Define dataset information
dataset = ".../...."  # Replace with your dataset identifier
download_dir = "./data"  # Local directory to save the dataset

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

# Download the dataset
os.system(f"kaggle datasets download -d {dataset} -p {download_dir}")

# Unzip the dataset
zip_path = os.path.join(download_dir, ".....zip")  # Replace with your zip file name
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(download_dir)

# Load the CSV file into a DataFrame
csv_path = os.path.join(download_dir, ".....csv")  # Replace with your CSV file name
df = pd.read_csv(csv_path)

# Display the DataFrame
print(df.head())
