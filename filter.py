#!env/bin/python
import csv
import re

def search():
    """
    Remove all non-Dayton properties from the taxroll
    """
    all_props = open("./taxroll.csv", "r")
    filtered = open("./daytontaxroll.csv", "w")

    all_reader =  csv.reader(all_props)
    match_writer = csv.writer(filtered)
    patternobj = re.compile('^R72.*$')

    next(all_reader)
    for line in all_reader:
        if patternobj.match(line[1]) is not None:
            match_writer.writerow(line)

    all_props.close()
    filtered.close()


if __name__ == "__main__":
    search()
