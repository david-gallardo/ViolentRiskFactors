# ViolentRiskFactors
[![Website](https://img.shields.io/badge/site-violentriskfactors.github.io-informational.svg)](https://violentriskfactors.github.io/)
[![Paper](https://img.shields.io/badge/paper-s41598.022.05939.9-success.svg)](https://doi.org/10.1038/s41598-022-05939-9)

`ViolentRiskFactors` project repository: automated meta-analysis of violence and delinquency risk factors literature.

## Overview

Violence and delinquency have been the focus of numerous studies, exploring the risk factors that contribute to these behaviors.
This project utilizes automated literature collection and text-mining from published research articles to summarize the literature on violence and recidivism risk factors, identifying patterns and associations across various risk domains such as familial, social, and individual factors.

The results of this project are hosted online on the [project website](https://osf.io/ats8c/).

## Project Guide

The goal of this project is to explore and summarize the existing literature on risk factors associated with violence and delinquency. To achieve this, we manually curated a dictionary of known risk factors and relevant terms from the literature. This list of terms is available in the `terms` sub-folder and viewable in the `SearchTerms` notebook.

For data collection, this project uses two main approaches:
- The 'Words' approach gathers text and metadata (e.g., authors, journals, keywords, and publication date) from all articles identified through search terms. This data is used to build profiles of violence and delinquency risk factors.
- The 'Count' approach collects data on the co-occurrence of violence-related terms and other pre-defined terms of interest, including psychological, social, and environmental risk factors. This data is used to analyze patterns and relationships between different risk factors. This project is inspired and based on [Donoghue & Votek (2022)](https://www.nature.com/articles/s41598-022-05939-9).

The project aims to analyze trends in the literature and provide insights into how various risk factors relate to violent and delinquent behavior.

You can explore the outputs of this project by visiting the [project website](https://osf.io/ats8c/), which features individual profiles of all the examined risk factors and group-level analyses.

For details on how the project was conducted and to view the underlying code, you can explore this repository.
As a starting point, the `notebooks` provide an overview of the approach used in this project. To conduct similar literature analyses, refer to the [LISC](https://github.com/lisc-tools/lisc) tool.

## Reference

This project is described in the following paper:

    [Authors] (2025). TO BE DEFINED. DOI: [Placeholder DOI]

Direct link: [Placeholder DOI]

## Requirements

This project is written in Python 3 and requires Python >= 3.7 to run.

The project requires standard scientific Python libraries, listed in `requirements.txt`, which can be installed via [Anaconda Distribution](https://www.anaconda.com/distribution/).

Additional requirements include:
- [lisc](https://github.com/lisc-tools/lisc) >= 0.2.0

## Repository Layout

This project repository is organized in the following way:

- `build_site/` contains scripts to create the project website
- `code/` contains the code used for this project
- `docs/` contains the files that define the project website
- `notebooks/` contains Jupyter notebooks detailing the project workflow
- `scripts/` contains scripts for data collection and analysis
- `terms/` contains all the search terms used for literature collection

To re-run the analyses using the existing dataset, download the dataset (see below) and add it to a `data` folder within the project directory.

You can also run a new data collection using the terms defined in the `terms` sub-folder and the data collection scripts in the `scripts` sub-folder.

The primary data analyses are conducted in the `notebooks` after data collection.

## Data

This project uses literature data.

The literature dataset collected and analyzed in this project is openly available at this [OSF repository](https://osf.io/ats8c/).
