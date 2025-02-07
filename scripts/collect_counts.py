"""Script to run counts collection for the ViolentRiskFactors project."""

from lisc import Counts
from lisc.utils import SCDB, save_object, load_api_key

###################################################################################################
###################################################################################################


# Set whether to run a test run
TEST = False

# Set locations / names for loading files
DB_NAME = './data'
TERMS_DIR = './terms/'
API_FILE = 'api_key.txt'

import os
print(os.path.abspath(os.path.join(TERMS_DIR, 'riskfactors.txt')))


# Set label for secondary terms to run
#   Options: 'cognitive', 'disorders', 'erp'
LABEL = 'violence'

# Set collection settings
LOGGING = None
VERBOSE = True

# Update settings for test run
if TEST:
    LABEL = 'test'

###################################################################################################
###################################################################################################

def main():

    db = SCDB(DB_NAME)
    api_key = load_api_key(API_FILE)

    counts = Counts()

    if TEST:
        counts.add_terms([['Antisocial attitudes'], ['Unemployment'], ['Impulsivity']], dim='A')
        counts.add_terms([['physical violence'], ['sexual recidivism']], dim='B')
    else:
        counts.add_terms('riskfactors.txt', dim='A', directory=TERMS_DIR)
        counts.add_terms('erps_exclude.txt', term_type='exclusions', dim='A', directory=TERMS_DIR)
        counts.add_labels('erp_labels.txt', dim='A', directory=TERMS_DIR)
        if LABEL != 'erp':
            counts.add_terms(LABEL + '.txt', dim='B', directory=TERMS_DIR)

    print('\n\nRUNNING COUNTS COLLECTION')
    print('RUNNING COLLECTION: ', LABEL, '\n\n')

    counts.run_collection(db='pubmed', api_key=api_key, logging=LOGGING, verbose=VERBOSE)

    # Ruta per desar el fitxer sense duplicar 'data'
    save_path = os.path.join('data', 'counts')
    os.makedirs(save_path, exist_ok=True)

    # Desem l'objecte counts sense duplicar db
    save_object(counts, os.path.join(save_path, 'counts_' + LABEL + '.p'))

    print('\n\nCOUNTS COLLECTION FINISHED\n\n')



if __name__ == "__main__":
    main()
