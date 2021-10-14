import pip
import pandas as pd
from datetime import datetime


# checks whether packages are already installed or not.
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


# Writes information to csv file to administer the scanned profiles
def write_to_csv(name, age, member, sentence_id, num_rows):
    exportFile = # Insert Export Directory
    valueInsertDF = pd.DataFrame(
        {'Name': name,
         'Age': age,
         'Member': member,
         'DateTime': datetime.now(),
         'SentenceID': sentence_id
         }, index=[num_rows])

    # opening the csv file in 'a+' mode
    file = open(exportFile, 'a+', newline='')

    # write to csv and close the file
    valueInsertDF.to_csv(file, mode='a', index=False, header=False, sep=';')
    file.close()


# Based on given value, checks which opening sentence we should return to message
def level_of_interest(level):
    pd.options.display.max_colwidth = 300
    sentencesFile = # Insert directory to file with opening sentences
    data = pd.read_csv(sentencesFile, sep=';')
    Sentence = data.loc[data['ID'] == level, 'Sentence'].to_string(index=False)
    return Sentence


def calculate_corr_tags(listOther, listSelf):
    if len(listOther) > 0:
        c = 0
        for tag in listOther:
            tagtext = tag.text
            if tagtext in set(listSelf):
                c = c + 1
                # print('tag ' + tagtext.__str__() + ' does correspond')
            else:
                # print('tag ' + tagtext.__str__() + ' does NOT correspond')
                c = c
        return c
    else:
        return ()
