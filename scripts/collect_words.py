"""Script to run words collection for the ERP-SCANR project."""

from lisc import Words
from lisc.utils import SCDB, save_object, load_api_key

###################################################################################################
###################################################################################################

# Set whether to run a test run
TEST = False

# Set label for collection
LABEL = 'violence'

# Set locations / names for loading files
DB_NAME = '../data'
TERMS_DIR = '../terms/'
API_FILE = 'api_key.txt'

# Set e-utils settings
FIELD = 'TIAB'
RETMAX = 10000

# Set collection settings
SAVE_N_CLEAR = True
LOGGING = None

# Update settings for test run
if TEST:
    LABEL = 'test'
    RETMAX = 5
    SAVE_N_CLEAR = False

###################################################################################################
###################################################################################################

def main():

    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)

    words = Words()

    if TEST:

        words.add_terms([['P100'], ['N100']])
        words.add_terms([['protein'], ['protein']], term_type='exclusions')

    else:

        words.add_terms('riskfactors.txt', directory=TERMS_DIR)
        words.add_terms('erps_exclude.txt', term_type='exclusions', directory=TERMS_DIR)
        words.add_labels('erp_labels.txt', directory=TERMS_DIR)

    print('\n\nRUNNING WORDS COLLECTION')

    words.run_collection(db='pubmed', retmax=RETMAX, field=FIELD,
                         usehistory=True, api_key=api_key, save_and_clear=SAVE_N_CLEAR,
                         directory=db, logging=LOGGING, verbose=True)

    save_object(words, 'words_' + LABEL, db)

    print('\n\nWORDS COLLECTION FINISHED\n\n')


if __name__ == "__main__":
    main()
