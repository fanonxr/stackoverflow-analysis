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

