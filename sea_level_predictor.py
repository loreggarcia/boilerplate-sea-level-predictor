import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Anos para previsão (1880 a 2050)
    years_all = pd.Series(range(1880, 2051))
    # Níveis do mar previstos
    sea_levels_all = res_all.intercept + res_all.slope * years_all
    # Plotar a linha
    ax.plot(years_all, sea_levels_all, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    # Filtrar dados a partir do ano 2000
    df_recent = df[df['Year'] >= 2000]
    # Regressão nos dados recentes
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    # Anos para a nova previsão (2000 a 2050)
    years_recent = pd.Series(range(2000, 2051))
    # Níveis do mar previstos (nova linha)
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent
    # Plotar a segunda linha
    ax.plot(years_recent, sea_levels_recent, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()