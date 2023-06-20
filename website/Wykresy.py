import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('auta.csv', delimiter=';')
df.dropna()

def W1():   # Benzyna
    nazwa = df['Nazwa'].iloc[1:]
    b18 = df[df.columns[df.columns.str.contains('samochody osobowe;benzyna;2018;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b19 = df[df.columns[df.columns.str.contains('samochody osobowe;benzyna;2019;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b20 = df[df.columns[df.columns.str.contains('samochody osobowe;benzyna;2020;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b21 = df[df.columns[df.columns.str.contains('samochody osobowe;benzyna;2021;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]


    width = 0.2
    offset = 0.2
    plt.bar(np.arange(len(nazwa)) - offset, b18, width=width, label ='2018')
    plt.bar(np.arange(len(nazwa)) + width - offset, b19, width=width, label='2019')
    plt.bar(np.arange(len(nazwa)) + 2 * width - offset, b20, width=width, label='2020')
    plt.bar(np.arange(len(nazwa)) + 3 * width - offset, b21, width=width, label='2021')
    plt.title('Samochody osobowe na benzynę w poszczególnych województwach')
    plt.ylabel('Ilość samochodów')
    plt.xticks(np.arange(len(nazwa)) + width / 2, nazwa,rotation=80)
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.tight_layout()
    plt.legend()
    plt.show()


def W2():  # Diesel
    nazwa = df['Nazwa'].iloc[1:]
    b18 = df[df.columns[df.columns.str.contains('samochody osobowe;olej napędowy;2018;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b19 = df[df.columns[df.columns.str.contains('samochody osobowe;olej napędowy;2019;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b20 = df[df.columns[df.columns.str.contains('samochody osobowe;olej napędowy;2020;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b21 = df[df.columns[df.columns.str.contains('samochody osobowe;olej napędowy;2021;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]


    width = 0.2
    offset = 0.2
    plt.bar(np.arange(len(nazwa)) - offset, b18, width=width, label ='2018')
    plt.bar(np.arange(len(nazwa)) + width - offset, b19, width=width, label='2019')
    plt.bar(np.arange(len(nazwa)) + 2 * width - offset, b20, width=width, label='2020')
    plt.bar(np.arange(len(nazwa)) + 3 * width - offset, b21, width=width, label='2021')
    plt.title('Samochody osobowe na olej napędowy w poszczególnych województwach')
    plt.ylabel('Ilość samochodów')
    plt.xticks(np.arange(len(nazwa)) + width / 2, nazwa,rotation=80)
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.tight_layout()
    plt.legend()
    plt.show()

def W3():  # LPG
    nazwa = df['Nazwa'].iloc[1:]
    b18 = df[df.columns[df.columns.str.contains('samochody osobowe;gaz \(LPG\);2018;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b19 = df[df.columns[df.columns.str.contains('samochody osobowe;gaz \(LPG\);2019;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b20 = df[df.columns[df.columns.str.contains('samochody osobowe;gaz \(LPG\);2020;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b21 = df[df.columns[df.columns.str.contains('samochody osobowe;gaz \(LPG\);2021;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]


    width = 0.2
    offset = 0.2
    plt.bar(np.arange(len(nazwa)) - offset, b18, width=width, label ='2018')
    plt.bar(np.arange(len(nazwa)) + width - offset, b19, width=width, label='2019')
    plt.bar(np.arange(len(nazwa)) + 2 * width - offset, b20, width=width, label='2020')
    plt.bar(np.arange(len(nazwa)) + 3 * width - offset, b21, width=width, label='2021')
    plt.title('Samochody osobowe na gaz(LPG) w poszczególnych województwach')
    plt.ylabel('Ilość samochodów')
    plt.xticks(np.arange(len(nazwa)) + width / 2, nazwa,rotation=80)
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.tight_layout()
    plt.legend()
    plt.show()

def W4():  # Pozostałe
    nazwa = df['Nazwa'].iloc[1:]
    b18 = df[df.columns[df.columns.str.contains('samochody osobowe;pozostałe;2018;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b19 = df[df.columns[df.columns.str.contains('samochody osobowe;pozostałe;2019;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b20 = df[df.columns[df.columns.str.contains('samochody osobowe;pozostałe;2020;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]
    b21 = df[df.columns[df.columns.str.contains('samochody osobowe;pozostałe;2021;')]].astype(str).apply(
        lambda x: pd.to_numeric(x.str.extract('(\d+)', expand=False), errors='coerce')).sum(axis=1).iloc[1:]


    width = 0.2
    offset = 0.2
    plt.bar(np.arange(len(nazwa)) - offset, b18, width=width, label ='2018')
    plt.bar(np.arange(len(nazwa)) + width - offset, b19, width=width, label='2019')
    plt.bar(np.arange(len(nazwa)) + 2 * width - offset, b20, width=width, label='2020')
    plt.bar(np.arange(len(nazwa)) + 3 * width - offset, b21, width=width, label='2021')
    plt.title('Samochody osobowe napędzane innym paliwem w poszczególnych województwach')
    plt.ylabel('Ilość samochodów')
    plt.xticks(np.arange(len(nazwa)) + width / 2, nazwa,rotation=80)
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)
    plt.tight_layout()
    plt.legend()
    plt.show()
