import pandas as pd
import numpy as np


def run_aminoCluster(df, dict_amino):

    df_amino = df[['Ncodons']].copy()
    aminos = list(dict_amino.keys())

    for amino, codons in dict_amino.items():

        amino_df = df[codons]
        # amino_sum = (amino_df.mul(df["Ncodons"], axis=0)).sum(axis=1)
        amino_sum = amino_df.sum(axis=1)
        df_amino[amino] = amino_sum
        sorted_df = df_amino.copy()

        
    sorted_df['Row_Sum'] = df_amino[aminos].sum(axis=1)
    df_amino = sorted_df.sort_values(by='Row_Sum', ascending=False)
    df_amino = df_amino.drop("Row_Sum",axis=1)

    return df_amino