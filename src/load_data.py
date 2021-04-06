# impot modules for data
import pandas as pd
import numpy as np

df = pd.read_csv("/home/apprenant/simplon_project/bike_renting/data/vlib.csv")

#################################################################################
"""Sélection des colonnes """
print(df.head())
print(df.columns)
df = df["datetime","season", "holiday", "workingday", "weather", "temp" , "atemp", "humidity", "windspeed", "count"]

"""je ne prends pas en compte les colonnes casual et registered car la colonne count et la somme de ces deux colonnes"""
 #################################################################################
 