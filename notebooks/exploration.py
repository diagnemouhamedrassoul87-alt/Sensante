import pandas as pd

# Charger les données
df = pd.read_csv("data/patients_dakar.csv")

print("=" * 50)
print("SENSANTE - Exploration du dataset")
print("=" * 50)

# Dimensions
print(f"\nNombre de patients : {len(df)}")
print(f"Nombre de colonnes : {df.shape[1]}")
print(f"Colonnes : {list(df.columns)}")

# Aperçu
print("\n--- 5 premiers patients ---")
print(df.head())

# Statistiques
print("\n--- Statistiques descriptives ---")
print(df.describe().round(2))

# Répartition des diagnostics
print("\n--- Répartition des diagnostics ---")
diag_counts = df["diagnostic"].value_counts()

for diag, count in diag_counts.items():
    pct = count / len(df) * 100
    print(f"{diag} : {count} patients ({pct:.1f}%)")

# Température moyenne
print("\n--- Température moyenne par diagnostic ---")
temp_by_diag = df.groupby("diagnostic")["temperature"].mean()

for diag, temp in temp_by_diag.items():
    print(f"{diag} : {temp:.1f} °C")

print("\nExploration terminée !")
print("\n--- Répartition par sexe et diagnostic ---")

group = df.groupby(["sexe", "diagnostic"]).size()

for (sexe, diag), count in group.items():
    print(f"Sexe: {sexe} | Diagnostic: {diag} → {count} patients")