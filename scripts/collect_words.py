from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

""""Script to run words collection for the ViolentRiskFactors project for both violence and recidivism."""

import os
import pickle
import pandas as pd
from lisc import Words
from lisc.utils import SCDB, save_object, load_api_key

###################################################################################################
# Configuration settings

# Set whether to run a test run
TEST = False

# Set locations / names for loading files
DB_NAME = './data'
TERMS_DIR = './terms/'
API_FILE = 'api_key.txt'

# Set e-utils settings
FIELD = 'TIAB'
RETMAX = 10000

# Set collection settings
SAVE_N_CLEAR = True
LOGGING = None

# Update settings for test run
if TEST:
    RETMAX = 5
    SAVE_N_CLEAR = False

###################################################################################################
###################################################################################################

def run_words_collection(label, db, api_key):
    """
    Run words collection for a given secondary term label.
    
    For the primary terms (risk factors) and their exclusions/labels, always load:
      - 'riskfactors.txt'
      - 'erps_exclude.txt'
      - 'erp_labels.txt'
    
    For the secondary terms, load a file named according to the label,
    e.g. 'violence.txt' or 'recidivism.txt'.
    """
    words = Words()

    if TEST:
        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')
    else:
        words.add_terms('riskfactors.txt', directory=TERMS_DIR)
        words.add_terms('erps_exclude.txt', term_type='exclusions', directory=TERMS_DIR)
        words.add_labels('erp_labels.txt', directory=TERMS_DIR)
        if label != 'erp':
            words.add_terms(label + '.txt', directory=TERMS_DIR)

    print('\n\nRUNNING WORDS COLLECTION for:', label, '\n\n')

    words.run_collection(db='pubmed', retmax=RETMAX, field=FIELD,
                         usehistory=True, api_key=api_key, save_and_clear=SAVE_N_CLEAR,
                         directory=db, logging=LOGGING, verbose=True)

    # Desa l'objecte Words amb el nom que inclou el label (ex.: "words_violence.p")
    save_object(words, 'words_' + label, db)

    print('\n\nWORDS COLLECTION FINISHED for:', label, '\n\n')

def main():
    # Inicialitza la base de dades i carrega l'API key
    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)

    # Executa la col·lecció per a ambdós labels: "violence" i "recidivism"
    for label in ['violence', 'recidivism']:
        run_words_collection(label, db, api_key)

if __name__ == "__main__":
    main()
