import pandas as pd

df = pd.read_csv("sample_gene_expression.csv")

df["Average_Expression"] = df.iloc[:, 1:].mean(axis=1)

df = df.dropna(subset=[df.columns[0]])

top_10 = df.sort_values("Average_Expression", ascending=False).head(10)

print("Top 10 Expressed Genes:")
print(top_10[[df.columns[0], "Average_Expression"]])
