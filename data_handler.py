# the file that will handle and load in the data
import csv
from collections import defaultdict, Counter


def load_survey_data(filePath):
    """
    function to load in the data and handle it as a csv reader
    :param filePath: the string to the file
    :return a csv reader generator object containing the contents of the csv
    """
    with open(filePath) as f:
        # generator object
        csv_reader = csv.DictReader(f)

    return csv_reader


def get_hobbyist_count(reader):
    """
    function to get the total count of hobbyist vs non hobbyist
    :param reader: a generator object containing the contents of th csv
    :return: a dict of numbers indicting how many people are vs not hobbyist
    """

    # a counter object to store how many people say yes vs no
    counts = Counter()

    # the value will be yes or no and will increment the count by 1
    for line in reader:
        counts[line['Hobbyist']] += 1

    return counts


def get_language(reader):
    """
    function to get the most popular language
    :param reader:
    :return: a list containing the Counter collection and the total amount of people using that language
    """

    language_counter = Counter()
    total = 0

    for line in reader:
        # get all the langauages that the developer has worked with
        languages = line['LanguageWorkedWith'].split(";")

        # loop over the list of languages and increment the counter
        language_counter.update(languages)
        total += 1

    return [language_counter, total]


def get_type_of_developer(reader):
    """
    :params: reader csv generator object containing the contents of the csv file
    :return: 
    """
    language_counter = Counter()
    total = 0
    dev_type_info = {}
    
    for line in reader:
        dev_types = line['DevType'].split(';')
        
        for dev_type in dev_types:
            # set default checks to see if we have a value for that key, (dev type)
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'language_counter': Counter()
            })

            languages = line['LanguageWorkedWith'].split(';')
            dev_type_info[dev_type]['language_counter'].update(languages)
            dev_type_info[dev_type]['total'] += 1
