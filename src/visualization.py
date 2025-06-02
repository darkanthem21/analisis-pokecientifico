# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_categorical_distribution(dataframe, column_name, plot_title, xlabel, ylabel, palette='viridis', figsize=(12, 7), save_path=None):
    """
    Genera y muestra un gráfico de barras para la distribución de una columna categórica.

    Args:
        dataframe (pd.DataFrame): El DataFrame que contiene los datos.
        column_name (str): El nombre de la columna para graficar.
        plot_title (str): El título del gráfico.
        xlabel (str): La etiqueta para el eje X.
        ylabel (str): La etiqueta para el eje Y.
        palette (str, optional): La paleta de colores para Seaborn. Defaults to 'viridis'.
        figsize (tuple, optional): El tamaño de la figura. Defaults to (12, 7).
        save_path (str, optional): Ruta para guardar la imagen. Si es None, no se guarda. Defaults to None.
    """
    plt.figure(figsize=figsize)
    sns.countplot(data=dataframe, y=column_name, order=dataframe[column_name].value_counts().index, palette=palette)
    plt.title(plot_title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Gráfico guardado en: {save_path}")

    plt.show()

def plot_correlation_heatmap(dataframe, title="Matriz de Correlación", figsize=(10, 8), cmap='coolwarm', save_path=None):
    """
    Genera y muestra un heatmap de la matriz de correlación de un DataFrame.

    Args:
        dataframe (pd.DataFrame): DataFrame con columnas numéricas para correlacionar.
        title (str, optional): Título del gráfico. Defaults to "Matriz de Correlación".
        figsize (tuple, optional): Tamaño de la figura. Defaults to (10, 8).
        cmap (str, optional): Mapa de colores para el heatmap. Defaults to 'coolwarm'.
        save_path (str, optional): Ruta para guardar la imagen. Si es None, no se guarda. Defaults to None.
    """
    correlation_matrix = dataframe.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(correlation_matrix, annot=True, cmap=cmap, fmt=".2f", linewidths=.5)
    plt.title(title, fontsize=16)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Gráfico guardado en: {save_path}")

    plt.show()
