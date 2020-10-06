#!/usr/bin/env python

import pandas as pd
import csv
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


def createDataFrame(path):
    """Creates a dataframe from a given path, calculates the amount of planets
    of a host star and changes spectraltypes to their upper generalization. 

    Keyword arguments:
    path -- the path where the data is located
    
    Returns:
    df -- the created pandas dataframe
    """
    df = pd.read_csv(path)
    df = df[['planet_name', 'planet_mass', 'orbital_radius', 'host_name', 
             'spectral_type', 'stellar_age', 'stellar_radius', 
             'stellar_mass', 'stellar_temperature', 'stellar_luminosity', 
             'optical_magnitude', 'near_ir_magnitude', 
             'stellar_surface_gravity', 'stellar_metallicity']]
    
    df = df.dropna(subset=['spectral_type'])
    df.spectral_type = df.spectral_type.str[0:1]
    df.spectral_type = df.spectral_type.str.strip()
    classification = np.array(['O','B','A','F','G','K','M'])
    df = df[df.spectral_type.isin(classification)]
    df.insert(4, "amount_of_planets", 0)
    df.amount_of_planets = df.groupby('host_name')['host_name'].transform('count')
    
    df.planet_mass = np.log10(df.planet_mass)
    df.orbital_radius = np.log10(df.orbital_radius)
    
    df = df.sort_values(by=['host_name'])
    df = df.reset_index(drop=True) 
    
    return df


def drawCountPlot(df, colors, order):
    """Draws a seaborn countplot for the column spectral_type of the given 
    dataframe. 

    Keyword arguments:
    df -- the data used as input
    colors -- the colors used to paint bars
    order -- the order used in X axis
    """
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15,8))
    sns.set_palette(sns.color_palette(colors))
    sns.countplot(x=df.spectral_type, data=df, order=order)
    plt.show()
    
    
def drawCountPlotPlanets(df):
    """Draws a seaborn countplot for the column amount_of_planets of the given 
    dataframe. 

    Keyword arguments:
    df -- the data used as input
    """
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(15,8))
    sns.countplot(x=df.amount_of_planets, data=df, palette='Reds_d')
    plt.show()


def drawHist(data, xLabel, unit, binSize, title):
    """Draws a matplotlib histogram of the given data and prints several
    stochastic attributes. 

    Keyword arguments:
    data -- the data used as input
    xLabel -- the label for the X axis
    unit -- the unit of the data that is appended to the xLabel
    binSize - size of a single bin
    """
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)[0].astype(float)
    
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    sigma = np.std(data)
    
    
    bins = np.arange(min(data), max(data) + 1, binSize)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12,7))
    plt.hist(data, bins=bins, histtype='bar') 
    plt.title(title)
    plt.xlabel(xLabel + " " + unit)
    plt.ylabel('count')
    ymax = ax.get_ylim()[1]
    ax.vlines(mean, 0, ymax, color='red', label='mean')
    ax.vlines(mean-sigma, 0, ymax, color='red', linestyle='--', 
              label='mean +/- std')
    ax.vlines(mean+sigma, 0, ymax, color='red', linestyle='--')
    plt.legend()
    plt.show()
    
    print("Einheit: ", unit)
    print("Minimum: ", round(data.min(),3))
    print("Maximum: ", round(data.max(),3))
    print("Mittelwert: ", round(mean,3))
    print("Median: ", round(median,3))
    print("Modus: ", round(mode[0],3))
    print("Standardabweichung: ", round(sigma, 3))
    print("1. Quartil: ", round(q1,3))
    print("3. Quartil: ", round(q3,3))
    print("Quartilsdifferenz: ", round(iqr,3))
    
    
def drawPairPlot(df):
    """Draws a seaborn pairplot of the given data that uses the spectral_type
    column as hue. 

    Keyword arguments:
    df -- the dataframe used as input
    """
    plt.style.use('dark_background')
    warnings.filterwarnings("ignore")
    types = getSpectralTypes()
    colors = getColors()
    sns.set_palette(sns.color_palette(colors))
    g = sns.pairplot(df, hue="spectral_type", hue_order=types, dropna=True,
                     vars=["stellar_age", "stellar_temperature", 
                           "stellar_luminosity", "stellar_mass", 
                           "stellar_radius", "stellar_surface_gravity", 
                           "optical_magnitude", "stellar_metallicity"])
    plt.show()
    

def drawBoxplot(data, column, yLabel, unit):
    """Draws a seaborn boxplot for each spectral type of the given data. 

    Keyword arguments:
    data -- the dataframe used as input
    column -- the column of the data, which is used as Y axis
    """
    sns.set(style='darkgrid')
    plt.style.use('default')
    plt.style.use('dark_background')
    types = getSpectralTypes()
    colors = getColors()
    sns.set_palette(sns.color_palette(colors))
    fig, ax = plt.subplots(figsize=(14,7))
    sns.boxplot(x='spectral_type', y=column, data=data, order=types)
    plt.ylabel(yLabel + " " + unit)
    plt.xlabel("Spektraltyp")
    plt.show()
    
    

def drawStackedBarPlot(df, column, hue):
    """Draws a stacked barplot

    Keyword arguments:
    df -- the data used as input
    column -- the column used for Y axis
    hue -- the column used as hue
    """
    plt.style.use('default')
    plt.style.use('dark_background')
    p_table = pd.pivot_table(df, index=column, 
                         columns=hue, aggfunc='size')
    p_table = p_table.div(p_table.sum(axis=1), axis=0)
    p_table.plot.bar(stacked=True, figsize=(14,7))
    plt.xlabel('Spekraltyp')
    plt.ylabel('Anteil')
    plt.show()
    
    
def drawCatplot(df, xColumn):
    """Draws a seaborn catplot

    Keyword arguments:
    df -- the data used as input
    xXolumn -- the column used for X axis
    """
    plt.style.use('default')
    plt.style.use('dark_background')
    types = getSpectralTypes()
    colors = getColors()
    sns.set_palette(sns.color_palette(colors))
    
    sns.catplot(x=xColumn, y="spectral_type", data=df, order=types, height=3, 
    aspect=4);
    plt.show()





def getSpectralTypes():
    """Returns an array of spectral types without type O."""
    return ['B','A','F','G','K','M']
    
    
def getColors():
    """Returns an array of spectral colors without the color of type O."""
    return ['#8c99fc', '#cacefd', '#fff1d7', '#feda98', '#fda85a', '#fc6647']


def dropDuplicateStars(df):
    """Drops all stars that occur more than once in the given dataframe. The 
    first star occured is beeing kept.

    Keyword arguments:
    df -- the dataframe used as input
    
    Returns:
    df -- the edited dataframe
    """
    df = df.drop_duplicates(subset ="host_name", keep = 'first')
    return df


    
