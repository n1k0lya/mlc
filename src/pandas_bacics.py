import pandas as pd

df = pd.read_csv(r"C:\vsproj\mlc\data\Titanic-Dataset.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isna().sum())

print(df.describe())

summa = df[(df["Age"]>60) & (df["Pclass"]==1)].shape[0]
count_60_1 = ((df["Age"] > 60) & (df["Pclass"] == 1)).sum()

print(summa)
print(count_60_1)

meanfare = df.groupby("Sex")["Fare"].mean()
print(meanfare)

survivedpeople = df.groupby("Sex")["Survived"].mean()
survivedpeopleclass = df.groupby("Pclass")["Survived"].mean()
survivedpeopletable = df.groupby(["Sex", "Pclass"])["Survived"].mean()

print(survivedpeople)
print(survivedpeopleclass)
print(survivedpeopletable)

print(pd.pivot_table(df, values="Survived", index="Sex", columns="Pclass", aggfunc = "mean"))