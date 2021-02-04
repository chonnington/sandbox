
outputFile = 'foo'

def writeRecords(records):
    
    """Write out CSV lines"""
    
    output = StringIO.StringIO()
    writer = csv.DictWriter(output, fieldnames=["name", "favoriteAnimal"]) 
    for record in records:
        writer.writerow(record) 
    return [output.getvalue()]
    
pandaLovers.mapPartitions(writeRecords).saveAsTextFile(outputFile)