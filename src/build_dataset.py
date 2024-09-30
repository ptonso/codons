

import subprocess
import zipfile
import os

def build_dataset():
    data_path = "./data/raw.csv"
    os.makedirs(os.path.dirname(data_path), exist_ok=True)

    if not data_path.endswith(".csv"):
        raise ValueError("The data_path should be a .csv file")

    subprocess.run(["kaggle", "datasets", "download", "-d", "salikhussaini49/codon-usage", "-p", os.path.dirname(data_path)])

    zip_path = os.path.join(os.path.dirname(data_path), "codon-usage.zip")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(data_path))

    extracted_file = [f for f in os.listdir(os.path.dirname(data_path)) if f.endswith(".csv")][0]
    os.rename(os.path.join(os.path.dirname(data_path), extracted_file), data_path)

    os.remove(zip_path)