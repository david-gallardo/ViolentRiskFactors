"""
Run analysis on collected words data.

This script loads the pre-computed words object for "words_violence",
processes the data (aggregates and creates summaries for each term),
and then exports the results (including wordcloud and years plots).
The summary information is saved as JSON files.
"""

from lisc.data import ArticlesAll
from lisc.utils import SCDB, load_object
from lisc.io import load_txt_file
from lisc.plts.words import plot_years, plot_wordcloud
import os
import seaborn as sns
import json
import numpy as np
import pandas as pd

###################################################################################################
# Configuration settings

# Set data for words object to load.
# Since SCDB appends a "data" folder internally, we set DB_NAME to '.' (the project root).
TERM_DIR = './terms'      # Folder with term files (assumed to be in the project root)
DB_NAME = '.'             # Project root; SCDB will use "./data" internally
F_NAME = 'words_violence' # File name (without extension) for the words object

# Set the year range for plotting.
YEAR_RANGE = [None, 2020]

# Set the file format for saved plots.
PLT_EXT = '.pdf'

# Set plotting context.
sns.set_context('talk')

###################################################################################################
###################################################################################################

def main():
    """Main function to analyze the words data and export summaries and plots."""
    
    print('\n\n ANALYZING WORDS DATA \n\n')
    
    # Initialize the database object using SCDB.
    # With DB_NAME = '.', SCDB will construct its internal paths relative to the project root.
    db = SCDB(DB_NAME)
    
    # Assegurar que la carpeta per a les paraules existeix.
    words_folder = db.get_folder_path('words')
    if not os.path.exists(words_folder):
        os.makedirs(words_folder, exist_ok=True)
        print("Words folder created:", os.path.abspath(words_folder))
    else:
        print("Words folder exists:", os.path.abspath(words_folder))
    
    # Assegurar que la carpeta "summary" existeix dins de la carpeta de paraules.
    summary_folder = os.path.join(words_folder, 'summary')
    if not os.path.exists(summary_folder):
        os.makedirs(summary_folder, exist_ok=True)
        print("Summary folder created:", os.path.abspath(summary_folder))
    else:
        print("Summary folder exists:", os.path.abspath(summary_folder))
    
    # Assegurar que també existeixen les carpetes per als gràfics.
    # Aquestes funcions (plot_wordcloud, plot_years) estan intentant desar els fitxers a "figures/wc" i "figures/years".
    if not os.path.exists("figures"):
        os.makedirs("figures", exist_ok=True)
        print("Figures folder created:", os.path.abspath("figures"))
    else:
        print("Figures folder exists:", os.path.abspath("figures"))
    
    wc_folder = os.path.join("figures", "wc")
    if not os.path.exists(wc_folder):
        os.makedirs(wc_folder, exist_ok=True)
        print("WC folder created:", os.path.abspath(wc_folder))
    else:
        print("WC folder exists:", os.path.abspath(wc_folder))
    
    years_folder = os.path.join("figures", "years")
    if not os.path.exists(years_folder):
        os.makedirs(years_folder, exist_ok=True)
        print("Years folder created:", os.path.abspath(years_folder))
    else:
        print("Years folder exists:", os.path.abspath(years_folder))
    
    # Load the words object and the analysis exclusions file.
    words = load_object(F_NAME, db)
    exclusions = load_txt_file('analysis_exclusions.txt', TERM_DIR, split_elements=False)
    
    # For each term in the words object, process the data.
    for erp in words.labels:
        print('Analyzing', erp, 'data')
        
        # Load data for the current term.
        words[erp].load(directory=db)
        
        # Aggregate article data for the current term, applying exclusions.
        erp_data = ArticlesAll(words[erp], exclusions=exclusions)
        
        # Create a summary of the aggregated data, add custom info (e.g., full term name) and save the summary.
        erp_data.create_summary()
        erp_data.summary['name'] = erp_data.term.search[0]
        erp_data.save_summary(directory=db)
        
        # Create and save the wordcloud figure.
        plot_wordcloud(erp_data.words, 20,
                       file_name='wc/' + erp + PLT_EXT, directory=db,
                       save_kwargs={'transparent': True, 'dpi': 600}, close=True)
        
        # Create and save the years figure.
        plot_years(erp_data.years, year_range=YEAR_RANGE,
                   file_name='years/' + erp + PLT_EXT, directory=db,
                   save_kwargs={'transparent': True, 'dpi': 600}, close=True)
        
        # Clear the loaded data for the current term to free memory.
        words[erp].clear()
    
    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
