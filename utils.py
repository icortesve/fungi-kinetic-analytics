import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def analizar_fermentacion(csv_path):
    df = pd.read_csv(csv_path)
    X = df[['tiempo']]
    y = df['biomasa']
    modelo = LinearRegression().fit(X, y)
    
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    sns.scatterplot(data=df, x='tiempo', y='biomasa', color='#2ecc71', s=100, label='Real')
    sns.lineplot(x=df['tiempo'], y=modelo.predict(X), color='#34495e', linewidth=2.5, label='Modelo')
    
    plt.title('Dinámica de crecimiento micelial', fontsize=16, fontweight='bold')
    plt.xlabel('Tiempo (h)'); plt.ylabel('Biomasa (g/L)')
    sns.despine()
    plt.show()