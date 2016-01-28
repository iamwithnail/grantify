import nltk
import string
import os
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer


""" Takes a directory of technical narratives (at projectroot/narratives) and grants spreadsheet, and analyses them for semantic similarity to
 'match' clients with potential grants (including closed ones).
 Reads in individual texts using docx2txt, creates a single string, then 'tokenizes' that into a list of strings
 The roots of those strings are then analysed to calculate the TFIDF vectors for each document (effectively, 'how
 important is each term in that particular document' - different texts (grants and tech narratives) are then compared
 using cosine similarity to get a 'match' for each grant.
 Although bulky, the programme requires scipy as well as sklearn, as there is a dependency from the TfidfVectorizer
 package that breaks without scipy: this is reflected in the requirements.txt file"""





def stem_tokens(tokens, stemmer):
    """takes the list of tokens and stems them so that we can compare the roots of the words"""
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def tokenize(text):
    """converts a raw string or unicode entry into tokens, i.e. a list of strings
    note that this does not remove stopwords or duplicates"""
    tokens = nltk.word_tokenize(text)
    stemmer = PorterStemmer()
    stems = stem_tokens(tokens, stemmer)
    return stems


def remove_stopwords(token_list):
    """it's important to remove stopwords before calculating the TF-IFD, otherwise the functional
    stopwords will 'pollute' the word corpus"""
    from nltk.corpus import stopwords
    stopwords_removed = [word for word in token_list if word not in stopwords.words('english')]
    return stopwords_removed


def remove_duplicates(token_list):
    #it's important to remove stopwords before calculating the TF-IFD, otherwise the functional
    #stopwords will 'pollute' the word corpus
    from nltk.corpus import stopwords
    duplicates_removed = []
    duplicates_removed = [word for word in token_list if word not in duplicates_removed]
    return duplicates_removed


def process_files():
    for subdir, dirs, files in os.walk("."):
        for file in files:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file

            if filepath.endswith(".asm"):
                print (filepath)
def main():
    token_dict = {}
    filename= "GC.docx"
    text = docx2txt.process(filename)
    lowers = text.lower()
    #no_punctuation = lowers.translate(None, string.punctuation)
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

    token_dict["gocardless"] = lowers
    tfs = tfidf.fit_transform(token_dict.values())
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print feature_names[col], ' - ', tfs[0, col]

def process_narratives():
    narrative_outputs = {}
    narrative_list = os.listdir('narratives')
    for narrative in narrative_list:
        if not narrative == '.DS_Store':
            #don't try and read the hidden files
            text = docx2txt.process('narratives'+narrative)
            tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

main()



