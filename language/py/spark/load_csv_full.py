
import csv

from io import StringIO
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf=conf)


def loadRecords(fileNameContents):
    """Load all the records in a given file"""
    input = StringIO.StringIO(fileNameContents[1])
    reader = csv.DictReader(input, fieldnames=["name", "favoriteAnimal"])
    return reader


inputFile = "tmp/fake.csv"
fullFileData = sc.wholeTextFiles(inputFile).flatMap(loadRecords)