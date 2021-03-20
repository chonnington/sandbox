import csv

from io import StringIO
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)

inputFile = 'books/breakfast_at_tiffanys.txt'


def loadRecord(line):
    """Parse a CSV line"""
    input = StringIO.StringIO(line)
    reader = csv.DictReader(input,
                            fieldnames=["name",
                                        "favouriteAnimal"])
    return reader.next()

input = sc.textFile(inputFile).map(loadRecord)


