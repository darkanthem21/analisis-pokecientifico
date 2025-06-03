# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd # Necesario para type hinting y manipulación dentro de las funciones si es el caso

def plot_average_stats_comparison(comparison_df: pd.DataFrame, title: str, ylabel: str, xlabel: str, legend_title: str, palette_dict: dict, save_path=None, figsize=(12,7)):
    """
    Genera un gráfico de barras comparando estadísticas promedio entre grupos.

    Args:
        comparison_df (pd.DataFrame): DataFrame 'melted' con columnas 'Stat', 'Average_Stat_Value', 'Group'.
        title (str): Título del gráfico.
        ylabel (str): Etiqueta del eje Y.
        xlabel (str): Etiqueta del eje X.
        legend_title (str): Título de la leyenda.
        palette_dict (dict): Diccionario para mapear grupos a colores.
        save_path (str, optional): Ruta para guardar la imagen. Defaults to None.
    """
    plt.figure(figsize=figsize)
    sns.barplot(x='Stat', y='Average_Stat_Value', hue='Group', data=comparison_df, palette=palette_dict)
    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title=legend_title)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Gráfico guardado en: {save_path}")
    plt.show()

def plot_total_stats_kde_comparison(
    data_group1: pd.Series,
    data_group2: pd.Series,
    label_group1: str,
    label_group2: str,
    title: str,
    xlabel: str,
    save_path=None,
    figsize=(10,6)
):
    """
    Genera un gráfico KDE comparando la distribución de estadísticas totales entre dos grupos.

    Args:
        data_group1 (pd.Series): Serie con las estadísticas totales del primer grupo.
        data_group2 (pd.Series): Serie con las estadísticas totales del segundo grupo.
        label_group1 (str): Etiqueta para el primer grupo.
        label_group2 (str): Etiqueta para el segundo grupo.
        title (str): Título del gráfico.
        xlabel (str): Etiqueta del eje X.
        save_path (str, optional): Ruta para guardar la imagen. Defaults to None.
    """
    plt.figure(figsize=figsize)
    sns.kdeplot(data_group1, label=label_group1, fill=True, color='skyblue', alpha=0.7)
    sns.kdeplot(data_group2, label=label_group2, fill=True, color='lightcoral', alpha=0.7)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Densidad', fontsize=12) # Y-axis label is 'Density' for KDE plots
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"Gráfico guardado en: {save_path}")
    plt.show()

# Puedes añadir más funciones de visualización aquí
