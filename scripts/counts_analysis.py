"""
Run analysis on collected words data.

This script loads pre-computed counts objects (for cognitive and disorder-related terms),
processes the data by dropping low-frequency components and normalizing scores, and then
extracts the top associations between terms. The results are saved as JSON files, where each
file summarizes the top associations for a specific term.
"""

import os
import json
import numpy as np
from lisc.utils import SCDB, load_object

###################################################################################################
# Configuration settings

# Directories and file names for loading the counts objects and terms
TERM_DIR = './terms'          # Directory for the term files (not directly used here)
DB_NAME = './data'            # Database directory where counts objects are stored
COG_F_NAME = 'counts_violence'  # File name (without extension) for cognitive counts object
DIS_F_NAME = 'counts_disorders' # File name (without extension) for disorder counts object

# Parameters for analysis
N_TERMS = 3   # Number of top associations to extract for each term
N_DROP = 100  # Number of low-frequency items to drop before normalization

###################################################################################################

def main():
    """Main function to analyze counts data and save the top associations."""

    print('\n\n ANALYZING COUNTS DATA \n\n')

    # Initialize the database object using SCDB.
    # This loads the directory structure and paths defined in DB_NAME.
    db = SCDB(DB_NAME)

    # Define the paths for saving the summary of counts and associations.
    # These directories will be created inside the counts directory of the database.
    counts_summary_path = os.path.join(db.paths['counts'], 'summary')
    counts_assocs_path = os.path.join(db.paths['counts'], 'assocs')

    # Create the summary and associations directories if they do not already exist.
    for path in [counts_summary_path, counts_assocs_path]:
        if not os.path.exists(path):
            os.mkdir(path)

    # Load the counts objects for both cognitive and disorder associations.
    # These objects contain co-occurrence scores and term labels.
    cog_counts = load_object(COG_F_NAME, directory=db)
    dis_counts = load_object(DIS_F_NAME, directory=db)

    # Pre-process the counts objects by:
    # 1. Dropping data corresponding to low-frequency terms (using N_DROP).
    # 2. Computing normalized scores for dimension 'A'.
    cog_counts.drop_data(N_DROP)
    cog_counts.compute_score('normalize', dim='A')
    dis_counts.drop_data(N_DROP)
    dis_counts.compute_score('normalize', dim='A')

    # For each term in the 'A' dimension (e.g., family-related terms),
    # collect the top associations from the co-occurrence scores.
    for l_ind, label in enumerate(cog_counts.terms['A'].labels):

        # Initialize a dictionary to store top associations from both cognitive and disorder counts.
        top_assocs = {'top_cog_assocs': [], 'top_dis_assocs': []}

        # Extract the top N_TERMS associations for cognitive terms.
        # np.argsort returns indices that would sort the array.
        # np.flip reverses the order so that the highest scores come first.
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(cog_counts.score[l_ind, :]))):
            top_assocs['top_cog_assocs'].append(cog_counts.terms['B'][assoc].label)

        # Extract the top N_TERMS associations for disorder terms.
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(dis_counts.score[l_ind, :]))):
            top_assocs['top_dis_assocs'].append(dis_counts.terms['B'][assoc].label)

        # Save the top associations for the current 'A' term in a JSON file.
        # Each file is named after the label of the term.
        summary_filepath = os.path.join(counts_summary_path, label + '.json')
        with open(summary_filepath, 'w') as outfile:
            json.dump(top_assocs, outfile)

    # Collect and save top components associated with each cognitive-related term (from dimension 'B').
    cog_assocs = {}
    for l_ind, label in enumerate(cog_counts.terms['B'].labels):
        cog_assocs[label] = []
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(cog_counts.score[:, l_ind]))):
            cog_assocs[label].append(cog_counts.terms['A'][assoc].label)
    # Save the cognitive associations dictionary in a JSON file.
    cog_assocs_filepath = os.path.join(counts_assocs_path, 'cognitive.json')
    with open(cog_assocs_filepath, 'w') as outfile:
        json.dump(cog_assocs, outfile)

    # Collect and save top components associated with each disorder-related term (from dimension 'B').
    dis_assocs = {}
    for l_ind, label in enumerate(dis_counts.terms['B'].labels):
        dis_assocs[label] = []
        for t_ind, assoc in zip(range(N_TERMS), np.flip(np.argsort(dis_counts.score[:, l_ind]))):
            dis_assocs[label].append(dis_counts.terms['A'][assoc].label)
    # Save the disorder associations dictionary in a JSON file.
    dis_assocs_filepath = os.path.join(counts_assocs_path, 'disorders.json')
    with open(dis_assocs_filepath, 'w') as outfile:
        json.dump(dis_assocs, outfile)

    print('\n\n FINISHED ANALYZING WORDS DATA \n\n')


if __name__ == "__main__":
    main()
