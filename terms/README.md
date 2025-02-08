# Terms Lists

This sub-folder contains a collection of terms lists used for the project.

For an overview of the search terms that were used, and brief descriptions, see
[this notebook](https://github.com/ERPscanr/ERPscanr/blob/main/notebooks/01-SearchTerms.ipynb).

### ERP Terms

The following files relate to term definitions and metadata about the ERP components included in this project.

- `riskfactors.txt` contains a list of risk factors related to violence terms and synonyms
- `erp_labels.txt` contains a list of labels that are used for each ERP term
- `erps_exclude.txt` contains a list of customized exclusion terms used for each ERP term
- `latencies.txt` contains a list of canonical latencies for each ERP term

Note that each of the ERP files should have the same number of lines, and each line index relates to the same ERP across files.
Blank lines indicate that there is no entry for the current ERP.

### Association Terms

The following lists relate to association terms:

- `violence.txt` contains a list of the violence association terms
- `disease.txt` contains a list of the disease association terms

### Dropped Terms

The following lists contain ERPs that were initially considered but ultimately dropped from the project.

- `dropped_erps.txt` contains a list of ERPs that were dropped due to having too few results
    - These ERPs return at least 1 result, but were dropped for being too rare (<10 results)
- `sensory_erps.txt`
    - There ERPs have canonical latencies less than 100 ms (early sensory responses) and were not included

Note that dropped terms were removed prior to data collection, and so are not included in the collected dataset.

### Analysis Related Lists

The following lists contain lists of terms that were used during the analysis (post data collection).

- `analysis_exclusions.txt` a list of general terms that are excluded from analysis of common keywords, words, etc
