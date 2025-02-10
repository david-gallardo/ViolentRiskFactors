from bs4 import XMLParsedAsHTMLWarning
import warnings
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

""""Script to run words collection for the ViolentRiskFactors project for both violence and recidivism."""

import os
import pickle
import pandas as pd
from lisc import Words
from lisc.utils import SCDB, save_object, load_api_key

# Global configuration settings
TEST = False
DB_NAME = './data'
TERMS_DIR = './terms/'
API_FILE = 'api_key.txt'
FIELD = 'TIAB'
RETMAX = 10000
SAVE_N_CLEAR = True
LOGGING = None

if TEST:
    RETMAX = 5
    SAVE_N_CLEAR = False

def collect_words_violence():
    label = 'violence'
    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)
    words = Words()

    if TEST:
        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')
    else:
        words.add_terms('riskfactors.txt', directory=TERMS_DIR)
        words.add_terms('erps_exclude.txt', term_type='exclusions', directory=TERMS_DIR)
        words.add_labels('riskfactor_labels.txt', directory=TERMS_DIR)

    print('\n\nRUNNING WORDS COLLECTION for:', label, '\n\n')

    # Define the save directory using a relative path that matches SCDB’s internal structure
    save_dir = os.path.join(DB_NAME,'words', 'raw', 'violence')
    os.makedirs(save_dir, exist_ok=True)
    print("Directory created (if not exists):", os.path.abspath(save_dir))

    words.run_collection(db='pubmed', retmax=RETMAX, field=FIELD,
                         usehistory=True, api_key=api_key, save_and_clear=SAVE_N_CLEAR,
                         directory=db, logging=LOGGING, verbose=True)

    save_object(words, 'words_' + label, db)
    print('\n\nWORDS COLLECTION FINISHED for:', label, '\n\n')

def collect_words_recidivism():
    label = 'recidivism'
    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)
    words = Words()

    if TEST:
        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')
    else:
        words.add_terms('riskfactors.txt', directory=TERMS_DIR)
        words.add_terms('erps_exclude.txt', term_type='exclusions', directory=TERMS_DIR)
        words.add_labels('riskfactor_labels.txt', directory=TERMS_DIR)

    print('\n\nRUNNING WORDS COLLECTION for:', label, '\n\n')

    save_dir = os.path.join(DB_NAME, 'words', 'raw', 'recidivism')
    os.makedirs(save_dir, exist_ok=True)
    print("Directory created (if not exists):", os.path.abspath(save_dir))

    words.run_collection(db='pubmed', retmax=RETMAX, field=FIELD,
                         usehistory=True, api_key=api_key, save_and_clear=SAVE_N_CLEAR,
                         directory=db, logging=LOGGING, verbose=True)

    save_object(words, 'words_' + label, db)
    print('\n\nWORDS COLLECTION FINISHED for:', label, '\n\n')

if __name__ == "__main__":
    collect_words_violence()
    collect_words_recidivism()
