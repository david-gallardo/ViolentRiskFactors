"""Classes and functions to store and process extracted paper data."""

from erpsc.core.errors import InconsistentDataError

##########################################################################
############################ ERPSC - ERPWords ############################
##########################################################################

class ERPData(object):
    """An object to hold the word results for a given ERP or term.

    Attributes
    ----------
    erp : str
        Name of the ERP word data relates to.
    ids : list of int
        Pubmed article ids for all articles included in object.
    n_articles : int
        Number of articles included in object.
    titles : list of str
        Titles of all articles included in object.
    journals : list of tuple of (str, str)
        List of journals articles come from. (Journal Name, ISO abbreviation).
    authors : list of list of str
        Authors of all articles included in object.
    words : list of list of unicode
        Words extracted from each article.
    years : list of int
        Publication year of each article included in object.
    kws : list of list of str
        List of keywords for each article included in the object.
    all_words : list of unicode
        All words from all articles.
    freqs : nltk FreqDist
        Frequency distribution of all words.
    """

    def __init__(self, erp):
        """Initialize ERPWords() object.

        Parameters
        ----------
        erp  : str
            Name of the ERP.
        """

        # Set the given string as the erp label
        self.erp = erp

        # Initialize list to store pubmed article ids
        self.ids = list()

        # Initialize to store article count
        self.n_articles = 0

        # Initiliaze to store data pulled from articles
        self.titles = list()
        self.journals = list()
        self.authors = list()
        self.words = list()
        self.kws = list()
        self.years = list()

        # Initialize a list to store all words (across all papers)
        self.all_words = list()

        # Initialize to store FreqDists (across all words)
        self.freqs = list()


    def add_id(self, new_id):
        """Add a new ID to ERPWords object.

        Parameters
        ----------
        new_id : int
            The ID number of the current article.
        """

        self.ids.append(new_id)


    def add_title(self, new_title):
        """Add a new title to ERPWords object.

        Parameters
        ----------
        new_title : str
            The title of the current article.
        """

        self.titles.append(new_title)


    def add_authors(self, new_authors):
        """Add a new set of authors to ERPWords object.

        Parameters
        ----------
        new_authors : list of tuple of (str, str, str, str)
            Author list of the current article, as (LastName, FirstName, Initials, Affiliation).
        """

        self.authors.append(new_authors)


    def add_journal(self, new_journal, new_iso_abbrev):
        """Add a new journal name and ISO abbreviation to ERPWords object.

        Parameters
        ----------
        new_journal : str
            Name of the journal current article comes from.
        new_iso_abbrev : str
            Standardized abbreviation of journal name article comes from.
        """

        self.journals.append((new_journal, new_iso_abbrev))


    def add_words(self, new_words):
        """Add new words to ERPWords object.

        Parameters
        ----------
        new_words : list of str
            List of words from the current article.
        """

        self.words.append(new_words)


    def add_kws(self, new_kws):
        """Add new keywords to ERPWords object.

        Parameters
        ----------
        new_kws : list of str
            List of keywords from current article.
        """

        self.kws.append(new_kws)


    def add_year(self, new_year):
        """Add a new year to ERPWords object.

        Parameters
        ----------
        new_year : int
            The year the current article was published.
        """

        self.years.append(new_year)


    def increment_n_articles(self):
        """Increment the number of articles included in current object."""

        self.n_articles += 1


    def check_results(self):
        """Check for consistencty in extracted results.

        If everything worked, each data field (ids, titles, words, years)
        should have the same length, equal to the number of articles.
        Some entries may be blank (missing data), but if the lengths are not
        the same then the data does not line up and cannot be trusted.
        """

        # Check that all data fields have length n_articles
        if not (self.n_articles == len(self.ids) == len(self.titles) == len(self.words)
                == len(self.journals) == len(self.authors) == len(self.kws) == len(self.years)):

            # If not, print out error
            raise InconsistentDataError('ERP Words data is inconsistent.')