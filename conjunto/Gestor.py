import pandas as pd
def plan_estudio():
    columnas= ["Codigo","UC","Previa 1","Previa 2","Previa 3","Previa 4","Previa 5","Créditos"]
    df = pd.read_csv("Plan2021.csv", names=columnas, index_col=0)
    return df.fillna("No tiene")
